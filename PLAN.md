# Following Robot — Master Plan (Stage 1 → 3)

**Brain:** RDK X5 4GB (10 TOPS) · **Platform:** Yahboom ROSMASTER M1 · **Goal:** vision-only person-following robot · **All work due 2026-07-15.**

The single checklist of steps to complete each stage. Status: ✅ done · 🔜 next · ⬜ todo.
Detailed docs: Stage 1 working doc on branch `docs/stage1-scaffold`; Stage 2/3 design
(PROPOSAL / ROADMAP / SHOPPING) on branch `docs/stage2-plan`. They merge here as each stage completes.

---

## Stage 1 — Ignite · closes **Jun 10** · *board only (M1 kit not needed)*
1. ✅ Register — Discord + Google Form + RDK Studio account
2. ✅ Download + MD5-verify RDKOS 3.5.0 Desktop image
3. ✅ Flash microSD (RDK Studio) → first boot
4. ✅ Network + SSH from Mac (`ssh sunrise@192.168.128.10`, `uname -a` ✓; Wi-Fi `192.168.1.215`) → **Screenshot A**
5. ✅ Sensor (Challenge 2): no parts on hand → onboard ACT LED blink + DDR/CPU thermal-sensor log (`scripts/challenge2_sensor.py`) → **Screenshot B**
6. ✅ First AI (Challenge 3): YOLO11n on `bus.jpg` — BPU forward **13.1 ms (~76 FPS)**, bus 0.93 + 4 persons → **Screenshot C** (`~/Desktop/screenshot-C-yolo-result.jpg`)
7. ✅ Discord Stage 1 check-in → [permalink](https://discord.com/channels/1300358874280230994/1511058147350151168/1514414310296649849)
8. ✅ Fill the evidence into the Stage 1 doc; make the repo **public**
9. ✅ Competition `projects/` PR opened: [D-Robotics/Robotics-Dream-Keeper-Challenge#2](https://github.com/D-Robotics/Robotics-Dream-Keeper-Challenge/pull/2)

→ earns **RDK Explorer**

## Stage 2 — Build · Jun 11–25 · *design (no kit needed)*
1. ⬜ Concept + measurable goals (PROPOSAL Ch.1)
2. ⬜ ROS 2 architecture — node graph + BPU/CPU compute allocation (PROPOSAL Ch.2)
3. ⬜ Engineering plan — BOM, roadmap, risks, repo structure (PROPOSAL Ch.3)
4. ⬜ Early de-risk: YOLO person detection on the bare RDK X5 (BPU), record FPS
5. ⬜ Submit Stage 2 (PROPOSAL + ROADMAP + community post → `projects/` PR)

→ earns **RDK Builder**

## Stage 3 — Launch · Jun 26–Jul 15 · *build*
1. ⬜ Assemble the ROSMASTER M1; flash Yahboom's RDK X5 ROS 2 image
2. ⬜ Teleop with the gamepad (verify motors/encoders); bring up the camera node
3. ⬜ Integrate: `camera → YOLO (BPU) → target-lock → follow_controller → cmd_vel → mecanum`
4. ⬜ Close the loop: follow a person on the floor; tune the PID
5. ⬜ Add voice ("follow"/"stop") as the 2nd workload + e-stop + lost-target search
6. ⬜ Benchmark — FPS/latency, BPU/CPU, RAM (headless 4GB)
7. ⬜ Demo video (3–7 min, 1080p, ≥30 s continuous); tag `v1.0-demo`; finalize `docs/`
8. ⬜ Community post + showcase `projects/` PR

→ earns **RDK Creator**

---

## Critical path & constraints
- **Stage 1 must be done board-only by Jun 10** — the M1 kit won't arrive in time.
- **Kit shipping** (AliExpress) may slip to late June → front-load all non-kit work (Stage 1, YOLO on the bare board, controller logic against recorded video).
- **4GB RAM:** run the robot **headless**, light model (yolov8n @ 640×480), keep voice/LLM **cloud-side** (Dify) — not a local LLM.
