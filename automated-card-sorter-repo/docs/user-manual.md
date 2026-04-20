# Automated Card Sorting System - User Manual

## Table of Contents
1. [Safety Guidelines](#safety-guidelines)
2. [System Startup](#system-startup)
3. [Operating Procedures](#operating-procedures)
4. [Troubleshooting](#troubleshooting)
5. [Emergency Procedures](#emergency-procedures)

## Safety Guidelines

### ⚠️ WARNING
Only trained operators should operate this system. Improper use can result in equipment damage or personal injury.

### Safety Requirements
- ✅ Emergency stop must be functional and accessible
- ✅ Keep hands clear of gantry travel area during operation
- ✅ Wear safety glasses when working near moving machinery
- ✅ Do not bypass limit switches or safety interlocks
- ✅ Ensure proper grounding of all electrical components

### Hazard Zones
- **Pinch Points**: X/Y axis belt drives and Z-axis lead screw
- **Moving Parts**: Gantry motion in all three axes
- **Electrical**: 24VDC system, low voltage but can cause sparks

---

## System Startup

### 1. Power Application

1. **Main Power**
   - Switch ON the main breaker
   - Verify indicator lights on control panel
   - Confirm PLC power LED is illuminated

2. **Visual Inspection**
   - Check for loose wires or damaged components
   - Ensure gantry travel area is clear
   - Verify vacuum hose connections are secure

### 2. Software Connectivity

1. **Connect to PLC**
   ```bash
   # Connect laptop via Ethernet to PLC
   # Static IP: 192.168.1.100 (typical)
   ```

2. **Start Docker Services**
   ```bash
   docker-compose up -d
   ```

3. **Access Node-RED Dashboard**
   - Open web browser
   - Navigate to: `http://localhost:1880/ui`
   - Verify connection status indicator is green

4. **Launch Vision System**
   ```bash
   cd software/vision
   python card_classifier.py
   ```

### 3. System Readiness Verification

Confirm the following on the Node-RED dashboard:

- [ ] XY Position Monitor displays coordinates
- [ ] Position/Velocity Graph is updating
- [ ] Live camera image visible in Pick and Place panel
- [ ] Motor status shows "Disabled" (red indicator)
- [ ] Emergency stop is released (mushroom button pulled out)

---

## Operating Procedures

### Motor Enable Sequence

1. Navigate to **Motor Control** section on dashboard
2. Verify E-stop is **released**
3. Clear gantry travel area of all obstructions
4. Toggle **Motor Enable** switch
5. Green indicator OFF → Red indicator ON = Motors Enabled

### Homing Procedure

**⚠️ REQUIRED BEFORE ANY MOTION COMMANDS**

1. Click **"Home All"** button in Homing section
2. System will execute:
   - Z-axis raises to upper limit (safety first)
   - X/Y axes move to front-left corner
   - Limit switches establish reference zero
3. Wait for **"Homing Complete"** confirmation
4. Gantry position should read approximately (0, 0, Z_max)

### Manual Motion Control

#### Jogging Mode
Use for calibration, inspection, or manual positioning.

1. **Set Increment**
   - Enter distance in mm (e.g., 10)
   - Typical range: 1-50mm

2. **Move Axes**
   - Click directional arrows (←, →, ↑, ↓, Z+, Z-)
   - Gantry moves specified distance
   - Position updates on dashboard

3. **Safety Limits**
   - Motion stops at limit switches
   - Re-homing required after limit activation

#### Preset Positions
Quick navigation to calibrated coordinates.

1. Select preset from dropdown:
   - Camera Station
   - Flipper Drop-off
   - Flipper Pickup
   - Home Position
   - Bin Array Center

2. Click **"Go to Preset"**
3. Gantry moves to stored coordinates automatically

### Pick-and-Place Test

Verify vacuum and motion before automated sorting.

1. **Load Test Card**
   - Place card in feed bin
   - Ensure card is flat and accessible

2. **Configure Locations**
   - Pickup Location: Select feed bin number
   - Placement Location: Select target bin number

3. **Execute Routine**
   - Click **"Run Pick and Place"**
   - System performs:
     1. Move to pickup coordinates
     2. Lower Z-axis (photoelectric slowdown)
     3. Engage vacuum (verify pressure switch)
     4. Lift card
     5. Move to placement coordinates
     6. Lower Z-axis
     7. Release vacuum
     8. Raise Z-axis
     9. Return to home

4. **Verify Success**
   - Card transferred to target bin
   - No vacuum errors
   - Smooth motion profile

### Automated Sorting Program

#### Sorting Modes
- **Rank Sorting**: Groups by card value (A, 2-10, J, Q, K)
- **Suit Sorting**: Groups by suit (♠, ♥, ♦, ♣)

#### Operation Steps

1. **Prepare System**
   - Load cards in feed bin (stack up to 52 cards)
   - Ensure all target bins are empty
   - Verify vacuum reservoir pressure

2. **Select Mode**
   - Navigate to **Program** section
   - Choose sorting mode (Rank or Suit)
   - Specify feed bin location

3. **Start Sorting**
   - Click **"Start Program"**
   - System begins automated cycle:
     1. Move to feed bin
     2. Pick top card
     3. Move to camera station
     4. Request vision classification (Index 999)
     5. Receive bin index from Node-RED
     6. If Index 77 → Execute flip sequence
     7. Move to target bin
     8. Place card
     9. Return to feed bin
     10. Repeat until bin empty or cancelled

4. **Monitor Operation**
   - Dashboard shows:
     - Current card classification
     - Confidence level
     - Destination bin
     - Cards sorted count
     - Errors/retries

5. **Stop/Pause**
   - Click **"Cancel"** to stop sorting
   - System completes current card cycle
   - Gantry returns to safe position

#### Flip Sequence
Executed when vision returns Index 77 (inverted card or low confidence)

1. Move to Flipper Drop-off (Index 22)
2. Release card onto flipper mechanism
3. Wait for flip complete signal
4. Move to Flipper Pickup (Index 24)
5. Pick flipped card
6. Request re-scan (Index 999)

---

## Troubleshooting

### Problem: Motors Not Responding

**Symptoms**: Jogging commands have no effect

**Checks**:
- [ ] Motor enable switch is ON (red indicator)
- [ ] E-stop is released
- [ ] PLC power indicator is lit
- [ ] Motor driver LEDs are illuminated
- [ ] Check for loose motor connectors

**Solution**: 
1. Toggle motor enable OFF then ON
2. If no change, power cycle the system
3. Re-home after power restoration

---

### Problem: Vacuum Pickup Failure

**Symptoms**: Card not lifted, pressure switch error

**Checks**:
- [ ] Vacuum reservoir pressure (-20 to -40 kPa)
- [ ] Solenoid valve clicking sound when engaged
- [ ] Suction cup not dirty or damaged
- [ ] Vacuum hose not kinked or disconnected

**Solution**:
1. Run vacuum motor for 30 seconds to build pressure
2. Clean suction cup with isopropyl alcohol
3. Check pressure gauge on reservoir
4. Listen for air leaks in system

---

### Problem: Vision Classification Errors

**Symptoms**: Cards sent to wrong bins, frequent flip requests

**Checks**:
- [ ] Camera lens is clean
- [ ] Lighting is consistent
- [ ] Cards are standard playing cards
- [ ] Python script is running without errors
- [ ] MQTT connection status is "Connected"

**Solution**:
1. Clean camera lens with microfiber cloth
2. Restart Python vision script
3. Check template images are loaded correctly
4. Verify camera focus at card station height

---

### Problem: Limit Switch Activation

**Symptoms**: Motion stops unexpectedly, error message

**Checks**:
- [ ] Gantry physically at travel limit
- [ ] Limit switch not mechanically stuck
- [ ] Wiring to limit switch intact

**Solution**:
1. Press E-stop to disable motors
2. Manually move gantry away from limit (if safe)
3. Release E-stop
4. Re-home system before resuming

---

### Problem: Communication Loss

**Symptoms**: Dashboard not updating, "Connection Lost" message

**Checks**:
- [ ] Ethernet cable connected to PLC
- [ ] Node-RED container running
- [ ] Python script active
- [ ] No firewall blocking localhost:1880

**Solution**:
1. Check Docker status: `docker ps`
2. Restart containers: `docker-compose restart`
3. Verify PLC IP address matches configuration
4. Check Modbus TCP connection in Node-RED debug

---

## Emergency Procedures

### Emergency Stop (E-Stop)

**When to Use**:
- Unexpected motion or behavior
- Person/object in gantry path
- Unusual sounds or vibrations
- Smoke or burning smell
- Any unsafe condition

**Procedure**:
1. **PRESS RED MUSHROOM BUTTON** (E-stop)
2. Motors immediately disabled
3. Vacuum releases (if engaged)
4. All motion stops

**Recovery**:
1. Identify and resolve cause of emergency
2. Clear gantry area
3. Pull E-stop button out to release
4. Re-home system before resuming operation

---

### Power Failure

**During Operation**:
1. System loses position reference
2. Card may be in transit when power lost
3. Vacuum releases automatically

**Recovery**:
1. Remove any cards from gantry/gripper manually
2. Restore main power
3. Follow standard startup procedure
4. Re-home system (critical!)
5. Resume sorting from beginning

---

### Runaway Motion

**Symptoms**: Gantry moving without command or at wrong speed

**Immediate Action**:
1. **PRESS E-STOP IMMEDIATELY**
2. Do not attempt to physically stop motion
3. Turn off main power if E-stop ineffective

**Investigation**:
1. Check for stuck keys on dashboard
2. Verify PLC program integrity
3. Inspect motor driver connections
4. Contact technical support before resuming

---

## System Shutdown

### Normal Shutdown Procedure

1. **Complete Current Operation**
   - Allow sorting cycle to finish
   - Don't interrupt mid-cycle

2. **Stop Program**
   - Click "Cancel" on dashboard
   - Wait for gantry to return to safe position

3. **Disable Motors**
   - Toggle motor enable to OFF
   - Green indicator should illuminate

4. **Close Software**
   - Stop Python vision script (Ctrl+C)
   - Close Node-RED dashboard browser tab
   - Stop Docker containers: `docker-compose down`

5. **Power Down**
   - Switch OFF main breaker
   - Wait 10 seconds for capacitors to discharge

6. **Secure System**
   - Clear bins if needed
   - Cover electronics from dust
   - Log any issues in maintenance record

---

## Daily Maintenance Checklist

**Before Operation**:
- [ ] Visual inspection for loose wires
- [ ] Vacuum hose connections secure
- [ ] Suction cup clean and undamaged
- [ ] Bins empty and properly positioned
- [ ] E-stop functional test

**After Operation**:
- [ ] Clean suction cup
- [ ] Remove debris from bins and workspace
- [ ] Record operation hours
- [ ] Note any unusual behavior for maintenance log

---

## Contact Information

**Technical Support**:
- Joshua Craven: jcraven@myseneca.ca | 647-248-7322
- Jae Park: jpark83@myseneca.ca | 647-500-4630

**Emergency Contacts**:
- Facility Supervisor: [Add local contact]
- Maintenance Team: [Add local contact]

---

**Document Revision**: 1.0  
**Last Updated**: March 2026  
**Next Review**: September 2026
