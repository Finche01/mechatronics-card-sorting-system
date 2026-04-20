# User Guide

[← Back to Main README](README.md)

---

## 🎯 Quick Start

**First Time Setup:**
1. Complete [Hardware Setup](HARDWARE.md)
2. Complete [Software Installation](INSTALLATION.md)
3. Run calibration routine (see below)
4. Start sorting!

---

## 🚀 Starting the System

### Launch Application

```bash
# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Start the application
python main.py
```

### Startup Sequence

The system performs these checks automatically:

```
┌─────────────────────────────────────┐
│ 1. Load Configuration               │
│    ✓ config.yaml loaded             │
├─────────────────────────────────────┤
│ 2. PLC Connection                   │
│    ✓ Connected to 192.168.0.10      │
├─────────────────────────────────────┤
│ 3. Camera Initialization            │
│    ✓ Camera 0 ready (1920x1080)     │
├─────────────────────────────────────┤
│ 4. Homing Sequence                  │
│    ✓ X-axis homed                   │
│    ✓ Y-axis homed                   │
│    ✓ Z-axis homed                   │
├─────────────────────────────────────┤
│ 5. Vision System Check              │
│    ✓ Card detection model loaded    │
└─────────────────────────────────────┘

🟢 SYSTEM READY
```

---

## 🖥️ User Interface

### Main Window Layout

```
┌────────────────────────────────────────────────────┐
│  Card Sorting System v1.0          [Status: READY] │
├──────────────┬─────────────────────────────────────┤
│              │                                     │
│   Camera     │        System Controls              │
│   Feed       │                                     │
│   (Live)     │   [Start]  [Pause]  [Stop]          │
│              │   [Home]   [Calibrate]               │
│              │                                     │
│              │   Current Position:                 │
│              │   X: 125.5 mm  Y: 200.0 mm          │
│              │   Z: 50.0 mm                        │
│              │                                     │
│              │   Cards Sorted: 47                  │
│              │   Errors: 0                         │
│              │                                     │
├──────────────┴─────────────────────────────────────┤
│  Log:                                              │
│  [10:32:15] System started                         │
│  [10:32:22] Detected: 7 of Hearts                  │
│  [10:32:25] Sorted to Hearts bin                   │
└────────────────────────────────────────────────────┘
```

### Button Functions

| Button | Function | Shortcut |
|--------|----------|----------|
| **Start** | Begin automatic sorting | F5 |
| **Pause** | Pause operation (preserves position) | Space |
| **Stop** | Stop and return to home | Esc |
| **Home** | Move all axes to home position | H |
| **Calibrate** | Run camera calibration routine | C |
| **E-Stop** | Emergency stop (hardware button) | - |

---

## 🎴 Operating Modes

### 1. Automatic Mode (Default)

**Purpose:** Continuous sorting of card deck

**Operation:**
1. Place shuffled deck in input tray
2. Click **Start** button
3. System automatically:
   - Picks up card
   - Images card
   - Classifies suit/rank
   - Sorts to appropriate bin
4. Repeats until deck is empty

**Settings:**
- Speed: Adjustable (50-100%)
- Sort criteria: Suit / Rank / Both
- Card verification: On/Off

### 2. Manual Mode

**Purpose:** Test individual movements or specific card placement

**Operation:**
1. Click **Mode** → **Manual**
2. Use jog controls to move axes
3. Test gripper with **Grip/Release** buttons
4. Take test images with **Capture** button

**Controls:**
- Arrow keys: Move X/Y axes
- PgUp/PgDn: Move Z axis
- +/- : Adjust jog distance (1mm, 10mm, 100mm)

### 3. Calibration Mode

**Purpose:** Set up camera and motion parameters

**Procedure:** See Calibration section below

---

## 🔧 Calibration Procedures

### Camera Calibration

**When to calibrate:**
- First time setup
- Camera moved or adjusted
- Lighting conditions changed
- Detection accuracy drops

