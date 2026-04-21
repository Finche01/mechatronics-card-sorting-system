# Electrical Schematics

This document provides detailed electrical schematics for the 3-axis motion platform, including motor control, pneumatic systems, and power distribution.

---

## System Architecture Overview

The electrical system consists of three main subsystems:
1. **Motor Control System** - Stepper motor drivers and motion control
2. **Pneumatic Control System** - Solenoid valves and air pressure management
3. **Power Distribution System** - Multi-voltage power supply and protection circuits

---

## Motor Control Schematic

![Motor Control Schematic](image/electrical_images/Motor_schematic.png)

### System Components

| Component | Description | Specifications |
|:----------|:------------|:---------------|
| **TB_LOGIC** | Logic power input terminal | 5V DC |
| **CS-H62** | Stepper motor driver (x4) | Microstep controller |
| **MOTOR_DRIVER_1~4** | Motor driver modules | STEP/DIR/ENABLE control |
| **TB_MOTOR** | Motor power terminal | 24V DC |
| **ESTOP** | Emergency stop button | Normally closed circuit |
| **SW (SWITCH1)** | I/O control switch | Digital input |

### Motor Driver Pinout

Each motor driver (MOTOR_DRIVER_X) has the following connections:

| Pin | Function | Connection |
|:----|:---------|:-----------|
| STEP+ | Step signal positive | From CS-H62 controller |
| STEP- | Step signal ground | Ground reference |
| DIR+ | Direction signal positive | From CS-H62 controller |
| DIR- | Direction signal ground | Ground reference |
| ENA+ | Enable signal positive | From CS-H62 controller |
| ENA- | Enable signal ground | Ground reference |
| GND | Power ground | Common ground |
| VEL+ | Velocity feedback | Optional encoder |
| A+ / A- | Motor coil A | Stepper motor phase A |
| B+ / B- | Motor coil B | Stepper motor phase B |

### Control Signal Flow

1. **Logic Power (TB_LOGIC)**: Supplies 5V to CS-H62 controller and I/O circuits
2. **CS-H62 Controller**: Generates STEP/DIR/ENABLE signals for all 4 motor drivers
3. **Emergency Stop (ESTOP)**: Breaks enable circuit to all motors when activated
4. **Motor Power (TB_MOTOR)**: Supplies 24V to motor drivers (TB1-4 terminals)
5. **Motors (MTR1-4)**: X-axis, Y1-axis, Y2-axis, and Z-axis stepper motors

---

## Pneumatic Control Schematic

![Pneumatic Control Schematic](image/electrical_images/Pneumatic_schematic.png)

### Pneumatic System Components

| Component | Description | Function |
|:----------|:------------|:---------|
| **TB_LOGIC** | Logic power input | 24V DC for solenoid control |
| **TB_L12** | 12V power terminal | Powers tilt motor |
| **CS-H610** | Pneumatic controller | Manages solenoid valves |
| **SOL1-4** | 5/2 solenoid valves | Double-acting pneumatic control |
| **PRESSURE_SWITCH** | Air pressure sensor | Monitors system pressure |
| **COMP_PROTECT_SW** | Compressor protection switch | Overload protection |
| **PLC_SW** | PLC control switch | Manual/Auto mode selection |
| **TILT_MOTOR** | Tilt mechanism motor | 24V DC motor |

### Solenoid Valve Configuration

Each solenoid valve (SOL1-SOL4) controls a pneumatic actuator:

| Valve | Port A | Port B | Function |
|:------|:-------|:-------|:---------|
| **SOL1** | A+ | B+ | Actuator 1 extend/retract |
| **SOL2** | A+ | B+ | Actuator 2 extend/retract |
| **SOL3** | A+ | B+ | Actuator 3 extend/retract |
| **SOL4** | A+ | B+ | Vacuum/pressure control |

### Pneumatic Signal Flow

1. **Air Supply**: Compressed air at regulated pressure (typically 6 bar / 87 PSI)
2. **Pressure Monitoring**: PRESSURE_SWITCH monitors system pressure
3. **Valve Control**: CS-H610 activates solenoids based on PLC commands
4. **Actuator Control**: 5/2 valves direct air to extend or retract cylinders
5. **Safety**: COMP_PROTECT_SW protects compressor from overload

---

## Power Distribution Schematic

![Power Distribution Schematic](image/electrical_images/Power_schematic.png)

### Power Supply Architecture

| Supply Unit | Input | Output | Current | Application |
|:------------|:------|:-------|:--------|:------------|
| **POWER_SUPPLY_1** | 240VAC / 1.3A | 24VDC | PLC rated | PLC and I/O modules |
| **POWER_SUPPLY_2** | 240VAC / 8.5A | 24VDC | Motors rated | Motor drivers |
| **DC/DC CONVERTER** | 24VDC | 12VDC | TBD | Solenoids/Accessories |

### Main Power Input

| Terminal | Phase | Protection | Notes |
|:---------|:------|:-----------|:------|
| **L1** | Line (Hot) | 4 Amp breaker (CB) | Brown wire |
| **N1** | Neutral | Common | Blue wire |
| **PE1** | Protective Earth | Ground | Green/Yellow wire |

### Distribution Circuit Details

#### PLC Power Circuit
- **Input**: 240VAC from mains (L1, N1)
- **Protection**: Slow-blow fuse RL1 (1A)
- **Output**: 24VDC via terminals 2V/1, 0V/1
- **I/O Modules**: Connected to PLC backplane
  - ES-LINK
  - RELAY
  - DC INPUT (4X)
  - 24VDC Sink

