# SCADA Overview

![SCADA](image/scada_diagram/Scada_diagram.png)

---

| Component                      | Role              | Protocols Used                              | Description |
|--------------------------------|-------------------|---------------------------------------------|-------------|
| **PLC CPU (192.168.1.10)**     | Control Unit      | Modbus TCP (Server)                         | Executes pre-defined logic to manage the process. Continuously monitors and updates internal variables (coils/registers). |
| **Node-RED (192.168.1.20)**    | Data Integration  | Modbus TCP (Client), MQTT (Vision System)   | Connects different protocols and devices, enabling data flow between the PLC, MQTT broker, and other system components. |

---
## Deployment Environment
![SCADA](image/scada_diagram/Docker_containers.png)
- Node-RED and the MQTT broker are deployed as containers using Docker Desktop.  
- Running them in containers simplifies network setup and provides isolation between services.  
- Containerized deployment is easy to manage, lightweight, and ensures a consistent runtime environment.
---
## Core Services

### a) MQTT Broker (Port 1883)
- Handles publish/subscribe messaging  
- Enables data exchange between Node-RED and other components (e.g., vision system)  

### b) VisionSystem.py (OpenCV)
- Captures images from a USB camera when triggered  
- Processes the image (grayscale, filtering, template matching)  
- Identifies the rank and suit from a predefined template set  
- Publishes the result to the MQTT broker  

---