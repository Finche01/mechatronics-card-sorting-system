# Hardware Overview

## 3-Axis Motion Platform

This document provides technical documentation for the 3-axis CNC/motion platform assembly.

---

## Assembly Views

### Assembled Configuration
![3-Axis Platform - Assembled View](docs/images/3-axis-assembled.png)

The complete assembly showing the XYZ gantry system with dual Y-axis motors and aluminum extrusion frame construction.

---

### Component Identification
![3-Axis Platform - Exploded View](docs/images/3-axis-exploded.png)

**Key Components:**
- **X-Axis**: Horizontal gantry carriage with stepper motor
- **Y-Axis (1)**: Left-side rail motor assembly
- **Y-Axis (2)**: Right-side rail motor assembly  
- **Z-Axis**: Vertical spindle/tool carriage
- **USB CAM**: Integrated camera module
- **Limit Switch**: End-stop position sensor
- **Photoelectric Sensor**: Workpiece detection/homing
- **Suction Cup**: Workpiece holding fixture

---

## Enclosure Configurations

### Folding Frame Assembly
![Enclosure - Folding Configuration](docs/images/assembly-fold.png)

Two-tier enclosure design with collapsible upper section for compact storage or transport. The folding mechanism allows the top frame to nest with the base.

### Vertical Frame Assembly
![Enclosure - Vertical Configuration](docs/images/assembly-vertical.png)

Standard vertical enclosure configuration providing full working envelope access while protecting the motion platform.

---

## Technical Specifications

### Motion System
| Axis | Travel (mm) | Motor Type | Drive System |
|------|-------------|------------|--------------|
| X    | TBD         | NEMA 17/23 | Belt/Lead Screw |
| Y    | TBD         | NEMA 17/23 (Dual) | Belt/Lead Screw |
| Z    | TBD         | NEMA 17/23 | Lead Screw |

### Frame Construction
- **Material**: Aluminum extrusion profiles (likely 2020 or 2040)
- **Base Dimensions**: TBD x TBD mm
- **Enclosed Height**: TBD mm
- **Working Area**: TBD x TBD x TBD mm

### Electronics
- Stepper motor drivers (type TBD)
- Controller board (type TBD)
- Limit switches for homing
- Photoelectric sensor for Z-axis probing
- USB camera for vision/alignment

---

## Bill of Materials (BOM)

A detailed BOM with part numbers, quantities, and sourcing information will be added here.

| Component | Quantity | Specification | Notes |
|-----------|----------|---------------|-------|
| Aluminum Extrusion | TBD | 2020/2040 profile | Frame structure |
| Stepper Motors | 4 | NEMA 17/23 | 3x axis + optional |
| Linear Rails | TBD | MGN12/15 | Smooth motion |
| Lead Screws | TBD | TR8x8 or similar | Z-axis drive |
| Timing Belts | TBD | GT2 6mm | X/Y drive |
| ... | ... | ... | ... |

---

## Assembly Instructions

### Prerequisites
- [ ] All components from BOM collected
- [ ] Required tools: Allen keys, wrenches, square
- [ ] Work surface prepared

### Build Steps
1. **Base Frame Assembly**
   - Assemble rectangular base from extrusions
   - Install Y-axis linear rails
   - Mount Y-axis stepper motors

2. **Gantry Assembly**
   - Build X-axis carriage
   - Install X-axis motor and belt system
   - Attach to Y-axis carriages

3. **Z-Axis Installation**
   - Mount Z-axis lead screw and motor
   - Install linear guides
   - Attach spindle/tool mount

4. **Electronics Integration**
   - Wire stepper motors
   - Install limit switches
   - Connect sensors and camera
   - Test homing sequence

5. **Enclosure Installation** (Optional)
   - Assemble vertical frame sections
   - Install panels (acrylic/polycarbonate)
   - Configure folding mechanism if applicable

---

## Software & Control

### Compatible Firmware
- GRBL
- Marlin
- Other (specify)

### Control Software
- UGS (Universal Gcode Sender)
- bCNC
- Lightburn (for laser applications)
- Custom control interface

---

## Applications

This platform can be configured for:
- CNC milling/engraving
- Laser cutting/engraving
- Pick-and-place automation
- 3D scanning
- PCB drilling
- Pen plotting

---

## Design Files

CAD files and technical drawings are available in the `/cad` directory:
- Assembly files (NX format)
- Individual component models
- 2D drawings with dimensions
- STEP/STL exports for compatibility

---

## Safety Considerations

⚠️ **Important Safety Notes:**
- Always use emergency stop functionality
- Ensure proper grounding of electrical components
- Keep hands clear of moving parts during operation
- Use appropriate eye protection when machine is running
- Verify limit switches are functioning before each use

---

## Maintenance

### Regular Maintenance Schedule
- **Daily**: Clean work surface, check for loose fasteners
- **Weekly**: Lubricate linear rails and lead screws
- **Monthly**: Check belt tension, verify limit switch function
- **Quarterly**: Deep clean, check electrical connections

---

## License

[Specify your license - e.g., MIT, GPL, CC-BY-SA, etc.]

---

## Credits & Acknowledgments

Design and assembly by [Your Name/Team]

Based on/inspired by: [Any reference designs]

---

## Contact & Support

For questions, issues, or contributions:
- GitHub Issues: [Link to issues page]
- Email: [Your contact]
- Community Forum: [If applicable]

---

*Last Updated: [Current Date]*