#### Motor Power Circuit
- **Input**: 240VAC from mains (L1, N1)
- **Protection**: Slow-blow fuse RL2 (5A)
- **Output**: 24VDC via terminals 2V/3, 0V/3
- **Load**: Motor drivers (TB3 = Motor Power Terminals)

#### DC/DC Converter Circuit
- **Input**: 24VDC
- **Output**: 12VDC
- **Protection**: Terminals 12V/1, 0V/1
- **Load**: Solenoid flipper and accessories (TB3)

### Terminal Block Assignments

| Terminal Block | Voltage | Usage |
|:--------------|:--------|:------|
| **TB3** | +24V / 0V | Motor Power Terminals |
| **TB3** | +12V / 0V | Solenoids Flipper |

---

## Wiring Color Code

Following standard electrical wiring conventions:

| Wire Color | Function | Usage |
|:-----------|:---------|:------|
| **Brown (L)** | Live/Hot | 240VAC supply |
| **Blue (N)** | Neutral | 240VAC return |
| **Green/Yellow (PE)** | Protective Earth | Safety ground |
| **Red** | Positive DC | +24V / +12V power |
| **Black** | Negative DC | 0V / Ground |
| **White/Gray** | Signal | Control signals |
| **Orange/Yellow** | Step/Dir | Motor control signals |

---

## Safety Features

### Electrical Protection

| Protection Type | Component | Rating | Purpose |
|:----------------|:----------|:-------|:--------|
| Main Circuit Breaker | CB | 4A | Overcurrent protection |
| PLC Supply Fuse | RL1 | 1A slow-blow | PLC circuit protection |
| Motor Supply Fuse | RL2 | 5A slow-blow | Motor circuit protection |
| Emergency Stop | ESTOP | NC contact | Immediate motor shutdown |
| Ground Connection | PE | All metal parts | Electrical safety |

### Operational Safety
- ⚠️ All motor enable signals routed through emergency stop circuit
- ⚠️ Fuses protect against short circuits and overload
- ⚠️ Separate power supplies prevent PLC reset during motor surge
- ⚠️ Pressure switch monitors pneumatic system for leaks/failures
- ⚠️ Compressor protection prevents pneumatic system damage

---

## System Startup Sequence

1. **Pre-Power Checks**
   - Verify all wiring connections
   - Check emergency stop is released
   - Ensure pneumatic lines are connected
   - Verify air pressure is adequate (6 bar nominal)

2. **Power-Up Sequence**
   - Close main circuit breaker (CB)
   - PLC power supply energizes (POWER_SUPPLY_1)
   - Motor power supply energizes (POWER_SUPPLY_2)
   - Verify LED indicators on power supplies
   - Check PLC status lights

3. **System Initialization**
   - PLC runs initialization routine
   - Motor drivers receive enable signals
   - Pneumatic system pressurizes
   - Perform homing sequence for all axes

4. **Ready State**
   - All motors enabled and holding
   - Pneumatic pressure within operating range
   - System ready for operation commands

---

## Maintenance & Troubleshooting

### Regular Maintenance

| Interval | Task | Notes |
|:---------|:-----|:------|
| **Weekly** | Check terminal tightness | Vibration can loosen connections |
| **Monthly** | Inspect wire insulation | Look for wear or damage |
| **Quarterly** | Test emergency stop | Verify all motors disable |
| **Annually** | Replace fuses | Preventive replacement |

### Common Issues

| Symptom | Possible Cause | Solution |
|:--------|:--------------|:---------|
| Motors not responding | ESTOP engaged | Release emergency stop |
| Single motor failure | Loose motor connections | Check motor wiring at driver |
| PLC not powering | RL1 fuse blown | Check for short circuit, replace fuse |
| Motor power loss | RL2 fuse blown | Check motor current draw |
| Pneumatics not working | Low air pressure | Check compressor and pressure switch |
| Intermittent operation | Loose terminal connections | Tighten all terminal blocks |

---

## Technical Specifications Summary

### Power Requirements
- **Input Voltage**: 240VAC, 50/60Hz
- **Total Power Consumption**: ~2.5kW (approx.)
- **PLC Supply**: 24VDC, 1.3A
- **Motor Supply**: 24VDC, 8.5A
- **Auxiliary Supply**: 12VDC via DC/DC converter

### Control Signals
- **Logic Level**: 5VDC (TTL compatible)
- **Motor Signals**: STEP/DIR differential or single-ended
- **Pneumatic Signals**: 24VDC solenoid control

### Environmental
- **Operating Temperature**: 0°C to 40°C
- **Storage Temperature**: -20°C to 60°C
- **Humidity**: 20% to 80% RH (non-condensing)

---

## Compliance & Standards

This electrical system should comply with:
- IEC 60204-1 (Safety of machinery - Electrical equipment)
- IEC 61000-6-2 (EMC immunity for industrial environments)
- Local electrical codes and regulations

---

## Revision History

| Version | Date | Changes | Author |
|:--------|:-----|:--------|:-------|
| 1.0 | TBD | Initial release | [Your Name] |

---

## Related Documentation

- [Hardware Overview](hardware-overview.md) - Mechanical assembly and components
- [Software Setup](software-setup.md) - PLC programming and configuration
- [Maintenance Guide](maintenance-guide.md) - Scheduled maintenance procedures

---

## License

[Specify your license - e.g., MIT, GPL, CC-BY-SA, etc.]

---

## Contact & Support

For electrical system questions or issues:
- GitHub Issues: [Link to issues page]
- Email: [Your contact]
- **⚠️ WARNING**: Only qualified electricians should modify this system

---

*Last Updated: [Current Date]*
