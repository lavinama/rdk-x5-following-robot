#!/usr/bin/env python3
"""Challenge 2 — sensor + peripheral, no external parts (M1 kit still shipping).

Blinks the RDK X5's onboard ACT LED (GPIO-driven, normally the kernel
heartbeat) while reading the SoC's DDR and CPU thermal sensors each tick.
Run with sudo:  sudo python3 challenge2_sensor.py [ticks]
"""
import sys
import time
from pathlib import Path

LED = Path("/sys/class/leds/ACT")
ZONES = {
    p.joinpath("type").read_text().strip(): p / "temp"
    for p in sorted(Path("/sys/class/thermal").glob("thermal_zone*"))
}
TICKS = int(sys.argv[1]) if len(sys.argv) > 1 else 120  # 0.5 s/tick -> 60 s


def set_trigger(value):
    (LED / "trigger").write_text(value)


def set_led(on):
    (LED / "brightness").write_text("1" if on else "0")


try:
    set_trigger("none")  # take the LED over from the kernel heartbeat
    for i in range(TICKS):
        on = i % 2 == 0
        set_led(on)
        temps = "  ".join(
            f"{name}: {int(z.read_text()) / 1000:.1f}C" for name, z in ZONES.items()
        )
        print(f"[{i * 0.5:5.1f}s] ACT LED {'ON ' if on else 'off'}  |  {temps}", flush=True)
        time.sleep(0.5)
finally:
    set_led(False)
    set_trigger("heartbeat")  # hand the LED back to the kernel
    print("ACT LED restored to heartbeat trigger.")
