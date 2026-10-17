# Power and Communications Architecture

## Power domains

1. Central source and protected distribution.
2. Separate actuator power from logic/sensor power where practical.
3. Local branch protection at each arm.
4. Hardware E-stop path designed around the actual actuator safety requirements.

## Communications

Each arm has a local controller connected to a protected field bus. RS-485 or CAN may be used as the physical layer after system-level selection and validation.

Messages should include:

- arm identifier
- command sequence number
- timestamp or cycle counter
- requested state
- measured position/velocity
- temperature and current telemetry
- fault code
- watchdog status

## Electrical engineering requirements

- Calculate worst-case continuous and peak current for all 12 arms.
- Size conductors, connectors, fuses, switches, and power supplies from those calculations.
- Verify voltage drop at maximum cable length.
- Provide over-current and short-circuit protection.
- Separate high-current actuator routing from sensitive sensor wiring where necessary.
- Bond/shield according to the final EMC architecture.

No specific power-supply rating is approved by this reference document; it must follow validated actuator and duty-cycle data.
