# Software Installation Guide

[← Back to Main README](README.md)

---

## 📋 Prerequisites

Before beginning installation, ensure you have:

- Windows 10/11 or Ubuntu 20.04+ (64-bit)
- Python 3.8 or higher
- Administrator/sudo privileges
- Internet connection for package downloads
- PLC programming software (Siemens TIA Portal or RSLogix)
- USB camera drivers

---

## 🐍 Python Environment Setup

### Windows Installation

1. **Download Python**
   ```
   Visit: https://www.python.org/downloads/
   Download: Python 3.11.x (latest stable)
   ```

2. **Install Python**
   - Run installer
   - ✅ Check "Add Python to PATH"
   - Click "Install Now"

3. **Verify Installation**
   ```bash
   python --version
   pip --version
   ```

### Linux Installation

```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3.11 python3-pip python3-venv

# Verify installation
python3 --version
pip3 --version
```

---

## 📦 Create Virtual Environment

**Recommended** to isolate project dependencies:

```bash
# Navigate to project directory
cd Mechatronics-card-sorting-system

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# You should see (venv) in your terminal prompt
```

---

## 📚 Install Required Packages

### Option 1: Install from requirements.txt

```bash
pip install -r requirements.txt
```

### Option 2: Manual Installation

```bash
# Core dependencies
pip install opencv-python==4.8.0
pip install numpy==1.24.3
pip install scikit-learn==1.3.0
pip install pillow==10.0.0

# PLC communication (choose based on your PLC)
pip install pymodbus==3.5.2        # For Modbus TCP/RTU
pip install pycomm3==1.2.1         # For Allen-Bradley Ethernet/IP
pip install python-snap7==1.3      # For Siemens S7

# GUI and visualization
pip install matplotlib==3.7.2
pip install tkinter  # Usually included with Python

# Utilities
pip install pyserial==3.5          # For serial communication
pip install pyyaml==6.0.1          # For configuration files
```

---

## 📷 Camera Setup

### Windows

1. **Install Camera Drivers**
   - Most USB cameras work with default Windows drivers
   - For industrial cameras, install manufacturer's SDK
   - Download from camera manufacturer's website

2. **Test Camera Access**
   ```python
   import cv2
   
   # Test camera
   cap = cv2.VideoCapture(0)  # 0 = default camera
   ret, frame = cap.read()
   
   if ret:
       print("Camera working!")
       cv2.imshow('Test', frame)
       cv2.waitKey(0)
   else:
       print("Camera not detected")
   
   cap.release()
   cv2.destroyAllWindows()
   ```

### Linux

```bash
# Install video capture libraries
sudo apt install libv4l-dev v4l-utils

# List available cameras
v4l2-ctl --list-devices

# Test camera (should show video feed)
ffplay /dev/video0
```

---

## 🔌 PLC Software Setup

### For Siemens PLCs (S7-1200/1500)

1. **Download TIA Portal**
   - Visit: Siemens Support
   - Version: v17 or later
   - License: Required

2. **Install SNAP7 Library** (for Python communication)
   ```bash
   # Windows
   pip install python-snap7
   # Download snap7.dll from https://sourceforge.net/projects/snap7/
   # Place snap7.dll in: C:\Windows\System32\
   
   # Linux
   sudo apt install libsnap7-1 libsnap7-dev
   pip install python-snap7
   ```

3. **Configure PLC Network**
   - Set PLC IP address (e.g., 192.168.0.10)
   - Enable PUT/GET communication
   - Disable "Optimized block access" for DBs

### For Allen-Bradley PLCs

1. **Download RSLogix/Studio 5000**
   - Visit: Rockwell Automation
   - Install connected components workbench

2. **Install pycomm3**
   ```bash
   pip install pycomm3
   ```

3. **Configure Ethernet/IP**
   - Set PLC IP address
   - Enable Ethernet/IP communication
   - Note: No additional drivers needed for pycomm3

---

## ⚙️ Configuration Files

### 1. Create config.yaml

