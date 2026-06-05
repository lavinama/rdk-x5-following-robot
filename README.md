# RDK X5 Following Robot

A vision-guided **following robot** built on the D-Robotics **RDK X5**, developed for the
[Robotics Dream Keeper Challenge](https://github.com/D-Robotics/Robotics-Dream-Keeper-Challenge).
This repo documents my setup and Stage 1 ("Ignite") work, and will grow with the build
through Stages 2–3.

- **Participant:** Mario
- **Board:** RDK X5 (Sunrise 5, 10 TOPS BPU)
- **OS:** RDKOS 3.5.0 Desktop (Ubuntu 22.04, arm64)
- **Host:** MacBook Pro 16" (M4 Pro), macOS 15.6.1

> The official submission lives in `submission/Mario-Project-FollowingRobot.md` (a draft to
> copy into a fork of the challenge repo's `projects/` folder when Stage 1 is complete).

---

## Stage 1 — Ignite

Goal: power on the board and run an on-device AI inference task.

### Deliverables checklist
- [ ] **Challenge 1 — Board bring-up:** flash OS → network → SSH → Discord check-in
- [ ] **Challenge 2 — Sensor:** drive/read one peripheral (camera)
- [ ] **Challenge 3 — First AI task:** on-device inference (YOLO object detection)
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

## 3. Sensor (Challenge 2) — Camera

- **Peripheral:** <MIPI CSI camera / UVC USB camera>
- **Interface:** <fill in>
- **Test command:** `<fill in — e.g. list devices, capture a frame>`

> 📸 **Screenshot B:** live camera preview / sensor output.

## 4. First AI task (Challenge 3) — YOLO object detection

- **Source:** [rdk_model_zoo](https://github.com/D-Robotics/rdk_model_zoo)
- **Model:** <fill in — e.g. YOLOv5s on the BPU>
- **Run command:** `<fill in>`
- **Result:** on-device detection with bounding boxes.

> 📸 **Screenshot C:** annotated detection output running on the board.

## Dependencies
- <fill in: packages, model files, Python deps>

## Community check-in
- Discord intro post: <permalink>

---

## Roadmap
- **Stage 2 — Build:** design the following-robot system (chassis, motors, perception → control loop).
- **Stage 3 — Launch:** integrate ROS 2 + real-time BPU inference for live person/object following.
