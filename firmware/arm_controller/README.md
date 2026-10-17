# ARM Controller Firmware

Prototype local controller scaffold for the ARM01–ARM12 modules.

## Responsibilities

- Read local sensors.
- Enforce bounded control-loop timing.
- Monitor temperature, current, limits, and communications watchdogs.
- Enter a safe state on E-stop or critical fault.
- Exchange commands and telemetry with the high-level controller.

The current `main.cpp` is intentionally hardware-agnostic. A production implementation must add the selected MCU HAL, actuator driver, watchdog configuration, deterministic timing, nonvolatile configuration, and validated safety architecture.

## Commissioning

Start with sensors disconnected from actuators where practical, then use a fixture and reduced limits for every first powered test.
