# Software Directory Structure

This document outlines the organization of all software components for the Automated Card Sorting System.

## Directory Tree

```
software/
├── vision/
│   ├── card_classifier.py          # Main vision processing script
│   ├── requirements.txt            # Python dependencies
│   ├── config.yaml                 # Configuration parameters
│   ├── templates/                  # Card recognition templates
│   │   ├── ranks/                  # Rank templates (A, 2-10, J, Q, K)
│   │   └── suits/                  # Suit templates (♠, ♥, ♦, ♣)
│   ├── logs/                       # Classification logs
│   └── README.md                   # Vision system documentation
│
├── plc/
│   ├── click-program/
│   │   ├── main.txt                # Main PLC ladder logic
│   │   ├── motion-control.txt      # Stepper motor control routines
│   │   ├── vacuum-control.txt      # Pneumatic control logic
│   │   └── safety-interlocks.txt   # E-stop and limit switch logic
│   ├── modbus-mapping.md           # Modbus register documentation
│   ├── io-assignment.md            # I/O point assignments
│   └── README.md                   # PLC programming guide
│
├── node-red/
│   ├── flows.json                  # Complete Node-RED flows
│   ├── dashboard-config.json       # Dashboard layout configuration
│   ├── mqtt-config.json            # MQTT broker settings
│   ├── README.md                   # Node-RED setup guide
│   └── custom-nodes/               # Custom Node-RED nodes (if any)
│
└── docker/
    ├── docker-compose.yml          # Multi-container setup
    ├── Dockerfile.nodered          # Node-RED container
    ├── Dockerfile.mqtt             # MQTT broker container
    └── README.md                   # Docker deployment guide
```

## Component Details

### Vision System (`software/vision/`)

**card_classifier.py** - Main Script
```python
# Key Functions:
# - capture_frame()          # Grab image from USB camera
# - preprocess_image()       # Crop, rotate, enhance
# - extract_rank_roi()       # Region of interest for rank
# - extract_suit_roi()       # Region of interest for suit
# - template_match()         # OpenCV template matching
# - calculate_confidence()   # Classification confidence score
# - detect_orientation()     # Check if card is upside-down
# - publish_result()         # Send via MQTT to Node-RED
# - log_classification()     # Persistent storage to disk

# MQTT Topics:
# Subscribe: vision/request (receives index 999 from PLC)
# Publish: vision/result (sends rank, suit, confidence, flip flag)
```

**requirements.txt**
```txt
opencv-python==4.5.5
numpy==1.22.3
paho-mqtt==1.6.1
pyyaml==6.0
```

**config.yaml** - Configuration
```yaml
camera:
  index: 0                    # USB camera index
  width: 1920
  height: 1080
  fps: 30

mqtt:
  broker: "localhost"
  port: 1883
  topic_request: "vision/request"
  topic_result: "vision/result"

classification:
  confidence_threshold: 0.75  # Minimum confidence to accept
  flip_index: 77              # Special value requesting flip
  scan_request_index: 999     # Special value triggering scan

templates:
  ranks_dir: "templates/ranks/"
  suits_dir: "templates/suits/"
  
logging:
  enabled: true
  path: "logs/classifications.log"
  format: "%(asctime)s - %(levelname)s - %(message)s"
```

### PLC Programs (`software/plc/`)

**Modbus Register Map** (`modbus-mapping.md`)
```markdown
# Holding Registers (Read/Write)

| Address | Name              | Type    | Description                    |
|---------|-------------------|---------|--------------------------------|
| 40001   | BIN_INDEX         | INT16   | Target bin for current card    |
| 40002   | X_POSITION        | INT16   | Current X position (mm)        |
| 40003   | Y_POSITION        | INT16   | Current Y position (mm)        |
| 40004   | Z_POSITION        | INT16   | Current Z position (mm)        |
| 40005   | MOTOR_ENABLE      | BOOL    | Motor enable state             |
| 40006   | PROGRAM_RUN       | BOOL    | Auto program running           |
| 40007   | VISION_REQUEST    | INT16   | Request classification (999)   |
| 40008   | FLIP_REQUEST      | BOOL    | Card flip needed (Index 77)    |

# Input Registers (Read Only)

| Address | Name              | Type    | Description                    |
|---------|-------------------|---------|--------------------------------|
| 30001   | X_LIMIT_HOME      | BOOL    | X-axis home limit switch       |
| 30002   | Y_LIMIT_HOME      | BOOL    | Y-axis home limit switch       |
| 30003   | Z_LIMIT_TOP       | BOOL    | Z-axis upper limit             |
| 30004   | ESTOP_STATUS      | BOOL    | Emergency stop state           |
| 30005   | VACUUM_PRESSURE   | BOOL    | Pressure switch state          |
| 30006   | PHOTOELECTRIC     | BOOL    | Card detection sensor          |
| 30007   | HOMING_COMPLETE   | BOOL    | Homing sequence done           |
```

