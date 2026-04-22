# SCADA Overview

![SCADA](image/scada_diagram/Scada_diagram.png)

---

## 1. Click PLC CPU (192.168.1.10)
The CLICK PLC acts as the main control unit, executing pre-defined logic to manage the process. It continuously monitors and updates internal variables (memory/registers). These variables can be accessed by external systems through communication protocols such as Modbus TCP.
## 2. Node-RED Data Hub (Laptop – 192.168.1.20)
Node-RED functions as the central data hub. It connects different protocols and devices, allowing data to flow between the PLC, MQTT broker, and other components in the system.
---
## Communication Protocols
- **Modbus TCP**: Enables communication between the PLC and Node-RED over an RJ45 Ethernet connection.  
- **MQTT**: Enables publish/subscribe communication between the Python vision script and Node-RED.
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
![SCADA](image/scada_diagram/template_examples.png)
- Captures images from a USB camera when triggered  
- Processes the image (grayscale, filtering, template matching)  
- Identifies the rank and suit from a predefined template set  
- Publishes the result to the MQTT broker  

---