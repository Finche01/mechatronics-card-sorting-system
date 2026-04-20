# Troubleshooting Guide

[← Back to Main README](README.md)

---

## 🔍 Quick Diagnostic

**Start here:** Run the diagnostic tool

```bash
python tools/diagnostics.py
```

This will check:
- ✓ PLC connection
- ✓ Camera status
- ✓ Config file validity
- ✓ Motion system health
- ✓ Recent error logs

---

## 🚨 Common Issues

### Camera Issues

#### Issue: "Camera not detected"

**Symptoms:**
- "Failed to open camera" error
- Black screen in camera feed
- Application crashes on start

**Solutions:**

1. **Check Physical Connection**
   ```bash
   # Windows: Device Manager → Imaging Devices
   # Linux: 
   ls /dev/video*
   v4l2-ctl --list-devices
   ```

2. **Test Camera Independently**
   ```bash
   # Windows: Windows Camera app
   # Linux:
   cheese  # or
   ffplay /dev/video0
   ```

3. **Fix Camera Index**
   ```yaml
   # config.yaml
   camera:
     index: 0  # Try 0, 1, 2 if multiple cameras
   ```

4. **Reset USB Connection**
   - Unplug camera
   - Wait 10 seconds
   - Plug back in
   - Restart application

5. **Driver Issues (Windows)**
   - Update camera drivers in Device Manager
   - Install manufacturer's SDK if industrial camera

6. **Permission Issues (Linux)**
   ```bash
   # Add user to video group
   sudo usermod -a -G video $USER
   # Logout and login
   
   # Or temporary fix:
   sudo chmod 666 /dev/video0
   ```

---

#### Issue: "Poor card detection accuracy"

**Symptoms:**
- Cards not recognized
- Wrong suit/rank detected
- "Unknown card" errors

**Solutions:**

1. **Lighting Check**
   - Ensure even lighting (no shadows)
   - LED brightness: 80-100%
   - Position lights at 45° angles
   - Use diffusers for harsh lights

2. **Camera Focus**
   - Clean lens with microfiber cloth
   - Adjust focus ring (if manual focus)
   - Verify distance: 400-500mm from cards

3. **Recalibrate Camera**
   ```
   Menu → Calibration → Camera Setup
   1. Capture clean background
   2. Set detection threshold: 120-140
   3. Test with known cards
   ```

4. **Check Card Condition**
   - Use clean, unworn cards for best results
   - Replace bent or dirty cards
   - Enable "wear compensation" in config

5. **Adjust Vision Parameters**
   ```yaml
   # config.yaml
   vision:
     threshold: 130          # Increase if too sensitive
     min_card_area: 4500     # Adjust based on distance
     blur_kernel: 5          # Reduce noise
   ```

6. **Retrain Model** (Advanced)
   ```bash
   python tools/train_classifier.py --dataset data/cards/
   ```

---

#### Issue: "Camera lag / slow framerate"

**Symptoms:**
- Choppy video feed
- System slower than expected
- High CPU usage

**Solutions:**

1. **Lower Resolution**
   ```yaml
   # config.yaml
   camera:
     resolution: [1280, 720]  # Down from 1920x1080
     fps: 30
   ```

2. **Close Other Applications**
   - Disable other webcam apps
   - Close resource-heavy programs

3. **Update OpenCV**
   ```bash
   pip install opencv-python --upgrade
   ```

4. **Use Hardware Acceleration** (if available)
   ```python
   # In camera init code
   cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
   ```

---

### PLC Connection Issues

#### Issue: "Cannot connect to PLC"

**Symptoms:**
- "PLC connection timeout"
- "Connection refused"
- Red indicator on GUI

**Solutions:**

1. **Verify Network Connection**
   ```bash
   # Ping PLC
   ping 192.168.0.10
   
   # Should see replies:
   # Reply from 192.168.0.10: bytes=32 time=1ms
   ```

2. **Check IP Configuration**
   - PLC IP: `192.168.0.10`
   - Computer IP: `192.168.0.x` (same subnet)
   - Subnet mask: `255.255.255.0`

3. **Verify PLC Mode**
   - PLC must be in RUN mode
   - Check indicator lights on PLC
   - Use PLC programming software to verify

4. **Firewall Settings**
   ```bash
   # Windows: Allow Python through firewall
   # Linux:
   sudo ufw allow 502/tcp  # Modbus
   sudo ufw allow 102/tcp  # S7 Protocol
   ```

