#include <stdint.h>

enum class Fault : uint8_t {
    None, EStop, Limit, OverTemp, OverCurrent, CommTimeout, SensorFault
};

struct AxisState {
    float position_mm = 0.0f;
    float velocity = 0.0f;
    float temperature_c = 0.0f;
    bool limit_min = false;
    bool limit_max = false;
    Fault fault = Fault::None;
};

static AxisState axes[4];
static bool estop_active = false;

void enterSafeState() {
    for (auto &axis : axes) axis.velocity = 0.0f;
}

bool safetyCheck() {
    if (estop_active) return false;
    for (const auto &axis : axes) {
        if (axis.fault != Fault::None) return false;
        if (axis.temperature_c > 70.0f) return false; // provisional software limit
    }
    return true;
}

void controlLoop() {
    if (!safetyCheck()) {
        enterSafeState();
        return;
    }
    // HAL-specific sensor acquisition, bounded motion control, and telemetry go here.
}

int main() {
    while (true) controlLoop();
    return 0;
}
