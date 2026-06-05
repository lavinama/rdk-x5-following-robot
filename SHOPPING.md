# Shopping List — Person-Following Robot (RDK X5)

Project: **Following Robot** — a vision-only robot that detects and follows a person.
A single camera + BPU YOLO person detection drives the follow loop (turn to center the
person, throttle to hold distance). **No distance sensors needed for control.**

Have already: RDK X5 board, microSD (SanDisk Ultra 64GB), USB-C power, macOS host.

---

## 0. Same-day / this week (Stage 1 closes Jun 10 — optional)

Stage 1 needs **no purchases** (GPIO LED blink for the sensor task + YOLO/classifier on a
static image for the AI task, both on the board alone). Only buy if you want a *live*
camera demo for Stage 1:

- [ ] **Camera** — confirm whether the kit already includes a MIPI camera. If not, a local
      **USB UVC webcam** (same-day) works for Stage 1. Otherwise just wait for the CSI
      camera below and use static images for Stage 1.

## 1. Order now — needed to drive the robot (Stage 3, ~1–2 wk lead)

- [ ] **Camera (CRITICAL)** — MIPI CSI preferred (low latency, RDK-native). IMX219 module
      (Raspberry Pi v2 form factor) or the official D-Robotics RDK camera. Verify the exact
      module is RDK X5-compatible. *(USB webcam = easy fallback.)*
- [ ] **Robot chassis** — 2WD or 4WD car chassis with TT DC gear motors + wheels + caster.
      (Encoders optional — not required; the camera closes the heading loop.)
- [ ] **Motor driver** — TB6612FNG (preferred) or L298N. Driven by RDK X5 PWM/GPIO.
- [ ] **Power**
  - [ ] Battery — 2S LiPo (7.4 V), friendly for TT motors (~3–6 V); or an 18650 pack.
  - [ ] **5 V buck converter** (≥4–5 A) to power the RDK X5 cleanly off the battery.
  - [ ] On/off switch + connectors (common ground between motor & logic rails).
- [ ] **Wiring & mounting** — jumper wires (M-F / F-F), standoffs, and a **tilt mount** for
      the camera (aim it slightly down so a person is framed from ~1–3 m).

## 2. Optional / recommended

- [ ] **1× front ToF (VL53L1X) or HC-SR04 ultrasonic** — safety e-stop only, independent of
      vision. Cheap insurance + lets you claim genuine sensor fusion (camera + range).
- [ ] **IMU (MPU6050 / BNO055)** — smoother heading during turns. Not required.

---

## Why these choices (design context)

- **Vision-only, person-following.** Perception = **YOLO person detection** (COCO class 0),
  which ships pre-converted in `rdk_model_zoo` — zero model work. Control = two proportional
  loops: **turn** from the person's bbox center-x, **throttle** from bbox size (distance).
- **Distance comes from the camera** (bbox size), so range sensors are not needed for the
  follow loop — keep one only as an optional hard e-stop.
- **Two concurrent workloads** (Stage 3): YOLO detection on **BPU** + follow/motor control
  loop on **CPU** (optionally a 2nd model — pose/gesture "stop" command).
- **Sensor fusion** (Stage 3, if claimed) = camera + the optional front range sensor.

> Note: same BOM whether person- or wall-following. We chose person-following for
> implementation simplicity (no floor-segmentation model exists in the zoo for vision
> wall-steering). See PROPOSAL.md for the full design.
