# Following Robot

- **Participant:** Mario
- **Stage completed:** 1
- **Repository:** https://github.com/lavinama/rdk-x5-following-robot
- **Demo video:** <add Stage 1 demo link>
- **Community post:** <add Discord permalink>

## Summary

<120–300 words. Describe Stage 1: flashed RDKOS 3.5.0 Desktop onto the RDK X5, brought the
board online and established SSH from a Mac, exercised the camera as the first sensor, and
ran an on-device YOLO object-detection demo on the 10 TOPS BPU — the perception foundation
for a vision-guided following robot.>

## Technical Highlights

- Flashed RDKOS 3.5.0 Desktop (Ubuntu 22.04 arm64) to a SanDisk Ultra 64GB card via RDK Studio on macOS.
- Headless control over SSH (`sunrise@<ip>`); verified networking and internet access.
- Camera (<MIPI/UVC>) brought up as the first sensor.
- On-device inference: YOLO object detection on the X5 BPU from rdk_model_zoo.
- <add metrics: model, input resolution, FPS / latency>

## Links & Evidence

- Screenshot album: <flash + SSH, sensor output, AI detection>
- Benchmarks: <optional FPS / latency table>

---

I agree that this showcase document may be used by the Robotics Dream
Keeper Challenge organizers as described in the official README
(promotion, judging, and archives).