**Steps:**

1. **Access Calibration Menu**
   ```
   Menu → Calibration → Camera Setup
   ```

2. **Background Capture**
   - Remove all cards from work area
   - Click **Capture Background**
   - System stores clean background image

3. **Card Reference**
   - Place standard playing card in pickup position
   - Click **Capture Card Reference**
   - System learns card dimensions and features

4. **Detection Threshold**
   - Adjust slider until card outline is clear in preview
   - Recommended: 120-140 for most lighting
   - Save settings

5. **Test Detection**
   - Place 5-10 different cards randomly
   - Click **Test Detection**
   - All cards should be outlined in green
   - If not, adjust threshold and retry

**Expected Results:**
- Detection rate: >98%
- False positives: <1%
- Processing time: <100ms per card

### Motion Calibration

**Home Position Setup:**

1. **Physical Alignment**
   - Manually move gantry to home position
   - Ensure all limit switches are accessible
   - Verify no obstacles in motion path

2. **Run Homing Sequence**
   ```
   Menu → Calibration → Home All Axes
   ```
   
3. **Verify Positions**
   - X-axis: Should be at left limit
   - Y-axis: Should be at back limit
   - Z-axis: Should be at top limit

**Position Teaching:**

Define pickup and drop positions:

1. **Manual Jog** to desired position
2. **Record Position**:
   ```
   Menu → Positions → Teach Position
   Enter name: "Hearts_Drop"
   Save
   ```

3. **Test Position**:
   ```
   Menu → Positions → Go To → Hearts_Drop
   ```

**Standard Positions to Teach:**
- Pickup position (where cards are fed)
- Hearts bin
- Diamonds bin
- Clubs bin
- Spades bin
- Discard bin (for unrecognized cards)

### Gripper Calibration

**Grip Pressure:**

1. Place single card at pickup position
2. Adjust pressure regulator (4-5 bar typical)
3. Test grip:
   - Should hold card securely
   - Should not crumple card
   - Card releases cleanly

**Pickup Height:**

1. Jog Z-axis to just above card
2. Lower in 0.1mm increments
3. Optimal: -2mm (slight compression)
4. Save as `z_pickup_offset` in config

**Release Timing:**

1. Test drop sequence
2. Adjust delay if cards stick to gripper
3. Typical: 0.2-0.3 seconds

---

## 📊 Card Detection System

### How It Works

```
┌─────────────┐
│ Camera      │  Capture image of card
│ Capture     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Preprocess  │  Convert to grayscale, threshold
│ Image       │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Find        │  Detect card contours
│ Contours    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Extract     │  Crop to card corners
│ Features    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Classify    │  Match to trained patterns
│ Suit & Rank │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Sort        │  Move to appropriate bin
│ Decision    │
└─────────────┘
```

### Card Classification

The system recognizes:
- **Suits:** Hearts ♥, Diamonds ♦, Clubs ♣, Spades ♠
- **Ranks:** A, 2-10, J, Q, K
- **Total:** 52 unique cards per deck

### Confidence Levels

| Confidence | Action |
|------------|--------|
| >90% | Auto-sort |
| 70-90% | Sort with warning log |
| <70% | Place in discard bin for manual review |

---

## 🎮 Sorting Strategies

### By Suit (Default)

Cards sorted into 4 bins by suit:
- Bin 1: Hearts ♥
- Bin 2: Diamonds ♦
- Bin 3: Clubs ♣
- Bin 4: Spades ♠

### By Rank

Cards sorted into 13 bins by rank:
- Requires 13-bin configuration
- A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K

### Custom Sorting

Define your own rules:
```yaml
# In config.yaml
sorting:
  mode: "custom"
  rules:
    - condition: "rank == 'A'"
      destination: "bin_1"
    - condition: "suit in ['Hearts', 'Diamonds']"
      destination: "bin_2"
    - condition: "rank in ['J', 'Q', 'K']"
      destination: "bin_3"
    - condition: "default"
      destination: "bin_4"
```

