import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "LICENSE",
    "config/arm_roles.json",
    "docs/ENGINEERING_PLAN.md",
    "docs/ASSEMBLY_SEQUENCE.md",
    "docs/MECHANICAL_INTERFACES.md",
    "docs/SAFETY_VALIDATION.md",
    "electronics/POWER_AND_BUS.md",
    "firmware/arm_controller/main.cpp",
    "firmware/arm_controller/README.md",
    "firmware/arm_controller/protocol.md",
    "models/Arm01_Master.scad",
    "bom/ARM12_BOM.csv",
]

missing = [p for p in required if not (ROOT / p).is_file()]
if missing:
    print("Missing required files:")
    print("\n".join(missing))
    sys.exit(1)

roles = json.loads((ROOT / "config/arm_roles.json").read_text(encoding="utf-8"))
if roles.get("arm_count") != 12 or len(roles.get("arms", [])) != 12:
    raise SystemExit("arm_roles.json must define exactly 12 arms")

ids = [a.get("id") for a in roles["arms"]]
expected = [f"ARM{i:02d}" for i in range(1, 13)]
if ids != expected:
    raise SystemExit(f"Unexpected arm IDs: {ids}")

print("Robot-test-files validation passed.")
print("12 arm modules, required engineering documents, firmware scaffold, CAD references, and BOM are present.")
