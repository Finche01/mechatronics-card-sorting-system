# Hardware Documentation

This directory contains all hardware design files, schematics, and documentation for the Automated Card Sorting System.

## Directory Structure

```
hardware/
├── mechanical/
│   ├── nx-models/              # Siemens NX CAD files
│   ├── assembly-drawings/      # PDF assembly drawings
│   ├── part-drawings/          # Individual component drawings
│   └── README.md               # Mechanical design documentation
│
├── electrical/
│   ├── eplan-diagrams/         # EPLAN electrical schematics
│   ├── pcb-designs/            # PCB layouts (if applicable)
│   ├── wiring-diagrams/        # Wiring guides and terminal assignments
│   └── README.md               # Electrical design documentation
│
├── pneumatic/
│   ├── circuit-diagram.pdf     # Pneumatic system schematic
│   └── README.md               # Pneumatic system documentation
│
└── bom.xlsx                    # Master Bill of Materials with datasheets
```

## Mechanical System

### Gantry Assembly

**Frame**: Aluminum extrusion (40x40mm profiles)  
**Working Envelope**: 400mm × 400mm × 60mm  
**Axes**: X, Y, Z Cartesian configuration

### Motion Components

| Axis | Drive Type | Resolution | Speed |
|------|------------|------------|-------|
| X    | GT2 Belt (2mm pitch, 20T pulley) | 160 steps/mm | 400 mm/s |
| Y    | GT2 Belt (2mm pitch, 20T pulley) | 160 steps/mm | 400 mm/s |
| Z    | Lead Screw (2mm pitch) | 3200 steps/mm | Variable |

### Linear Motion

- **Rails**: MGN12 linear rails
- **Bearings**: LM8UU linear bearings
- **Pulleys**: GT2 20-tooth aluminum
- **Belts**: GT2 6mm width, timing belt

### End-Effector

**Type**: Vacuum gripper with spring compliance  
**Vacuum Tube**: Brass, integrated into tool  
**Guide Rods**: 8mm diameter, prevents rotation  
**Spring**: Compression spring for vertical compliance

## Electrical System

### Power Distribution

- **Main Power**: 24VDC industrial power supply
- **Motor Power**: Shared 24VDC bus for all steppers
- **Control Power**: 24VDC for PLC and I/O
- **Total Current**: ~10A peak demand

### Control Hardware

**PLC**: CLICK PLUS series  
- Model: C0-02DD1-D (example - verify actual model)
- I/O Modules: 44 total points
- Communication: Modbus TCP over Ethernet

**Motor Drivers**: Stepper motor drivers with microstepping  
- Microstepping: 32 steps per full step
- Current Setting: Configured per motor rating

### Sensors

| Sensor Type | Quantity | Purpose | Model/Spec |
|-------------|----------|---------|------------|
| Limit Switch | 3+ | Homing and overtravel | V-156-1C25 (or equivalent) |
| Photoelectric | 1 | Z-axis proximity detection | Diffuse reflective |
| Pressure Switch | 1 | Vacuum verification | -15 kPa setpoint |
| IR Sensor | 1 | Card presence detection | Through-beam or reflective |

### Wiring Standards

- **Power Wiring**: Red (+24V), Black (0V)
- **Signal Wiring**: Shielded twisted pair where applicable
- **Motor Wiring**: 4-conductor for stepper motors
- **Cable Management**: Drag chains on all moving axes

## Pneumatic System

### Components

1. **Vacuum Pump**: Oil-less continuous duty
   - Flow Rate: 0.4-1.0 L/min
   - Max Vacuum: -60 kPa

2. **Reservoir**: 
   - Capacity: 15 oz (~450 ml)
   - Operating Range: -20 to -40 kPa
   - Runtime: ~6 minutes per charge

3. **Solenoid Valves**: 2× three-way valves
   - Voltage: 24VDC
   - Response Time: <50ms
   - Flow: Matched to system requirements

4. **Pressure Sensor**:
   - Type: Digital pressure switch
   - Range: 0 to -100 kPa
   - Output: Digital (NO/NC contact)

5. **Suction Cup**:
   - Diameter: 20mm
   - Material: Nitrile rubber
   - Bellows style for surface conformity

### Vacuum Circuit Operation

```
[Vacuum Pump] → [Check Valve] → [Reservoir] → [Solenoid Valve 1] → [Suction Cup]
                                              ↓
                                         [Solenoid Valve 2] → [Atmosphere]
```

- **Valve 1 Energized**: Vacuum applied to suction cup (pickup)
- **Valve 2 Energized**: Vent to atmosphere (release)
- **Both De-energized**: System sealed, reservoir maintains pressure

## Assembly Instructions

### Mechanical Assembly

1. **Frame Construction**
   - Assemble aluminum extrusion frame
   - Ensure squareness using machinist's square
   - Tighten all t-nuts and bolts

2. **Linear Rail Installation**
   - Mount rails parallel to frame edges
   - Check alignment with straightedge
   - Pre-load bearings per manufacturer specs

3. **Belt Tensioning**
   - Route belts through pulleys
   - Adjust tensioner until 1-2mm deflection at midspan
   - Verify no slipping during manual movement

4. **Z-Axis Assembly**
   - Install lead screw with anti-backlash nut
   - Mount end-effector with spring compliance
   - Verify smooth vertical travel

5. **End-Effector Integration**
   - Attach vacuum tube and suction cup
   - Mount camera and sensors
   - Route cables through drag chain

### Electrical Assembly

