# Following Robot — Roadmap (Stage 2 → Stage 3 demo)

**Version 0.1 · 2026-06-04** · Target final demo + submission: **2026-07-15**

Gantt-style week plan from Stage 2 design through the Stage 3 launch demo. Parts should be **ordered by ~Jun 12** to land before assembly week.

| Week | Dates | Stage | Milestones | Exit criteria |
|---|---|---|---|---|
| W1 | Jun 11–17 | 2 (Build) | Finalize PROPOSAL, architecture, BOM. **Order all parts.** Set up repo `src/` skeleton + ROS 2 workspace. | Stage 2 docs done; parts ordered; `colcon build` of empty pkgs passes. |
| W2 | Jun 18–25 | 2 → submit | Parts arrive. Assemble chassis, wire motors + TB6612FNG, bring up **camera on board**. Manual `cmd_vel` → motor test (teleop). **Submit Stage 2.** | Robot drives via teleop; camera streams on board; Stage 2 PR opened. |
| W3 | Jun 26–Jul 2 | 3 (Launch) | YOLO person detection on **live camera @ ≥15 FPS (BPU)**. ROS 2 node skeleton wired (`camera → detector → selector`). Benchmark first numbers. | Live detections visible with overlay; FPS recorded. |
| W4 | Jul 3–8 | 3 | Implement `follow_controller` (center + distance PID). Close the loop: detector → control → motors. Bench test, then floor test. Tune. | Robot follows a person on the floor (rough). |
| W5 | Jul 9–12 | 3 | Integration hardening: e-stop + safety limits, lost-target search, **second workload** (pose/gesture stop or obstacle). Fill benchmark table. | Stable following ≥60 s; e-stop works; 2 concurrent workloads documented. |
| W6 | Jul 13–15 | 3 → ship | Record **demo video (3–7 min, 1080p)**. Finalize `docs/` (architecture, calibration, known issues). Tag `v1.0-demo`. Community post. **Showcase PR.** | All Stage 3 deliverables submitted by Jul 15. |

## Critical path & dependencies

- **Parts (W1 order → W2 arrive)** gate everything physical. If late: do W3 detection work on the bare board + webcam in parallel; assemble when parts land.
- **W3 detection FPS** gates **W4 control** — don't start tuning the follow loop until detection is real-time.
- **Power integration (W2)** gates safe motor testing — verify the board doesn't brown out under motor load before closed-loop runs.

## Buffer

W5–W6 hold the slack. If behind, the cuttable scope (in order): second workload → lost-target search → fancy re-ID (fall back to "largest central person"). Core following + BPU + safe-stop + video are non-negotiable for Stage 3.