```yaml
# config.yaml
system:
  name: "Card Sorting System"
  version: "1.0.0"

camera:
  index: 0                    # Camera device ID
  resolution: [1920, 1080]    # Width x Height
  fps: 30
  exposure: -6                # Auto exposure if -1

vision:
  threshold: 127              # Binary threshold for card detection
  min_card_area: 5000         # Minimum contour area (pixels)
  max_card_area: 50000        # Maximum contour area (pixels)

plc:
  type: "modbus"              # Options: modbus, snap7, pycomm3
  ip: "192.168.0.10"
  port: 502
  rack: 0                     # For Siemens S7
  slot: 1
  
motion:
  steps_per_mm_x: 800
  steps_per_mm_y: 800
  steps_per_mm_z: 1600
  max_speed: 200              # mm/s
  acceleration: 500           # mm/s²
  
  # Work area limits (mm)
  x_min: 0
  x_max: 950
  y_min: 0
  y_max: 550
  z_min: 0
  z_max: 150
  
  # Positions
  home: [0, 0, 150]
  pickup: [100, 100, 0]
  sort_positions:
    hearts: [200, 300, 100]
    diamonds: [400, 300, 100]
    clubs: [600, 300, 100]
    spades: [800, 300, 100]

gripper:
  pickup_height: -2           # mm below card surface
  release_height: 50          # mm above drop position
  grip_delay: 0.3             # seconds to stabilize
  release_delay: 0.2
```

### 2. Create .env file (optional - for sensitive data)

```bash
# .env
PLC_IP=192.168.0.10
PLC_PASSWORD=yourpassword
ADMIN_EMAIL=admin@example.com
```

Install python-dotenv:
```bash
pip install python-dotenv
```

---

## 🧪 Test Installation

Run the included test script:

```bash
python tests/test_installation.py
```

Expected output:
```
✓ Python version: 3.11.x
✓ OpenCV version: 4.8.0
✓ Camera detected: Yes
✓ PLC connection: OK
✓ Config file loaded: OK

All systems operational!
```

### Manual Component Tests

**Test 1: Camera**
```bash
python tests/test_camera.py
```

**Test 2: PLC Connection**
```bash
python tests/test_plc.py
```

**Test 3: Vision System**
```bash
python tests/test_vision.py
```

---

## 🚀 First Run

1. **Start the system**
   ```bash
   python main.py
   ```

2. **Expected Startup Sequence**
   ```
   [INFO] Loading configuration...
   [INFO] Connecting to PLC at 192.168.0.10...
   [OK] PLC connected
   [INFO] Initializing camera...
   [OK] Camera ready
   [INFO] Homing all axes...
   [OK] System ready
   ```

3. **GUI Should Display**
   - Live camera feed
   - System status indicators
   - Control buttons

---

## 🔧 Common Installation Issues

### Issue: "opencv not found"
**Solution:**
```bash
pip uninstall opencv-python
pip install opencv-python-headless==4.8.0
```

### Issue: "Could not connect to PLC"
**Checklist:**
- [ ] PLC IP address correct in config.yaml
- [ ] PLC and computer on same network
- [ ] Firewall allowing port 502 (Modbus) or 102 (S7)
- [ ] PLC in RUN mode

**Test connection:**
```bash
ping 192.168.0.10
```

### Issue: "Camera not detected"
**Windows:**
```bash
# List camera devices
python -c "import cv2; print([cv2.VideoCapture(i) for i in range(10)])"
```

**Linux:**
```bash
ls -l /dev/video*
# Add user to video group
sudo usermod -a -G video $USER
# Logout and login again
```

### Issue: "Permission denied" on Linux
```bash
# Give execute permissions
chmod +x main.py

# For camera access
sudo chmod 666 /dev/video0

# For serial port access
sudo usermod -a -G dialout $USER
```

---

## 📱 Optional: GUI Enhancement (PyQt5)

For a more professional interface:

```bash
pip install PyQt5==5.15.9
pip install pyqtgraph==0.13.3
```

---

## 🔄 Update Procedure

To update to the latest version:

```bash
# Pull latest code
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Re-run tests
python tests/test_installation.py
```

---

## 🗂️ Directory Structure

After installation, your project should look like:

```
Mechatronics-card-sorting-system/
├── venv/                      # Virtual environment (don't commit)
├── src/
│   ├── vision/                # Computer vision modules
│   ├── motion/                # Motion control
│   ├── plc/                   # PLC communication
│   └── gui/                   # User interface
├── config/
│   ├── config.yaml            # System configuration
│   └── .env                   # Sensitive data
├── tests/                     # Test scripts
├── assets/                    # Images, icons
├── logs/                      # System logs
├── requirements.txt
└── main.py
```

---

## 📞 Support

Installation issues? Check:
1. [Troubleshooting Guide](TROUBLESHOOTING.md)
2. [GitHub Issues](https://github.com/yourusername/Mechatronics-card-sorting-system/issues)

---

[← Back to Main README](README.md) | [Next: User Guide →](USER_GUIDE.md)
