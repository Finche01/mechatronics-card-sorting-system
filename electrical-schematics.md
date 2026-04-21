# Electrical Schematics

## System Architecture Overview

The electrical system consists of three main subsystems:
1. **Power Distribution System** - Multi-voltage power supply and protection circuits
2. **Motor Control System** - Stepper motor drivers and motion control
3. **Pneumatic Control System** - Solenoid valves and air pressure management
---

## Power Distribution Schematic

![Power Distribution Schematic](image/schematic_images/Power_schematic.png)

### Power Supply Architecture

| Supply Unit | Input | Output | Current | Application |
|:------------|:------|:-------|:--------|:------------|
| **POWER_SUPPLY_1** | 240VAC / 1.3A | 24VDC | PLC rated | PLC and I/O modules |
| **POWER_SUPPLY_2** | 240VAC / 8.5A | 24VDC | Motors rated | Motor drivers |
| **DC/DC CONVERTER** | 24VDC | 12VDC | TBD | Solenoids/Accessories |

### Terminal Block Assignments

| Terminal Block | Voltage | Usage |
|:--------------|:--------|:------|
| **TB_Logic** | +24V / 0V | PLC I/O Power Terminals |
| **TB_Motor** | +24V / 0V | Motor Power Terminals |
| **TB3** | +12V / 0V | Solenoids Flipper |

---

## Motor Control Schematic

![Motor Control Schematic](image/schematic_images/Motor_schematic.png)

### System Components

| Component | Description | Specifications |
|:----------|:------------|:---------------|
| **C2-14DR** | I/O module | Relay |
| **Motors** | Motors for each axis |  |
| **Motor driver** | Stepper motor driver (x4) | translates electrical pulse into motor actuation |
| **Limit switch** | feedback sensor to signal the limits of each axis | two switches per axis |
| **ESTOP** | Emergency stop button | Normally closed circuit |

### Motor Driver Pinout
|![Motor Control Schematic](image/schematic_images/Motor_driver.png)| ![Motor Control Schematic](image/schematic_images/Motor_driver_configuration_switch.png)|

##Signal
| Pin | Function | Description |
|:----|:---------|:-----------|
| PUL+ | Step signal positive | Receives pulse train from PLC/controller - each pulse advances motor by one microstep |
| PUL- | Step signal ground | Ground reference for step signal (differential pair with STEP+) |
| DIR+ | Direction signal positive | Sets rotation direction: HIGH = clockwise, LOW = counter-clockwise |
| DIR- | Direction signal ground | Ground reference for direction signal (differential pair with DIR+) |
| ENA+ | Enable signal positive | Motor enable control: LOW = motor energized and holding, HIGH = motor disabled/free |
| ENA- | Enable signal ground | Ground reference for enable signal (differential pair with ENA+) |

##High Voltage
| Pin | Function | Description |
| GND | Power ground | Common ground reference for driver electronics |
| VEL+ | Velocity feedback | Optional encoder feedback signal (positive) for closed-loop control |
| VEL- | Velocity feedback | Optional encoder feedback signal (ground/negative) |
| A+ / A- | Motor coil A | Phase A winding connections to stepper motor (bipolar) |
| B+ / B- | Motor coil B | Phase B winding connections to stepper motor (bipolar) |



### Control Signal Flow

1. **Logic Power (TB_LOGIC)**: Supplies 5V to CS-H62 controller and I/O circuits
2. **CS-H62 Controller**: Generates STEP/DIR/ENABLE signals for all 4 motor drivers
3. **Emergency Stop (ESTOP)**: Breaks enable circuit to all motors when activated
4. **Motor Power (TB_MOTOR)**: Supplies 24V to motor drivers (TB1-4 terminals)
5. **Motors (MTR1-4)**: X-axis, Y1-axis, Y2-axis, and Z-axis stepper motors

---

## Pneumatic Control Schematic

![Pneumatic Control Schematic](image/schematic_images/Pneumatic_schematic.png)

### Pneumatic System Components

| Component | Description | Function |
|:----------|:------------|:---------|
| **C0-16TD1** | I/O Combo module | 24V DC for solenoid control |
| **C2-14DR** | I/O Combo module | Powers tilt motor |
| **SOL1-4** | 5/2 solenoid valves | Double-acting pneumatic control |
| **PRESSURE_SWITCH** | Air pressure sensor | Monitors system pressure |
| **COMP_PROTECT_SW** | Compressor protection switch | Overload protection |
| **FLIPPER_MOTOR** | Tilt mechanism motor | 24V DC motor |
| **lED STRIP** | | |

---
