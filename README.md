# RDK X5 Following Robot

A vision-guided **person-following robot**: a Yahboom **ROSMASTER M1** mecanum base driven by a
**D-Robotics RDK X5 (4GB, 10 TOPS)**, built for the
[Robotics Dream Keeper Challenge](https://github.com/D-Robotics/Robotics-Dream-Keeper-Challenge).
This documents my Stage 1 ("Ignite") work and grows through Stages 2–3.

- **Participant:** Mario
- **Brain:** RDK X5 — **4GB**, Sunrise 5, 10 TOPS BPU
- **OS:** RDKOS 3.5.0 Desktop (Ubuntu 22.04, arm64)
- **Host:** MacBook Pro 16" (M4 Pro), macOS 15.6.1
- **Platform (Stage 2–3):** ROSMASTER M1 — mecanum, 4× 520 encoder motors, USB HD camera, voice module. *Shipping; **Stage 1 below is board-only** and does not need it.*

> Official submission draft: `submission/Mario-Project-FollowingRobot.md` — copy into a fork of the challenge repo's `projects/` folder when Stage 1 is complete.

---

## Stage 1 — Ignite

Goal: power on the board and run an on-device AI inference task. **Doable with the board alone.**

### Deliverables checklist
- [ ] **Challenge 1 — Board bring-up:** flash OS → network → SSH → Discord check-in
- [ ] **Challenge 2 — Sensor:** GPIO — blink an LED via `Hobot.GPIO`
- [ ] **Challenge 3 — First AI task:** on-device YOLO detection on a static image (BPU)
- [ ] Screenshots A, B, C captured
- [ ] Showcase PR opened to the official `projects/` folder

---

## 1. Flash the OS image

- **Image:** `rdk-x5-ubuntu22-preinstalled-desktop-3.5.0-arm64.img.xz`
  ([archive](https://archive.d-robotics.cc/downloads/os_images/rdk_x5/rdk_os_3.5.0-2026-4-9/) · md5 `b39cd58ab65e838929063e4f1e184d0b`)
- **Tool:** RDK Studio (macOS) — _Choose device → RDK X5 / X5 Module → Choose image → local file → Refresh drives → select card → Stable mode → Start flashing._ (Fallback: balenaEtcher.)
- **Card:** SanDisk Ultra 64GB (A1/U1/V10), read via an Anker 7-in-1 USB-C hub → MacBook.

> 📸 **Screenshot A:** flashing tool (post-flash) + active SSH terminal.

## 2. Network & SSH setup

- **Network:** Wi-Fi (`nmtui`) or Ethernet. Verify internet: `ping -c3 8.8.8.8`.
- **Default login:** `sunrise` / `sunrise` (also `root` / `root`).
- **Board IP:** run `ip addr` on the desktop, or use defaults — Ethernet `192.168.127.10`, USB-C gadget `192.168.128.10`.
- **SSH from Mac:** `ssh sunrise@<board-ip>` → verify with `uname -a`.

## 3. Sensor (Challenge 2) — GPIO LED blink

The USB camera ships with the M1 (not here by the deadline), so the sensor task uses the 40-pin **GPIO** header — the simplest board-only option.

- **Wiring:** LED anode → ~330 Ω resistor → **physical pin 11**; LED cathode → **GND** (e.g. pin 6). *(Verify pin 11 against the RDK X5 40-pin pinout.)*
- **Library:** `Hobot.GPIO` — D-Robotics' RPi.GPIO-compatible lib, preinstalled on RDKOS.

`blink.py`:
```python
import Hobot.GPIO as GPIO, time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)              # physical pin numbering
LED = 11
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
try:
    while True:
        GPIO.output(LED, GPIO.HIGH); time.sleep(0.5)
        GPIO.output(LED, GPIO.LOW);  time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
```
Run: `sudo python3 blink.py` → LED blinks at ~1 Hz.

> **No LED handy?** Either jumper an output pin to an input pin and print the toggling value in software, or use the M1's USB camera once it arrives. Any of camera / IMU / GPIO / mic / motor satisfies Challenge 2.
>
> 📸 **Screenshot B:** the blinking LED (photo/short clip) or the GPIO toggle log.

## 4. First AI task (Challenge 3) — YOLO on the BPU (static image)

Runs on-device on a bundled test image — **no camera required**.

```bash
# 1. Get the sample + model (on the board)
git clone https://github.com/D-Robotics/rdk_model_zoo
cd rdk_model_zoo/samples/vision/ultralytics_yolo
bash model/download_model.sh                 # downloads the BPU .bin model(s)

# 2. Run detection on a bundled test image (test_data/bus.jpg)
cd runtime/python
bash run.sh                                  # exact model/image args: see runtime/python/README.md
```
- **Model:** `<fill in — e.g. yolov8n .bin from download_model.sh>`
- **Exact command I ran:** `<paste here>`
- **Result:** annotated image with bounding boxes, produced on the board (BPU).

*Lighter alternative if YOLO setup is heavy:* `samples/vision/mobilenetv2` image classification on a test image.

> 📸 **Screenshot C:** the annotated detection output, running on the board.

## Dependencies
- `git`; D-Robotics **BPU runtime** + `Hobot.GPIO` (both preinstalled on RDKOS).
- Python: `opencv-python`, `numpy` (`pip3 install opencv-python numpy` if missing).
- Model `.bin` from `rdk_model_zoo` (`model/download_model.sh`).

## Community check-in
- Discord intro / Stage 1 post: `<permalink>`

---

## Roadmap (Stage 2–3 — ROSMASTER M1 + RDK X5 4GB)
- **Stage 2 — Build:** design the person-follower — ROS 2 graph `camera → YOLO (BPU) → target-lock → follow_controller → mecanum`, with voice as a second workload. *(Full plan on the `docs/stage2-plan` branch.)*
- **Stage 3 — Launch:** assemble the M1, integrate real-time BPU YOLO following + voice + safety, benchmark on 4 GB headless, record the demo video.
