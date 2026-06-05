# Following Robot — Roadmap (Stage 1 → 3)

**v0.2 · 2026-06-05** · Brain: RDK X5 4GB · Platform: ROSMASTER M1 (purchased) · Final demo + submission: **2026-07-15**

> **Critical path = kit shipping.** Ordered 2026-06-05; AliExpress to US can be 2–4 weeks, so the M1 may not land until ~Jun 19–Jul 3. Strategy: **front-load every task that doesn't need the kit** (Stage 1 board bring-up, YOLO on the bare board, controller logic against recorded video, ROS 2 setup). Assemble + integrate the moment it arrives.

## Stage 1 — Ignite (closes **Jun 10**) — *board only, kit NOT required*
| Task | Plan |
|---|---|
| Challenge 1 — bring-up | Flash RDKOS 3.5.0 → network → SSH → Discord check-in |
| Challenge 2 — sensor | **GPIO LED blink** via sysfs (no extra hardware) |
| Challenge 3 — first AI | **YOLO / classifier on a static image** on the BPU (rule = on-device, not live) |
| Submit | screenshots A/B/C + repo README + Discord permalink → showcase PR |
> The M1 won't arrive by the 10th — do **not** make Stage 1 depend on it.

## Stage 2 → 3 build plan
| Week | Dates | Stage | Milestones | Exit criteria |
|---|---|---|---|---|
| W1 | Jun 11–17 | 2 | Finalize PROPOSAL/architecture/BOM. Set up ROS 2 Humble workspace. **On the bare RDK X5: get YOLO person detection on the BPU** (static images / borrowed USB webcam) to de-risk early. | Stage 2 docs done; live person detections + FPS recorded on the board. |
| W2 | Jun 18–25 | 2→submit | **If kit arrived:** assemble chassis, flash Yahboom RDK X5 ROS 2 image, teleop with **gamepad** (verify motors/encoders), camera node up. **If not:** write `follow_controller` against recorded video; prep launch files. **Submit Stage 2.** | Robot drives via gamepad + camera streams (or controller validated on recordings); Stage 2 PR opened. |
| W3 | Jun 26–Jul 2 | 3 | Wire `camera → detector → selector → follow_controller → rosmaster_driver`. Close the loop: detections → `cmd_vel` → mecanum motors. Floor test + PID tune. | Robot follows a person on the floor (rough). |
| W4 | Jul 3–8 | 3 | Add **voice** 2nd workload ("follow"/"stop"), e-stop + safety limits, lost-target search. Fill **benchmark** table (FPS/latency, BPU/CPU, RAM — headless 4GB). | Stable following + voice control; 2 concurrent workloads documented. |
| W5 | Jul 9–12 | 3 | Hardening: ≥ 60 s continuous multi-task run, distance/centering tuning, optional 2-DOF camera tracking. | Reliable demo-quality following. |
| W6 | Jul 13–15 | 3→ship | Record **demo video (3–7 min, 1080p)**. Finalize `docs/`. Tag `v1.0-demo`. Community post. **Showcase PR.** | All Stage 3 deliverables in by Jul 15. |

## Dependencies
- **Shipping (W1→W2)** gates all physical work — mitigated by front-loading software (above).
- **YOLO FPS (W1/W3)** gates the follow loop — don't tune control until detection is real-time on the BPU.
- **Power/assembly (W2)** gates closed-loop driving — verify teleop + no brownout before autonomous runs.

## Buffer / cuttable scope (if behind)
Drop in this order: 2-DOF active camera tracking → voice 2nd workload (detection+control alone still satisfies "two workloads") → re-ID (fall back to largest-central person). **Non-negotiable:** core following + BPU inference + safe-stop + the demo video.