**I/O Assignment** (`io-assignment.md`)
```markdown
# Digital Inputs

| Terminal | Device                  | Signal     | PLC Address |
|----------|-------------------------|------------|-------------|
| C0-01    | X-Axis Limit (Home)     | X_LIM_HOME | %I0.0       |
| C0-02    | Y-Axis Limit (Home)     | Y_LIM_HOME | %I0.1       |
| C0-03    | Z-Axis Limit (Top)      | Z_LIM_TOP  | %I0.2       |
| C0-04    | Emergency Stop          | ESTOP      | %I0.3       |
| C0-05    | Vacuum Pressure Switch  | VAC_PRESS  | %I0.4       |
| C0-06    | Photoelectric Sensor    | PHOTO_SENS | %I0.5       |

# Digital Outputs

| Terminal | Device                  | Signal     | PLC Address |
|----------|-------------------------|------------|-------------|
| C0-07    | X-Axis Step             | X_STEP     | %Q0.0       |
| C0-08    | X-Axis Direction        | X_DIR      | %Q0.1       |
| C0-09    | Y-Axis Step             | Y_STEP     | %Q0.2       |
| C0-10    | Y-Axis Direction        | Y_DIR      | %Q0.3       |
| C0-11    | Z-Axis Step             | Z_STEP     | %Q0.4       |
| C0-12    | Z-Axis Direction        | Z_DIR      | %Q0.5       |
| C0-13    | Motor Enable            | MOT_EN     | %Q0.6       |
| C0-14    | Vacuum Solenoid         | VAC_SOL    | %Q0.7       |
```

### Node-RED (`software/node-red/`)

**Flow Description**
```
Flow 1: Modbus Communication
├─ Modbus Read (poll every 100ms)
│  ├─ X/Y/Z Positions
│  ├─ Motor Enable State
│  └─ Vision Request Flag
├─ Modbus Write
│  ├─ Bin Index (from MQTT)
│  └─ Control Commands (from Dashboard)

Flow 2: MQTT Bridge
├─ Subscribe: vision/result
│  └─ Parse JSON classification
├─ Publish: vision/request
│  └─ Triggered by PLC index 999

Flow 3: Dashboard Interface
├─ Gauges: X, Y, Z Position
├─ Charts: Position over time
├─ Buttons: Home, Jog, Start/Stop
├─ Status: Classification results, confidence
└─ Controls: Sorting mode selection

Flow 4: Data Processing
├─ Bin Index Calculation
│  ├─ Rank Mode: Map A-K to bins 0-12
│  └─ Suit Mode: Map ♠♥♦♣ to bins 0-3
├─ Flip Detection (Index 77)
└─ Error Logging
```

## Setup Instructions

### 1. Vision System Setup

```bash
cd software/vision

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure settings
cp config.yaml.template config.yaml
# Edit config.yaml with your settings

# Run vision system
python card_classifier.py
```

### 2. Node-RED Setup

```bash
cd software/docker

# Start Node-RED and MQTT broker
docker-compose up -d

# Access Node-RED editor
# Browser: http://localhost:1880

# Import flows
# Copy contents of flows.json
# Node-RED Menu > Import > Clipboard

# Deploy flows
# Click "Deploy" button in top-right

# Access dashboard
# Browser: http://localhost:1880/ui
```

### 3. PLC Programming

```
1. Install CLICK Programming Software from AutomationDirect
2. Open project: software/plc/click-program/
3. Connect to PLC via Ethernet (default IP: 192.168.0.1)
4. Upload program to PLC
5. Verify Modbus TCP is enabled on Port 502
6. Test communication with Node-RED
```

## Integration Testing

### Test 1: Vision → Node-RED → PLC Loop

```bash
# Terminal 1: Start MQTT broker
docker-compose up mosquitto

# Terminal 2: Start Node-RED
docker-compose up nodered

# Terminal 3: Start vision system
cd software/vision
python card_classifier.py

# PLC: Set register 40007 = 999 (vision request)
# Expected: Vision classifies, returns result via MQTT
# Node-RED: Receives result, writes bin index to PLC register 40001
```

### Test 2: Dashboard Control

```
1. Open dashboard: http://localhost:1880/ui
2. Enable motors
3. Click "Home All"
4. Verify position updates on gauges
5. Jog X-axis +10mm
6. Confirm position reads +10mm
```

### Test 3: Full Sorting Cycle

```
1. Load card in feed bin
2. Select "Rank Sorting" mode
3. Specify feed bin location
4. Click "Start Program"
5. Verify:
   - Gantry picks card
   - Vision classifies correctly
   - Card placed in correct bin
   - Cycle repeats
```

## Troubleshooting

### Vision System Not Responding

```bash
# Check MQTT connection
mosquitto_sub -h localhost -t vision/#

# Verify camera
python -c "import cv2; print(cv2.VideoCapture(0).read())"

# Check logs
tail -f software/vision/logs/classifications.log
```

### Node-RED Communication Errors

```bash
# Check Modbus connection
docker-compose logs nodered | grep -i modbus

# Verify PLC IP address
ping 192.168.0.1

# Test MQTT broker
mosquitto_pub -h localhost -t test -m "hello"
```

### PLC Program Issues

```
1. Verify PLC is in Run mode (not Program mode)
2. Check Modbus TCP is enabled
3. Confirm network cable connected
4. Review ladder logic for faults
5. Check I/O point wiring
```

## Performance Optimization

### Vision Processing Speed
- Reduce image resolution for faster processing
- Optimize template sizes
- Use GPU acceleration if available
- Pre-cache templates on startup

### Motion Control Smoothness
- Tune acceleration/deceleration ramps
- Adjust step pulse frequency
- Optimize path planning
- Reduce mechanical backlash

### Network Latency
- Use wired Ethernet (not WiFi)
- Reduce Modbus polling frequency if needed
- Minimize MQTT message size
- Use persistent MQTT connections

---

**Document Version**: 1.0  
**Last Updated**: March 2026
