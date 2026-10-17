# Robot Test Files

Engineering reference project for the modular ARM12 robotic platform.

## Scope
- 12 mechanically identical arm modules
- ARM01 master mechanical reference
- Approx. 1.5–1.6 m conceptual extended reach
- Telescoping forearm
- Modular wrist/tool interface
- Local real-time controller architecture
- Protected power, communications, telemetry, and emergency-stop design

## Repository structure
- `cad/` — DXF-compatible conceptual 2D references
- `models/` — OpenSCAD parametric references
- `bom/` — bill of materials
- `docs/` — assembly, interfaces, and validation
- `electronics/` — power and communications
- `firmware/` — controller scaffold
- `config/` — arm roles and system configuration

These are engineering-reference files, not certified fabrication drawings. Final actuator sizing, structural analysis, fasteners, bearings, thermal limits, guarding, and safety functions require validation for the actual payload and duty cycle.