5. **Test with PLC Software**
   - Open TIA Portal / RSLogix
   - Attempt to go online with PLC
   - If this fails, issue is with PLC network config

6. **Check Cable Connection**
   - Ethernet cable properly seated
   - Try different cable
   - Test with another device

---

#### Issue: "PLC communication errors during operation"

**Symptoms:**
- Intermittent connection drops
- "Read/Write failed" errors
- System pauses unexpectedly

**Solutions:**

1. **Increase Timeout**
   ```python
   # In PLC communication code
   client.timeout = 5.0  # Increase from default 1.0
   ```

2. **Reduce Polling Rate**
   ```yaml
   # config.yaml
   plc:
     poll_interval: 0.1  # Increase from 0.05
   ```

3. **Check Network Load**
   - Other devices on same network?
   - Network switch overloaded?
   - Use dedicated network for PLC

4. **Verify PLC CPU Load**
   - Open PLC diagnostic buffer
   - Check cycle time < 50ms
   - Optimize PLC program if needed

---

### Motion Control Issues

#### Issue: "Axis not moving"

**Symptoms:**
- Motor doesn't respond
- Position stays at 0
- No movement on jog commands

**Solutions:**

1. **Check Emergency Stop**
   - Ensure E-Stop not pressed
   - Twist clockwise to reset
   - LED should be green

2. **Verify Motor Power**
   - Check 24V supply indicator
   - Measure voltage at motor driver: 20-28V
   - Check fuses

3. **Test Motor Driver**
   ```
   Send step pulses manually:
   1. Set DIR pin LOW
   2. Toggle PUL pin HIGH/LOW rapidly
   3. Motor should move slightly
   ```

4. **Check Wiring**
   - PLC outputs → Driver inputs
   - Driver outputs → Motor coils
   - Verify terminal tightness

5. **Swap Motor/Driver**
   - Test suspect motor on known-good axis
   - Isolates motor vs driver problem

6. **Review PLC Program**
   - Outputs enabled?
   - Motion routine executing?
   - Check PLC diagnostic buffer

---

#### Issue: "Axis moves in wrong direction"

**Symptoms:**
- Commanded +X moves -X
- Homing moves away from limit

**Solution:**

```yaml
# config.yaml - Invert direction
motion:
  invert_x: true   # Changes direction
  invert_y: false
  invert_z: false
```

Or swap DIR+ and DIR- wiring on motor driver.

---

#### Issue: "Positioning inaccuracy"

**Symptoms:**
- Repeatability poor (>1mm)
- Cards miss bins
- Drifting over time

**Solutions:**

1. **Mechanical Checks**
   - Tighten set screws on couplers
   - Check for loose pulleys/gears
   - Verify belt tension (if belt drive)
   - Lubricate linear bearings

2. **Recalibrate Steps/mm**
   ```python
   # Measure actual travel
   # Commanded: 100mm, Actual: 98mm
   # New steps/mm = old * (100/98)
   new_steps = 800 * (100/98) = 816.3
   ```

3. **Check for Missed Steps**
   - Reduce acceleration
   - Reduce maximum speed
   - Increase motor current (if too low)

4. **Home Before Each Cycle**
   ```yaml
   # config.yaml
   motion:
     home_before_sort: true
   ```

---

#### Issue: "Grinding noise / vibration"

**Symptoms:**
- Loud noise during motion
- Visible vibration
- Poor positioning

**Solutions:**

1. **Check Microstepping**
   - Should be set to 1/8 or 1/16
   - Verify driver DIP switches

2. **Adjust Acceleration**
   ```yaml
   # config.yaml
   motion:
     acceleration: 300  # Reduce from 500
   ```

3. **Mechanical Binding**
   - Manually move axis (power off)
   - Should move smoothly by hand
   - Look for debris in rails
   - Check perpendicularity

4. **Motor Current**
   - Set to 70% of motor rating
   - NEMA 23 2.8A motor → Set driver to 2.0A

---

### Gripper Issues

#### Issue: "Gripper not gripping cards"

**Solutions:**

1. **Check Air Pressure**
   ```
   Gauge should read: 4-5 bar (60-70 PSI)
   - Too low: Weak grip
   - Too high: Damages cards
   ```

2. **Test Solenoid Valve**
   ```bash
   # Manually activate valve
   # Should hear click and air flow
   ```

3. **Inspect Gripper Jaws**
   - Clean rubber pads
   - Replace worn pads
   - Verify parallel movement

