# SCADA Overview

##1. System Description
The Supervisory Control and Data Acquisition (SCADA) system enables centralized monitoring and control by integrating communication between key system components. It facilitates real-time data exchange, process control, and visualization through the use of multiple industrial communication protocols.

## 2. Main Architecture

###Click PLC CPU (192.168.1.10)
The CLICK PLC functions as the primary control unit, executing pre-defined logic to manage the process. It continuously monitors and updates internal variables (memory/registers), which represent system states such as inputs, outputs, and process values.
These variables can be accessed by external systems via communication protocols (e.g., Modbus TCP), allowing remote monitoring and control without interfering with the PLC’s core logic.
###Node-RED Data Hub (Laptop - 192.168.1.20)
Node-RED serves as the central data integration and communication hub. It bridges multiple protocols and devices, enabling seamless data flow between the PLC, MQTT broker, and other system components.

##Communication Protocol:**
- **Modbus TCP**: Enables network-based communication for reading and writing coils and registers by external device.
- **Connection**: RJ45 Ethernet cable

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