1. **PLC Mounting**
   - Install PLC on DIN rail in control panel
   - Connect Ethernet cable for programming
   - Apply 24VDC power

2. **I/O Wiring**
   - Follow terminal assignment diagram
   - Use color-coded wiring per standards
   - Label all connections clearly

3. **Motor Driver Setup**
   - Mount drivers with adequate cooling
   - Set current limits per motor specs
   - Wire step/direction signals from PLC

4. **Sensor Installation**
   - Mount limit switches at end of travel
   - Position photoelectric sensor on Z-axis
   - Install pressure switch in vacuum line

5. **Cable Management**
   - Install drag chains on X, Y axes
   - Secure cables at stress relief points
   - Test full range of motion for clearance

### Pneumatic Assembly

1. **Vacuum Pump Installation**
   - Mount pump on stable surface
   - Connect intake filter
   - Route discharge away from electronics

2. **Reservoir Connection**
   - Install check valve after pump
   - Connect reservoir with appropriate fittings
   - Mount pressure gauge for visual reference

3. **Solenoid Valve Wiring**
   - Wire valves to PLC outputs
   - Verify 24VDC polarity
   - Test actuation with manual control

4. **Tubing Installation**
   - Use 6mm OD polyurethane tubing
   - Minimize sharp bends
   - Secure all fittings, test for leaks

## CAD Files

### Siemens NX Models

**Location**: `hardware/mechanical/nx-models/`

The complete assembly is provided as Siemens NX files. Main assembly file: `FULL_ASSEMBLY.prt`

**Components**:
- Gantry frame
- X/Y/Z axis assemblies
- End-effector tool
- Bin array (6×4 grid)
- Mounting brackets
- Cable management

**How to Open**:
1. Install Siemens NX (version used: NX 12+)
2. Open `FULL_ASSEMBLY.prt`
3. All referenced parts should load automatically

**Export Options**:
- STEP files available in `assembly-drawings/`
- STL files for 3D printing custom parts

## Bill of Materials (BOM)

**Location**: `hardware/bom.xlsx`

The complete BOM includes:
- Part numbers and descriptions
- Quantities
- Supplier information
- Datasheets (linked)
- Cost estimates
- Lead times

**Major Component Categories**:
1. Structural (extrusions, brackets, fasteners)
2. Motion (rails, bearings, belts, pulleys, motors)
3. Electrical (PLC, drivers, sensors, cables)
4. Pneumatic (pump, valves, tubing, fittings)
5. Hardware (miscellaneous fasteners, connectors)

## Modifications and Customization

### Common Modifications

1. **Increase Working Envelope**:
   - Replace frame extrusions with longer sections
   - Extend belts and rails accordingly
   - Update PLC travel limits

2. **Add Fourth Axis**:
   - Implement rotary axis for card orientation
   - Additional motor driver required
   - Modify end-effector mounting

3. **Upgrade to Closed-Loop Motors**:
   - Replace stepper motors with servo motors
   - Update motor drivers
   - Modify PLC motion control logic

4. **Enhanced Vacuum System**:
   - Larger reservoir for longer runtime
   - Multiple suction cups for simultaneous pickup
   - Proportional vacuum control

## Troubleshooting

### Mechanical Issues

**Problem**: Gantry binding or uneven motion  
**Solution**: Check frame squareness, rail alignment, belt tension

**Problem**: Excessive vibration  
**Solution**: Tighten all bolts, check bearing pre-load, reduce acceleration

**Problem**: Z-axis dropping under gravity  
**Solution**: Verify lead screw is self-locking, check for worn bearings

### Electrical Issues

**Problem**: Motor not responding  
**Solution**: Check driver wiring, verify enable signal, inspect motor connections

**Problem**: Limit switch not triggering  
**Solution**: Verify wiring, test switch continuity, adjust mounting position

**Problem**: Sensor false triggers  
**Solution**: Check for electrical noise, add shielding, adjust sensitivity

### Pneumatic Issues

**Problem**: Weak vacuum  
**Solution**: Check for leaks, clean suction cup, verify pump operation

**Problem**: Slow pickup/release  
**Solution**: Check solenoid response time, verify valve wiring, reduce tubing length

## Safety Considerations

### Mechanical Hazards

- ⚠️ **Pinch Points**: Keep hands clear of belt drives and linear bearings
- ⚠️ **Moving Gantry**: Establish safety zones, use guarding if applicable
- ⚠️ **Sharp Edges**: Deburr all cut aluminum extrusions

### Electrical Hazards

- ⚠️ **Live Circuits**: 24VDC can cause sparks, disconnect power before servicing
- ⚠️ **Motor Current**: High current can damage components if miswired

### Operating Hazards

- ⚠️ **E-Stop Requirement**: Emergency stop must be accessible and functional
- ⚠️ **Limit Switches**: Never bypass safety interlocks

## Maintenance Schedule

See [maintenance.md](../docs/maintenance.md) for detailed maintenance procedures.

**Summary**:
- **Daily**: Visual inspection, suction cup cleaning
- **Weekly**: Belt tension check, sensor verification
- **Monthly**: Lubrication, electrical connection tightness
- **Quarterly**: Belt replacement evaluation, relay inspection

## Contact

**Hardware Design Team**:
- Joshua Craven: jcraven@myseneca.ca
- Jae Park: jpark83@myseneca.ca

**Faculty Advisor**:
- Iakov Romanovski

---

**Document Version**: 1.0  
**Last Updated**: March 2026