4. **Adjust Pickup Height**
   ```yaml
   # config.yaml
   gripper:
     pickup_height: -3  # Increase compression
   ```

---

#### Issue: "Cards stick to gripper"

**Solutions:**

1. **Increase Release Delay**
   ```yaml
   # config.yaml
   gripper:
     release_delay: 0.4  # Increase from 0.2
   ```

2. **Add Air Blast**
   - Install blow-off valve
   - Brief air burst on release

3. **Gripper Pad Material**
   - Switch to less tacky pads
   - Try different durometer rubber

---

### Software Errors

#### Issue: "Module not found" errors

**Symptom:**
```
ModuleNotFoundError: No module named 'cv2'
```

**Solution:**
```bash
# Ensure virtual environment activated
source venv/bin/activate

# Reinstall package
pip install opencv-python
```

---

#### Issue: "Config file error"

**Symptom:**
```
yaml.scanner.ScannerError: mapping values are not allowed here
```

**Solutions:**

1. **Validate YAML Syntax**
   - Online validator: yamllint.com
   - Check indentation (use spaces, not tabs)
   - Ensure colons have space after: `key: value`

2. **Restore Default Config**
   ```bash
   cp config/config.yaml.default config/config.yaml
   ```

---

#### Issue: "Permission denied" (Linux)

**Symptom:**
```
PermissionError: [Errno 13] Permission denied
```

**Solutions:**

```bash
# For serial ports:
sudo usermod -a -G dialout $USER

# For camera:
sudo usermod -a -G video $USER

# For GPIO (if used):
sudo usermod -a -G gpio $USER

# Logout and login for changes to take effect
```

---

## 🔧 Advanced Diagnostics

### Enable Debug Logging

```python
# In main.py
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)
```

### Monitor PLC Communication

```bash
# Use Wireshark to capture packets
# Filter: tcp.port == 502  (Modbus)
# or: tcp.port == 102      (S7)
```

### Benchmark Vision Performance

```bash
python tools/benchmark_vision.py
```

Expected output:
```
Average processing time: 85ms
FPS: 11.8
Detection accuracy: 98.2%
```

---

## 📊 Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| E001 | Camera initialization failed | Check camera connection |
| E002 | PLC connection timeout | Verify network settings |
| E003 | Homing failed | Check limit switches |
| E004 | Card detection timeout | Ensure card in pickup position |
| E005 | Position out of bounds | Check soft limits in config |
| E006 | Emergency stop triggered | Reset E-stop button |
| E007 | Gripper pressure low | Check air supply |
| E008 | Config file invalid | Validate YAML syntax |

---

## 🆘 Emergency Contacts

**For Hardware Issues:**
- Mechanical: Check [Hardware Guide](HARDWARE.md)
- Electrical: Review wiring diagrams

**For Software Issues:**
- Documentation: [Installation Guide](INSTALLATION.md)
- GitHub Issues: [Open Issue](https://github.com/yourusername/Mechatronics-card-sorting-system/issues)

---

## 🧪 System Reset Procedure

**Complete system reset** (when all else fails):

```bash
# 1. Backup current config
cp config/config.yaml config/config.backup.yaml

# 2. Stop all processes
pkill -f main.py

# 3. Power cycle hardware
# - Turn off PLC
# - Disconnect camera
# - Wait 30 seconds
# - Reconnect everything

# 4. Restore default config
cp config/config.yaml.default config/config.yaml

# 5. Run full calibration
python tools/calibrate_all.py

# 6. Restart system
python main.py
```

---

## 📈 Performance Issues

### System Running Slow

1. **Check CPU Usage**
   ```bash
   # Linux
   top
   # Look for main.py process
   ```

2. **Optimize Vision Processing**
   - Lower camera resolution
   - Reduce frame processing rate
   - Disable unnecessary features

3. **Database Cleanup** (if using logging DB)
   ```bash
   python tools/cleanup_logs.py --days 30
   ```

---

## 🔍 Still Need Help?

If you've tried everything above:

1. **Collect Diagnostic Info**
   ```bash
   python tools/system_info.py > system_report.txt
   ```

2. **Record Issue**
   - Video of problem (if mechanical)
   - Screenshot of error
   - Copy of log file

3. **Open GitHub Issue**
   - Include system_report.txt
   - Describe steps to reproduce
   - Attach recordings

---

[← Back to Main README](README.md) | [Contributing →](CONTRIBUTING.md)
