# Hardware Setup Guide

[← Back to Main README](README.md)

---

## 📦 Bill of Materials (BOM)

### Mechanical Components

| Component | Specification | Quantity | Purpose |
|-----------|--------------|----------|---------|
| Linear Rails | 20x20mm, 1000mm | 3 | X, Y, Z axis movement |
| Stepper Motors | NEMA 23, 2.8A | 3 | Axis actuation |
| Lead Screws | 8mm diameter, 2mm pitch | 3 | Linear motion conversion |
| Linear Bearings | LM20UU | 12 | Smooth rail movement |
| Aluminum Extrusion | 2020 profile | 6m | Frame structure |
| Pneumatic Gripper | 2-jaw, 10mm stroke | 1 | Card pickup |
| Air Compressor | 6 bar, 50L tank | 1 | Pneumatic power |

### Electronics

| Component | Specification | Quantity | Purpose |
|-----------|--------------|----------|---------|
| PLC Controller | Siemens S7-1200/Allen-Bradley MicroLogix | 1 | System control |
| Stepper Drivers | TB6600, 4.5A | 3 | Motor control |
| Power Supply | 24V DC, 15A | 1 | System power |
| Camera | USB 3.0, 1080p, 60fps | 1 | Card imaging |
| LED Strip | White, 12V, 5050 SMD | 2m | Uniform lighting |
| Solenoid Valve | 5/2-way, 24V DC | 1 | Gripper control |
| Limit Switches | Mechanical, NO/NC | 6 | Homing sensors |
| Emergency Stop | Twist-release, NC | 1 | Safety |

### Wiring & Connectors

- Cat6 Ethernet cable (for PLC communication)
- 18 AWG power cables
- Pneumatic tubing (6mm OD)
- Quick-connect fittings
- Cable management clips

---

## 🔌 Wiring Diagrams

### Power Distribution

```
┌──────────────────┐
│  24V DC Supply   │
└────────┬─────────┘
         │
    ┌────┴────┬──────────┬──────────┬────────┐
    │         │          │          │        │
    ▼         ▼          ▼          ▼        ▼
  PLC    Driver 1   Driver 2   Driver 3   Solenoid
         (X-axis)   (Y-axis)   (Z-axis)    Valve
```

### Stepper Motor Connections

**Each motor driver (TB6600) to PLC:**

| Driver Pin | PLC Output | Function |
|------------|------------|----------|
| PUL+ | Q0.x | Step signal |
| PUL- | COM | Ground |
| DIR+ | Q0.y | Direction signal |
| DIR- | COM | Ground |
| ENA+ | Q0.z | Enable signal |
| ENA- | COM | Ground |

**Motor wiring (4-wire bipolar):**
- A+ / A- → Motor coil 1
- B+ / B- → Motor coil 2

### Sensor Connections

| Sensor | PLC Input | Type |
|--------|-----------|------|
| X-axis Home | I0.0 | Limit switch (NO) |
| Y-axis Home | I0.1 | Limit switch (NO) |
| Z-axis Home | I0.2 | Limit switch (NO) |
| E-Stop | I0.7 | Emergency stop (NC) |

---

## 🔧 Assembly Instructions

### Frame Assembly

1. **Base Frame**
   - Cut 2020 extrusion to lengths: 4x 1000mm, 4x 600mm
   - Assemble rectangular base using corner brackets
   - Ensure frame is square (measure diagonals)

2. **Vertical Posts**
   - Attach 4x 800mm vertical posts to corners
   - Use T-slot nuts and M5 bolts

3. **Top Frame**
   - Mirror base frame construction on top
   - Check vertical alignment with level

### X-Axis Gantry

1. Mount linear rails parallel on base frame
2. Attach motor to one end with mounting plate
3. Install lead screw with flexible coupler
4. Add linear bearings to carriage plate
5. Install limit switch at home position

### Y-Axis Gantry

1. Mount on X-axis carriage perpendicularly
2. Repeat motor and lead screw installation
3. Ensure smooth motion without binding

### Z-Axis Assembly

1. Vertical rail mounted on Y-axis carriage
2. Motor at top, lead screw extends down
3. Pneumatic gripper mounted on Z-carriage
4. Route air hose along Z-axis

### Camera Mount

1. Fixed position above sorting area
2. Angle: 90° to work surface
3. Height: 400-500mm for optimal FOV
4. Secure lighting on both sides

---

## ⚙️ Mechanical Calibration

### Steps per Millimeter Calculation

For 8mm lead screw, 2mm pitch, 200 steps/rev motor, 1/8 microstepping:

```
Steps per revolution = 200 × 8 = 1600 steps
Distance per revolution = 2mm
Steps per mm = 1600 / 2 = 800 steps/mm
```

### Homing Procedure

1. Power on system
2. PLC runs homing routine
3. Each axis moves to limit switch
4. Backs off 5mm
5. Slow approach to precise home position
6. Set position to zero

### Gripper Calibration

1. **Pressure**: Adjust regulator to 4-5 bar
2. **Grip Force**: Test with single card (should not slip)
3. **Release Height**: Z-axis at +50mm above card
4. **Pickup Height**: Z-axis at -2mm (slight compression)

---

## 🛡️ Safety Features

### Emergency Stop System

- NC (Normally Closed) circuit
- Cuts power to all motors instantly
- Must be reset manually
- PLC monitors E-stop state

### Soft Limits

Configured in PLC:
- X-axis: 0 to 950mm
- Y-axis: 0 to 550mm
- Z-axis: 0 to 150mm

Exceeding limits triggers immediate stop.

### Collision Detection

- Current sensing on motor drivers
- Unexpected resistance triggers stop
- Error logged to PLC memory

---

## 🔍 Testing & Validation

### Motion Tests

1. **Jog Test**: Manually move each axis
2. **Speed Test**: Run at operational speed (200mm/s)
3. **Accuracy Test**: Move to known positions, measure error
4. **Repeatability**: Return to same position 10x, measure variance

### Expected Performance

- Positioning accuracy: ±0.5mm
- Repeatability: ±0.1mm
- Maximum speed: 300mm/s
- Acceleration: 500mm/s²

---

## 🔧 Maintenance Schedule

### Daily
- Visual inspection for loose connections
- Check air pressure (should be 4-5 bar)
- Clean camera lens

### Weekly
- Lubricate linear rails and bearings
- Check belt/lead screw tension
- Verify limit switch operation

### Monthly
- Deep clean all mechanical components
- Inspect wiring for wear
- Calibrate home positions

### Annually
- Replace pneumatic seals
- Check motor bearing condition
- Full system recalibration

---

## 📞 Support

For hardware issues, please:
1. Check [Troubleshooting Guide](TROUBLESHOOTING.md)
2. Review wiring diagrams above
3. Open an issue with photos/videos

---

[← Back to Main README](README.md) | [Next: Software Installation →](INSTALLATION.md)
