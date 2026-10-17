# Arm Controller Protocol

## Command frame

| Field | Type | Purpose |
|---|---|---|
| Version | uint8 | Protocol version |
| Arm ID | uint8 | ARM01–ARM12 identifier |
| Sequence | uint32 | Monotonic command sequence |
| Mode | uint8 | Disabled, Safe, Manual, Auto |
| Position target | float32 | Bounded target value |
| Velocity limit | float32 | Bounded velocity request |
| Flags | uint16 | E-stop/reset/watchdog state |

## Telemetry frame

| Field | Type | Purpose |
|---|---|---|
| Version | uint8 | Protocol version |
| Arm ID | uint8 | Source arm |
| Sequence | uint32 | Latest accepted command |
| Position | float32 | Measured position |
| Velocity | float32 | Measured velocity |
| Temperature | float32 | Controller/actuator temperature |
| Current | float32 | Measured current |
| Fault | uint16 | Fault bitmask |
| Limits | uint16 | Limit-state bitmask |

## Fault behavior

A watchdog timeout, E-stop, critical sensor fault, over-temperature, or over-current condition must transition the controller to its validated safe state. Exact actuator shutdown behavior is platform-specific and must be tested on the selected hardware.
