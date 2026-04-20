# Automated Pick-and-Place Card Sorting System

![System Status](https://img.shields.io/badge/status-completed-success)
![License](https://img.shields.io/badge/license-MIT-blue)

An automated playing card sorting system that uses machine vision, PLC control, and a 3-axis gantry to classify and distribute cards by rank or suit. Developed as a mechatronics engineering project at Seneca College.

![Gantry System](docs/images/gantry-view.jpg)

## 🎯 Project Overview

This project demonstrates a fully integrated mechatronic solution combining:
- **Machine Vision**: Python/OpenCV pipeline for card identification
- **Industrial Automation**: CLICK PLUS PLC for real-time control
- **Multi-axis Motion**: 400×400×60mm Cartesian gantry with stepper motors
- **Pneumatic System**: Vacuum-based end-effector with pressure regulation
- **IoT Dashboard**: Node-RED interface for monitoring and control

### Key Performance Metrics
- **Cycle Time**: 14-20 seconds per card
- **Throughput**: ~4.5 cards per minute
- **Classification Accuracy**: 98%
- **Pickup Reliability**: ~100% (under normal conditions)

## 🏗️ System Architecture

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   Python    │◄────────┤  Node-RED   │────────►│  CLICK PLC  │
│   OpenCV    │  MQTT   │  Dashboard  │  Modbus │   Control   │
│   Vision    │         │   Bridge    │   TCP   │             │
└─────────────┘         └─────────────┘         └──────┬──────┘
                                                        │
                                    ┌───────────────────┼───────────────────┐
                                    ▼                   ▼                   ▼
                            ┌───────────┐       ┌───────────┐       ┌───────────┐
                            │  Stepper  │       │  Vacuum   │       │  Sensors  │
                            │  Motors   │       │  Solenoid │       │  Network  │
                            │  (X,Y,Z)  │       │           │       │           │
                            └───────────┘       └───────────┘       └───────────┘
```

## 🔧 Hardware Components

### Motion System
- **Gantry**: 3-axis Cartesian with GT2 timing belt (X/Y) and lead screw (Z)
- **Motors**: NEMA 17/23 stepper motors with 32-step microstepping
- **Resolution**: 160 steps/mm (X/Y), 3200 steps/mm (Z)
- **Speed**: ~400 mm/s with smooth acceleration profiles

### Pneumatic System
- **Vacuum Generator**: Automatic pressure regulation
- **Reservoir**: 15 oz capacity, maintains -20 to -40 kPa
- **Runtime**: ~6 minutes without motor operation
- **End-Effector**: Vacuum gripper with spring-loaded compliance

### Sensors
- **Limit Switches**: Home position and overtravel protection
- **Photoelectric Sensor**: Z-axis proximity and pickup verification
- **Pressure Switch**: Vacuum seal verification
- **IR Detection**: Card presence detection

### Control Hardware
- **PLC**: CLICK PLUS with 44 I/O points
- **Network**: Modbus TCP over Ethernet
- **Safety**: Emergency stop with motor disable

## 💻 Software Stack

### Vision System (Python)
```
opencv-python     # Image processing and card classification
paho-mqtt        # MQTT communication with Node-RED
numpy            # Array operations
```

**Features**:
- Real-time card rank and suit detection
- Orientation detection with automatic flip request
- Confidence scoring and error handling
- Persistent logging of all classifications

### Control System (PLC)
- **Language**: SimTalk (proprietary ladder logic)
- **Communication**: Modbus TCP server
- **Motion Control**: Pulse-based stepper control with acceleration profiles
- **Safety Logic**: E-stop, limit switches, timeout protection

### IoT Interface (Node-RED)
- **Dashboard**: Real-time position monitoring, classification results
- **MQTT Bridge**: Vision system ↔ PLC communication
- **Operator Controls**: Manual jogging, preset positions, sorting modes

## 📁 Repository Structure

```
automated-card-sorter/
├── README.md
├── LICENSE
├── docs/
│   ├── technical-report.pdf      # Full technical documentation
│   ├── user-manual.md            # Operating procedures
│   ├── maintenance.md            # Maintenance guidelines
│   └── images/                   # System photos and diagrams
├── hardware/
│   ├── mechanical/
│   │   ├── nx-models/            # Siemens NX CAD files
│   │   └── assembly-drawings/
│   ├── electrical/
│   │   ├── eplan-diagrams/       # Electrical schematics
│   │   ├── pcb-designs/          # PCB layouts
│   │   └── wiring-guide.md
│   └── bom.xlsx                  # Bill of materials with datasheets
├── software/
│   ├── vision/
│   │   ├── card_classifier.py    # OpenCV vision system
│   │   ├── templates/            # Card rank/suit templates
│   │   └── config.yaml
│   ├── plc/
│   │   ├── click-program/        # PLC ladder logic
│   │   └── modbus-mapping.md
│   └── node-red/
│       ├── flows.json            # Node-RED flows
│       └── dashboard-config.json
└── tests/
    ├── calibration/
    └── validation/
```

## 🚀 Getting Started

### Prerequisites
- Docker (for Node-RED containerized services)
- Python 3.8+
- CLICK Programming Software (for PLC)
- Direct Ethernet connection to PLC

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/automated-card-sorter.git
cd automated-card-sorter
```

2. **Set up Python environment**
```bash
cd software/vision
pip install -r requirements.txt
```

3. **Start Node-RED**
```bash
docker-compose up -d
```

4. **Access the dashboard**
```
http://localhost:1880/ui
```

### System Startup Procedure

1. **Power up the system**
   - Switch ON main breaker
   - Verify control hardware indicators

2. **Establish connectivity**
   - Connect laptop to PLC via Ethernet
   - Start Docker containers
   - Launch Python vision script

3. **Verify readiness**
   - Check Node-RED dashboard displays live data
   - Confirm camera feed is visible
   - Verify motor enable status

4. **Home the system**
   - Ensure E-stop is released
   - Clear gantry travel area
   - Execute "Home All" sequence

5. **Begin operation**
   - Select sorting mode (rank or suit)
   - Specify feed bin location
   - Press Start

## 📊 Performance Analysis

### Motion Characteristics
- **X/Y Axes**: Belt-driven, 160 steps/mm, 400mm/s max speed
- **Z Axis**: Lead screw, 3200 steps/mm, controlled descent with photoelectric slowdown
- **Positioning Accuracy**: Sub-millimeter repeatability

### Vision Processing
- **Classification Method**: OpenCV template matching
- **Processing Time**: <1 second per card
- **Error Handling**: Automatic flip request for low confidence or inverted cards
- **Special Value**: Index 999 triggers vision request, 77 signals flip needed

### Sorting Logic
- **Bin Indices 0-21**: Physical sorting bins (6×4 grid)
- **Index 22**: Flipper drop-off point
- **Index 23**: Dead zone (flipper motor)
- **Index 24**: Flipper pickup point

## 🔬 Technical Challenges & Solutions

### Challenge: Gantry Precision
**Problem**: Misalignment causing binding and uneven motion  
**Solution**: Iterative measurement and adjustment during assembly

### Challenge: Vision Cable Interference
**Problem**: Cable disconnection from solenoid/pump interference  
**Solution**: Added shielding and careful cable routing

### Challenge: Photoelectric Sensor Chatter
**Problem**: Rapid switching causing Z-axis velocity errors  
**Solution**: Signal filtering and controlled slowdown logic

### Challenge: Cable Management
**Problem**: Cables snagging during 3-axis motion  
**Solution**: Drag chains, stress-relief routing, secured connectors

## 🔮 Future Improvements

### 1. Localized Vacuum Control
- Separate vacuum generators or flow regulators per operation
- Prevents double-feeding without mechanical wedge
- More precise pressure matching for different tasks

### 2. ZIPLink PLC Connections
- Pre-wired terminal modules for CLICK I/O
- Reduces wiring errors and installation time
- Cleaner cable management (estimated cost: $290 CAD vs $40 current)

### 3. Automated Suction Cup Cleaning
- Brush/wiper mechanism within gantry reach
- Periodic self-cleaning after N cycles or pressure drop
- Maintains pickup reliability autonomously

## 📚 Documentation

- [Technical Report](docs/technical-report.pdf) - Complete system design documentation
- [User Manual](docs/user-manual.md) - Operating procedures and safety
- [Maintenance Guide](docs/maintenance.md) - Preventive maintenance schedules
- [System Block Diagram](docs/images/system-block-diagram.png)

## 🤝 Contributors

**Josh Craven** - jcraven@myseneca.ca  
**Jae Park** - jpark83@myseneca.ca

**Instructor**: Iakov Romanovski  
**Course**: TPJ653NAA - Mechatronics Engineering  
**Institution**: Seneca College  
**Date**: March 2026

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Seneca College Mechatronics Engineering Program
- AutomationDirect for CLICK PLC documentation
- OpenCV community for computer vision resources

## 📧 Contact

For questions, improvements, or collaboration:
- Joshua Craven: jcraven@myseneca.ca | 647-248-7322
- Jay Park: jpark83@myseneca.ca | 647-500-4630

---

**Note**: This repository represents academic coursework completed in March 2026. The system demonstrates industrial automation principles and is designed for educational purposes.
