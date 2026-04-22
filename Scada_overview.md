# SCADA Overview

## System Description

The Supervisory Control And Data Acquisition (SCADA) system integrates industrial control hardware with modern software infrastructure to enable real-time monitoring and control of automated processes. This implementation consists of two major hubs working in coordination to provide comprehensive process control and visualization.

## Architecture Components

### 1. Click PLC CPU (192.168.1.10)

The Click PLC serves as the primary control unit, executing pre-programmed logic for industrial automation tasks.

**Key Functions:**
- **Input Processing**: Receives digital signals from connected input devices
- **Logic Execution**: Processes control logic based on programmed variables and data sets
- **Output Control**: Sends commands to output devices based on process logic
- **Process Logging**: Maintains operational logs for monitoring and troubleshooting

**Communication Protocol:**
- **Modbus TCP**: Enables network-based communication for reading and writing coils and registers
- **Connection**: RJ45 Ethernet cable for reliable industrial networking

### 2. Node-RED Data Hub (Laptop - 192.168.1.20)

Node-RED operates as a centralized data integration platform, bridging multiple protocols and providing visualization capabilities.

**Deployment Environment:**
- Runs within a Docker container for portability and isolation
- Containerized deployment ensures consistent runtime environment

**Core Services:**

#### a) Node_RED (Port 1880)
- **Function**: Primary data hub that merges data across different protocols
- **Protocol Integration**: Communicates with PLC via MQTT
- **Data Flow**: Receives process data and distributes to various endpoints

#### b) MQTT_Broker (Port 1883)
- **Function**: Message broker facilitating publish/subscribe communication
- **Architecture**: Enables bidirectional data exchange between Node-RED and PLC
- **Advantages**: Lightweight protocol ideal for IoT and industrial applications

#### c) HMI_Dashboard (Port 1880/ui)
- **Function**: Web-based Human-Machine Interface
- **Access**: HTTP dashboard accessible from any network browser
- **Purpose**: Provides real-time visualization and control interface for operators

#### d) VisionSystem.py (OpenCV)
- **Function**: Computer vision processing for quality control or object detection
- **Input**: USB Camera connected via USB cable
- **Integration**: Publishes vision data to MQTT broker for system-wide access
- **Technology**: Python-based OpenCV for image processing capabilities

## Communication Flow

### PLC to Node-RED Communication
1. PLC processes input signals and executes control logic
2. Modbus TCP registers and coils are exposed on the network
3. Node-RED reads/writes PLC data via Modbus TCP over RJ45 connection
4. Data is published to MQTT broker for distribution

### Node-RED Internal Data Flow
1. Node_RED service receives data from PLC via MQTT
2. MQTT_Broker manages message routing between services
3. HMI_Dashboard subscribes to relevant data topics for visualization
4. VisionSystem.py publishes image analysis results to MQTT broker

### Operator Interface
1. HTTP-based dashboard accessible at 192.168.1.20:1880/ui
2. HMI component connects to external HMI display devices
3. Real-time monitoring of process variables and system status
4. Control inputs sent back through MQTT to PLC

## Network Configuration

| Device/Service | IP Address | Port | Protocol |
|----------------|------------|------|----------|
| Click PLC | 192.168.1.10 | 502 | Modbus TCP |
| Node-RED | 192.168.1.20 | 1880 | HTTP |
| MQTT Broker | 192.168.1.20 | 1883 | MQTT |
| HMI Dashboard | 192.168.1.20 | 1880/ui | HTTP |

## Key Features

### Real-Time Monitoring
- Continuous data acquisition from PLC
- Live visualization through web-based HMI
- Computer vision integration for visual inspection

### Protocol Integration
- **Modbus TCP**: Industrial standard for PLC communication
- **MQTT**: Lightweight messaging for distributed data exchange
- **HTTP**: Web-based dashboard access for operators

### Modular Architecture
- Dockerized deployment for easy maintenance and updates
- Separation of concerns between control logic (PLC) and data integration (Node-RED)
- Scalable design allowing addition of new sensors or services

### Vision System Integration
- USB camera for image capture
- OpenCV processing for intelligent analysis
- MQTT integration for seamless data sharing with other system components

## System Benefits

1. **Centralized Control**: Single platform for monitoring multiple data sources
2. **Protocol Flexibility**: MQTT broker enables easy integration of additional devices
3. **Remote Access**: Web-based HMI accessible from any network-connected device
4. **Containerization**: Docker ensures consistent deployment across environments
5. **Visual Monitoring**: Computer vision adds intelligent inspection capabilities
6. **Data Logging**: Process history available for analysis and optimization

## Technology Stack

- **PLC**: Click PLC CPU
- **Communication**: Modbus TCP, MQTT
- **Integration Platform**: Node-RED
- **Containerization**: Docker
- **Message Broker**: MQTT Broker (Mosquitto)
- **Vision Processing**: Python + OpenCV
- **Visualization**: Node-RED Dashboard
- **Networking**: Ethernet (RJ45)

---

*This SCADA system demonstrates modern industrial automation practices by combining traditional PLC control with contemporary IoT technologies for comprehensive process monitoring and control.*