---

## 📈 Performance Monitoring

### Real-Time Statistics

**Dashboard displays:**
- Cards per minute (CPM)
- Total cards sorted
- Error rate
- Average cycle time
- System uptime

### Performance Targets

| Metric | Target | Acceptable | Action Required |
|--------|--------|------------|-----------------|
| Speed | 60 CPM | >50 CPM | <50 CPM |
| Accuracy | >98% | >95% | <95% |
| Cycle Time | <1.0s | <1.2s | >1.2s |

**If performance degrades:**
1. Check camera lens for dirt/fingerprints
2. Verify lighting is even
3. Run calibration routine
4. Check for mechanical binding

---

## 🔄 Typical Workflow

### Daily Startup

```
1. Power On System
   └─> Check air pressure (4-5 bar)
   └─> Verify camera is connected
   └─> Check card bins are empty

2. Launch Software
   └─> Wait for green "READY" status
   └─> Review log for any warnings

3. Quick Test
   └─> Place 5 test cards
   └─> Run manual sort
   └─> Verify correct classification

4. Begin Production
   └─> Load card deck
   └─> Click Start
   └─> Monitor first 10 cards
```

### During Operation

- **Monitor camera feed** for misalignments
- **Check bins** don't overflow
- **Watch error log** for issues
- **Pause if needed** using Pause button

### Shutdown

```
1. Stop Current Operation
   └─> Click Stop button
   └─> Wait for axes to return home

2. Close Software
   └─> Menu → Exit
   └─> Confirm save settings

3. Power Down
   └─> Close air valve
   └─> Turn off PLC
   └─> Disconnect camera (optional)
```

---

## 🛡️ Safety Guidelines

### Before Operating

✅ **DO:**
- Inspect system for loose parts
- Verify E-stop button works
- Clear work area of obstacles
- Tie back loose clothing/hair
- Wear safety glasses

❌ **DON'T:**
- Reach into work area during operation
- Override safety interlocks
- Operate with damaged components
- Leave system unattended during auto mode

### Emergency Procedures

**If something goes wrong:**

1. **Press E-Stop immediately**
2. Power down system
3. Identify issue (see Troubleshooting)
4. Fix problem
5. Reset E-Stop
6. Run test cycle before resuming

**Emergency Stop Button:**
- Located on control panel
- Twist clockwise to reset
- System will not operate until reset

---

## 🧹 Maintenance

### Daily (5 minutes)
- Wipe camera lens
- Check air pressure
- Empty card bins
- Visual inspection

### Weekly (15 minutes)
- Clean linear rails
- Lubricate moving parts
- Tighten loose bolts
- Verify limit switches

### Monthly (1 hour)
- Full calibration routine
- Deep clean all components
- Check motor temperatures
- Review error logs

---

## 💡 Tips & Tricks

### Improving Speed
- Increase motion speed in config (test incrementally)
- Reduce Z-axis travel distance
- Optimize sort bin positions
- Use "fast drop" mode (no verification)

### Improving Accuracy
- Add more light sources
- Increase camera resolution
- Slow down pickup speed
- Use higher confidence threshold
- Retrain classification model with more samples

### Handling Worn Cards
- Increase detection threshold
- Enable "wear compensation" mode
- Use preprocessing filters
- Consider manual pre-sort

---

## 📞 Getting Help

1. Check [Troubleshooting Guide](TROUBLESHOOTING.md)
2. Review error logs: `logs/system.log`
3. Search [GitHub Issues](https://github.com/yourusername/Mechatronics-card-sorting-system/issues)
4. Open new issue with:
   - System log file
   - Screenshot of error
   - Video of problem (if mechanical)

---

[← Back to Main README](README.md) | [Next: Troubleshooting →](TROUBLESHOOTING.md)
