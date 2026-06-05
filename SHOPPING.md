# Hardware / BOM — Following Robot (RDK X5 4GB + ROSMASTER M1)

**v0.2 · 2026-06-05** · Vision-only person-following robot. **Hardware acquired** — this is
now a manifest, not a shopping list.

## Owned (the brain)
- **RDK X5 — 4GB**, 10 TOPS BPU (reused as the kit's controller; *not* buying the kit's board)
- microSD SanDisk Ultra 64GB (A1/U1/V10)
- RDKOS 3.5.0 Desktop image (already flashed for Stage 1)
- Host: MacBook Pro 16" M4 Pro, macOS

## ROSMASTER M1 kit — purchased (RDK X5 config, no SBC)
| Component | Detail | Role |
|---|---|---|
| Chassis + wheels | Mecanum, 80 mm omnidirectional | drive |
| Motors | 4× 520 geared **encoder** motors (1:56) | closed-loop speed |
| Expansion board | motor control + power mgmt + **onboard IMU**; USB/serial to RDK X5 | replaces all DIY motor/power wiring |
| Battery | 12.6 V 6000 mAh (~3 h) + charger | integrated, regulated power |
| **Camera** | USB HD + 2-DOF pan/tilt (**RGB — confirmed**) | YOLO input |
| Voice | mic array + speaker + AI-LLM voice module (Dify) | Stage 3 **2nd workload** |
| Extras | 0.91" OLED, cooling fan, wireless gamepad, USB hub, microSD, cables, tools | teleop/e-stop, thermal, dev |

## Dropped vs the old DIY BOM
~~2WD chassis, TT motors, TB6612FNG driver, 2S LiPo, 5 V buck, switch, wiring, tilt mount~~ — **all replaced by the M1 kit.**

## Still to verify / small items
- [x] **Camera confirmed: RGB USB-HD + 2-DOF** → follow-distance from **bbox size** (depth path not needed).
- [ ] Yahboom's **RDK X5 ROS 2 image / Rosmaster software** package (so motor + camera drivers are ready).
- [ ] (Optional) a 2nd microSD to keep your Stage 1 RDKOS separate from Yahboom's robot image.

## RAM note (4GB)
Core task fits 4GB because YOLO runs on the **BPU**. Keep it lean: run the robot **headless**,
light model (yolov8n/v5n @ 640×480), voice/LLM **cloud-side** (Dify), not a local LLM. See PROPOSAL.
