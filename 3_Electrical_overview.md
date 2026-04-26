# Electrical Overview
The electrical system consists of three main subsystems:
1. **Power Distribution System** - Multi-voltage power supply and protection circuits
2. **Motor Control System** - Stepper motor drivers and motion control
3. **Pneumatic Control System** - Solenoid valves and air pressure management

---

# 1. Power Distribution Schematic
<div align="center">
  <img src="image/schematic_images/Power_schematic.png" width="80%">
</div>

## Power Supply Units
| Supply Unit | Input | Output | Current | Application |
|:------------|:------|:-------|:--------|:------------|
| **POWER_SUPPLY_1** | 240VAC / 1.3A | 24VDC | PLC rated | PLC and I/O modules |
| **POWER_SUPPLY_2** | 240VAC / 8.5A | 24VDC | Motors rated | Motor drivers |
| **DC/DC CONVERTER** | 24VDC | 12VDC | TBD | Solenoids/Accessories |

## Terminal Blocks
| Terminal Block | Voltage | Usage |
|:---------------|:--------|:------|
| **TB_Logic** | +24V / 0V | PLC I/O Power Terminals |
| **TB_Motor** | +24V / 0V | Motor Power Terminals |
| **TB3** | +12V / 0V | Flipper solenoid power terminals|

---

# 2. Motor Control Schematic
<div align="left">
  <img src="image/schematic_images/Motor_schematic.png" width="80%">
</div>

| Component | Description | Specifications |
|:----------|:------------|:---------------|
| **C2-14DR** | I/O module | Relay output |
| **Motors** | Stepper motors for each axis | X, Y1, Y2, Z-axis |
| **Motor Driver** | Stepper motor driver (x4) | Translates electrical pulses into motor actuation |
| **Limit Switch** | Feedback sensor to signal axis limits | Two switches per axis connected in parallel |
| **ESTOP** | Emergency stop button | Normally closed circuit |

### Motor Driver 
| Motor Driver Pins | DIP Switches (driver config) |
|:--------------------|:--------------|
| ![Motor Driver Pinout](image/schematic_images/Motor_driver.png) | ![Motor Driver Configuration Switch](image/schematic_images/Motor_driver_configuration_switch.png) |

---

### Power & Motor Connections

| Pin | Function | Description |
|:----|:---------|:-----------|
| **GND** | Ground | Common ground for the driver |
| **V+** | Power input | DC supply input to the motor driver |
| **A+ / A-** | Motor coil A | Energizes/de-energizes motor phase A |
| **B+ / B-** | Motor coil B | Energizes/de-energizes motor phase B |

---

### Signal Pins

| Pin | Function | Description |
|:----|:---------|:-----------|
| **PUL+** | Step signal (+) | Receives pulses from the PLC; each pulse moves the motor one step (configurable via DIP switches) |
| **PUL-** | Step signal (-) | Ground/reference for the step signal |
| **DIR+** | Direction (+) | Controls motor direction (HIGH = clockwise, LOW = counterclockwise) |
| **DIR-** | Direction (-) | Ground/reference for the direction signal |
| **ENA+** | Enable (+) | Enables or disables the motor (LOW = enabled, HIGH = disabled) |
| **ENA-** | Enable (-) | Ground/reference for the enable signal |

# 3. Pneumatic Control Schematic
<div align="left">
  <img src="image/schematic_images/Pneumatic_schematic.png" width="70%">
</div>

| Component | Description | Function |
|:----------|:------------|:---------|
| **C0-16TD1** | I/O Combo module | 24V DC for solenoid control |
| **C2-14DR** | I/O Combo module | Relay output control |
| **SOL1-4** | 5/2 solenoid valves | Double-acting pneumatic control |
| **Pressure Switch** | Air pressure sensor | Monitors system pressure |
| **Flipper Motor** | Tilt mechanism motor | 24V geared DC motor |
| **LED Strip** | Status / vision lighting | Provides diffused lighting for machine vision |
---