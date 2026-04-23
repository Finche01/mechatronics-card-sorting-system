# PLC Overview

## System Information

| Parameter | Value |
|:----------|:------|
| **PLC Model** | Click PLUS C2-01CPU-2 |
| **Program Name** | XYZT2_V56 |
| **IP Address** | 192.168.1.10 |
| **Communication Protocol** | Modbus TCP (Server) |
| **Firmware** | Included in loader file |

---

## Hardware Configuration

### CPU Module
- **Model**: C2-01CPU-2
- **Power**: 24 VDC
- **Ports**: Ethernet, Serial, MicroB-USB
- **Features**: Battery backup, 2 option slots

### I/O Modules

| Slot | Module | Type | Inputs | Outputs | Description |
|:----:|:-------|:-----|:------:|:-------:|:------------|
| **1** | C2-14D2 | Combo | 8 × 24VDC | 6 × 24VDC (0.1A) | Discrete I/O for sensors and low-power devices |
| **2** | C2-14DR | Combo | 8 × 24VDC | 6 × Relay (1A) | Relay outputs for higher power loads |
| **Base** | C0-16TD1 | Output | - | 16 × 5-27VDC (0.1A) | Sinking outputs for stepper drivers |

---

## I/O Configuration

### Digital Inputs (24 VDC)

| Address | Nickname | Function | Module | Description |
|:--------|:---------|:---------|:-------|:------------|
| **X001** | X_LmtNeg | Limit Switch | C2-14D2 | X-axis negative limit (homing reference) |
| **X002** | Y_LmtNeg | Limit Switch | C2-14D2 | Y-axis negative limit (homing reference) |
| **X003** | Z_LmtPos | Limit Switch | C2-14D2 | Z-axis positive limit (top position) |
| **X004** | Motor_Enable_Feedback | Motor Status | C2-14D2 | Stepper driver enable feedback |
| **X005** | Flipper LSW Normal | Limit Switch | C2-14D2 | Card flipper in normal position |
| **X006** | Flipper LSW Flipped | Limit Switch | C2-14D2 | Card flipper in flipped position |
| **X021** | Tool_Compression | Sensor | C2-14DR | Tool compression sensor (Z-axis contact detection) |
| **X022** | Tool_Card_Detect | Sensor | C2-14DR | Photoelectric sensor - card presence detection |
| **X025** | Vacuum_Ok | Pressure Switch | C2-14DR | ZSE30 vacuum pressure switch - vacuum level OK |

### Digital Outputs - Stepper Motor Control

| Address | Nickname | Function | Module | Connection |
|:--------|:---------|:---------|:-------|:-----------|
| **Y001** | X_Pulse | Step Signal | C0-16TD1 | X-axis stepper driver (PUL+) |
| **Y002** | X_Dir | Direction | C0-16TD1 | X-axis stepper driver (DIR+) |
| **Y003** | Y_Pulse | Step Signal | C0-16TD1 | Y-axis stepper driver (PUL+) |
| **Y004** | Y_Dir | Direction | C0-16TD1 | Y-axis stepper driver (DIR+) |
| **Y005** | Z_Pulse | Step Signal | C0-16TD1 | Z-axis stepper driver (PUL+) |
| **Y006** | Z_Dir | Direction | C0-16TD1 | Z-axis stepper driver (DIR+) |

### Digital Outputs - System Control

| Address | Nickname | Function | Module | Load Type |
|:--------|:---------|:---------|:-------|:----------|
| **Y026** | Main Cage LED | Lighting | C0-16TD1 | COB LED strip (24V) |
| **Y101** | Motor_Disable | Motor Enable | C0-16TD1 | Stepper drivers disable signal |
| **Y102** | Vision_LED | Lighting | C0-16TD1 | Vision system illumination (24V COB LED) |
| **Y104** | Vacuum_Pump | Pump Control | C0-16TD1 | Vacuum pump 24V diaphragm |
| **Y105** | Tool_Vacuum | Solenoid Valve | C0-16TD1 | Tool suction cup vacuum valve |
| **Y106** | Tool_Release | Solenoid Valve | C0-16TD1 | Tool suction cup release valve |
| **Y107** | Flipper_Vacuum | Solenoid Valve | C0-16TD1 | Flipper suction cup vacuum valve |
| **Y108** | Flipper_Release | Solenoid Valve | C0-16TD1 | Flipper suction cup release valve |
| **Y113** | Flipper RUN | Motor Enable | C0-16TD1 | Flipper DC gear motor run |
| **Y114** | Flipper FWD | Motor Direction | C0-16TD1 | Flipper forward rotation |
| **Y115** | Flipper REV | Motor Direction | C0-16TD1 | Flipper reverse rotation |

### Relay Outputs (Available)

| Address | Nickname | Status | Notes |
|:--------|:---------|:-------|:------|
| **Y021-Y025** | DR OUT 1-5 | Reserved | C2-14DR relay outputs (6-240VAC / 6-27VDC, 1A) |

---

## Motion Control System

### Axis Configuration

| Axis | Description | Motor Type | Encoder | Range | Home Position |
|:----:|:------------|:-----------|:--------|:------|:--------------|
| **X** | Left-Right | NEMA23 Stepper | Open-loop | ~400mm | X_LmtNeg (Left) |
| **Y** | Front-Back | Dual NEMA23 Stepper | Open-loop | ~400mm | Y_LmtNeg (Front) |
| **Z** | Up-Down | NEMA23 Stepper | Open-loop | ~60mm | Z_LmtPos (Top) |

### Motion Parameters (Modbus Registers)

#### X/Y Axes (Synchronized)

| Parameter | Register | Value | Unit | Description |
|:----------|:---------|:------|:-----|:------------|
| **XY_MaxVel** | DD5 | 64000 | steps/sec | Maximum velocity |
| **XY_Accel** | DD6 | 32000 | steps/sec² | Acceleration rate |
| **XY_Deccel** | DD7 | 32000 | steps/sec² | Deceleration rate |
| **XY_Steps_Per_mm** | DD8 | 160 | steps/mm | 200 steps/rev × 32 microsteps ÷ 20 teeth ÷ 2mm pitch |
| **XY_Home_Vel** | DD9 | 8000 | steps/sec | Homing velocity (slower for accuracy) |

#### Z Axis

| Parameter | Register | Value | Unit | Description |
|:----------|:---------|:------|:-----|:------------|
| **Z_MaxVel** | DD25 | 38400 | steps/sec | Maximum velocity |
| **Z_Accel** | DD26 | 51200 | steps/sec² | Acceleration rate |
| **Z_Decel** | DD27 | 51200 | steps/sec² | Deceleration rate |
| **Z_Reduced_Vel** | DD29 | 6400 | steps/sec | Reduced velocity for precision moves |
| **Z_Slow_Down_MM** | DD33 | 6 | mm | Distance before target to begin deceleration |
| **Z_Pos_Min** | DD20 | -116000 | steps | Minimum position (full down) |

### Position Tracking (Read-Only)

| Register | Nickname | Description |
|:---------|:---------|:------------|
| **DD1** | X_CurrPos | X-axis current position (steps) |
| **DD2** | X_CurrVel | X-axis current velocity (steps/sec) |
| **DD11** | Y_CurrPos | Y-axis current position (steps) |
| **DD12** | Y_CurrVel | Y-axis current velocity (steps/sec) |
| **DD21** | Z_CurrPos | Z-axis current position (steps) |
| **DD22** | Z_CurrVel | Z-axis current velocity (steps/sec) |

---

## Control Logic Overview

### Homing Sequences

Each axis has a dedicated homing routine with status feedback:

#### X-Axis Homing

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C9** (X_Home) | 16393 | Start X-axis homing sequence |
| **C1** (X_Home_Busy) | 16385 | Homing in progress |
| **C2** (X_Home_Complete) | 16386 | Homing sequence finished |
| **C3** (X_Home_Success) | 16387 | Homing successful |
| **C4** (X_Home_Error) | 16388 | Homing error occurred |
| **C13** (X_Homed) | 16397 | Axis is homed and ready |
| **DS1** (X_Home_ErrCode) | 400001 | Error code if homing fails |

#### Y-Axis Homing

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C22** (Y_Home) | 16406 | Start Y-axis homing sequence |
| **C24** (Y_Home_Busy) | 16408 | Homing in progress |
| **C25** (Y_Home_Complete) | 16409 | Homing sequence finished |
| **C26** (Y_Home_Success) | 16410 | Homing successful |
| **C27** (Y_Home_Error) | 16411 | Homing error occurred |
| **C23** (Y_Homed) | 16407 | Axis is homed and ready |
| **DS3** (Y_Home_ErrCode) | 400003 | Error code if homing fails |

#### Z-Axis Homing

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C33** (Z_Home) | 16417 | Start Z-axis homing sequence |
| **C35** (Z_Home_Busy) | 16419 | Homing in progress |
| **C36** (Z_Home_Complete) | 16420 | Homing sequence finished |
| **C37** (Z_Home_Success) | 16421 | Homing successful |
| **C38** (Z_Home_Error) | 16422 | Homing error occurred |
| **C34** (Z_Homed) | 16418 | Axis is homed and ready |
| **DS4** (Z_Home_ErrCode) | 400004 | Error code if homing fails |

#### Multi-Axis Homing

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C17** (Home_All) | 16401 | Home all three axes sequentially |
| **C18** (Home_XY) | 16402 | Home X and Y axes only |

### Motion Commands

#### XY Coordinated Move

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C10** (XY_Move) | 16394 | Execute XY move to target positions |
| **C5** (XY_Move_Busy) | 16389 | Move in progress |
| **C6** (XY_Move_Complete) | 16390 | Move finished |
| **C7** (XY_Move_Success) | 16391 | Move successful |
| **C8** (XY_Move_Error) | 16392 | Move error occurred |
| **C15** (XY_Move_User) | 16399 | User-initiated move command |
| **DD3** (X_Target) | 416389 | X-axis target position (steps) |
| **DD13** (Y_Target) | 416409 | Y-axis target position (steps) |
| **DS2** (XY_Move_ErrCode) | 400002 | Error code if move fails |

#### Z-Axis Move

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C49** (Z_Move) | 16433 | Execute Z move to target position |
| **C50** (Z_Move_Busy) | 16434 | Move in progress |
| **C51** (Z_Move_Complete) | 16435 | Move finished |
| **C52** (Z_Move_Success) | 16436 | Move successful |
| **C53** (Z_Move_Error) | 16437 | Move error occurred |
| **C54** (Z_Move_User) | 16454 | User-initiated move command |
| **DD23** (Z_Target) | 416429 | Z-axis target position (steps) |
| **DS5** (Z_Move_ErrCode) | 400005 | Error code if move fails |

#### Z-Axis Velocity Move

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C42** (Z_Vel_Move) | 16426 | Execute Z velocity-based move |
| **C43** (Z_Vel_Move_Busy) | 16427 | Move in progress |
| **C44** (Z_Vel_Move_Complete) | 16428 | Move finished |
| **C45** (Z_Vel_Move_Success) | 16429 | Move successful |
| **C46** (Z_Vel_Move_Error) | 16430 | Move error occurred |
| **DD24** (Z_Variable_Vel) | 416431 | Variable velocity setting |
| **DS6** (Z_Vel_Move_ErrCode) | 400006 | Error code if move fails |

---

## Card Handling Sequences

### Get Card Operation

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C56** (Get_Card) | 16440 | Execute card pickup sequence |
| **DS15** (Get_Card_Index) | 400015 | Position index for card pickup (default: 1) |
| **DS18** (Get_Card_Step) | 400018 | Current step in get card sequence |

**Sequence Steps:**
1. Move XY to magazine position (index-based)
2. Move Z down to card level
3. Activate vacuum (Tool_Vacuum Y105)
4. Wait for vacuum confirmation (Vacuum_Ok X025)
5. Move Z up with card
6. Return to safe position

### Put Card Operation

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C57** (Put_Card) | 16441 | Execute card placement sequence |
| **DS16** (Put_Card_Index) | 400016 | Position index for card placement (default: 10) |
| **DS19** (Put_Card_Step) | 400019 | Current step in put card sequence |
| **CT1** (Put_Counter) | Counter | Counts number of cards placed |

**Sequence Steps:**
1. Move XY to target bin position (index-based)
2. Move Z down to placement level
3. Deactivate vacuum / Activate release valve (Tool_Release Y106)
4. Wait for card to detach
5. Move Z up
6. Increment put counter

### Card Sorting Cycle

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C68** (Sort_Card_Start) | 16452 | Start automated card sorting |
| **C69** (Sort_Card_Stop) | 16453 | Stop card sorting cycle |
| **C66** (Sort_Card_Cycle) | 16450 | Sorting cycle active |
| **C67** (Sort_Card_Cycle_Allowed) | 16451 | Sorting allowed (all systems ready) |
| **DS24** (Sort_Card_Cycle_Step) | 400024 | Current step in sorting sequence |
| **DS27** (Sort_Card_Count) | 400027 | Total cards sorted (retentive) |
| **T15** (Sort_Card_Cycle_Time) | Timer | Cycle time measurement |
| **TD15** (Sort_Card_Cycle_Elapsed) | 445071 | Elapsed time in milliseconds |
| **DF20** (Sort_Card_Cycle_Average) | 428711 | Average cycle time (floating point) |

### Flipper Mechanism Control

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C71** (Flipper Goto Flipped) | 16455 | Rotate card to flipped position |
| **C72** (Flipper Goto Normal) | 16456 | Rotate card to normal position |
| **C73** (Flipper Stop) | 16457 | Stop flipper motor |
| **C75** (Flip_Cycle_Start) | 16459 | Start flip cycle |
| **C77** (Flip_Cycle) | 16461 | Flip cycle active |
| **DS23** (Flip_Cycle_Step) | 400023 | Current step in flip sequence |

**Flipper Motor Control:**
- **Y113** (Flipper RUN): Enable flipper motor
- **Y114** (Flipper FWD): Forward direction
- **Y115** (Flipper REV): Reverse direction
- **X005** (Flipper LSW Normal): Normal position sensor
- **X006** (Flipper LSW Flipped): Flipped position sensor

### Combined Operations

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C59** (Get_Put_Cycle) | 16443 | Automated get→put cycle |
| **C62** (Get_Put_Single) | 16446 | Single get→put operation |
| **DS20** (Get_Put_Cycle_Step) | 400020 | Current step in cycle |
| **DS21** (Get_Put_Cycle_Stop_Count) | 400021 | Stop after N cycles (default: 52 for full deck) |
| **DS22** (Get_Put_Single_Step) | 400022 | Current step in single operation |
| **CTD1** (Get_Put_Cycle_Count) | Counter | Number of cycles completed |

---

## Vacuum System Control

### Automatic Vacuum Management

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C64** (Vacuum_Auto) | 16448 | Auto vacuum control enabled (default: ON) |
| **C65** (Vacuum_Stats_Reset) | 16449 | Reset vacuum statistics counters |
| **C58** (Card_Attached) | 16442 | Card successfully attached to tool |
| **C70** (Sort_Card_Vacuum) | 16454 | Vacuum active during sort cycle |

### Vacuum Statistics (Retentive)

| Register | Modbus Address | Data Type | Description |
|:---------|:---------------|:----------|:------------|
| **CT10** (Vacuum_On_Count) | 149162 | Counter | Number of vacuum activations |
| **CTD10** (Vacuum_On_Seconds) | 449171 | INT2 | Total vacuum-on time (seconds) |
| **CT11** (Vacuum_Off_Count) | 149163 | Counter | Number of vacuum deactivations |
| **CTD11** (Vacuum_Off_Seconds) | 449173 | INT2 | Total vacuum-off time (seconds) |
| **DF16** (Vacuum_DC) | 428711 | FLOAT | Vacuum duty cycle (percentage) |

### Vacuum Control Outputs

| Output | Modbus Address | Function |
|:-------|:---------------|:---------|
| **Y104** (Vacuum_Pump) | 8228 | Main vacuum pump (24V diaphragm) |
| **Y105** (Tool_Vacuum) | 8229 | Tool suction cup vacuum valve |
| **Y106** (Tool_Release) | 8230 | Tool suction cup release valve |
| **Y107** (Flipper_Vacuum) | 8231 | Flipper suction cup vacuum valve |
| **Y108** (Flipper_Release) | 8232 | Flipper suction cup release valve |

### Vacuum Timers

| Timer | Modbus Address | Function |
|:------|:---------------|:---------|
| **T6** (Card_Suction_Delay) | 145062 | Delay after vacuum activation |
| **T7** (Extra_Card_Delay) | 145063 | Extra delay for stubborn cards |
| **T11** (Tool Vacuum Delay) | 145067 | Tool vacuum valve delay |
| **T12** (Tool Release Delay) | 145068 | Tool release valve delay |
| **T13** (Flipper Vacuum Delay) | 145069 | Flipper vacuum valve delay |
| **T14** (Flipper Release Delay) | 145070 | Flipper release valve delay |

---

## Position Index System

The PLC uses index-based positioning to store frequently used coordinates:

### Position Index Registers

| Register | Modbus Address | Default | Description |
|:---------|:---------------|:--------|:------------|
| **DS11** (X_Position_Index) | 400011 | 100 | Base index for X positions |
| **DS12** (Y_Position_Index) | 400012 | 200 | Base index for Y positions |
| **DS13** (Z_Position_Index) | 400013 | 300 | Base index for Z positions |
| **DS25** (Magazine_Bin_Index) | 400025 | 1 | Magazine pickup location |
| **DS26** (Sort_Bin_Index) | 400026 | 9999 | Current sort bin destination |

### Dynamic Position Registers

| Register | Modbus Address | Function |
|:---------|:---------------|:---------|
| **DD100** (X_Dynamic) | 416583 | X-axis dynamic position storage |
| **DD200** (Y_Dynamic) | 416783 | Y-axis dynamic position storage |
| **DD300** (Z_Dynamic) | 416983 | Z-axis dynamic position storage |

**Usage Pattern:**
- Index 1-13: Magazine positions (pickup locations)
- Index 10-62: Sort bin positions (placement locations)
- Each index corresponds to a stored XY coordinate pair
- Z positions vary based on card stack height

---

## Safety & Emergency Systems

### Emergency Stop

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C30** (EStop_Asserted) | 16414 | Emergency stop button pressed |

**E-Stop Behavior:**
- Immediately stops all motion
- Disables stepper motor drivers
- Deactivates vacuum system
- Requires system reset and re-homing

### System Status Flags

| Control Bit | Modbus Address | Function |
|:------------|:---------------|:---------|
| **C14** (Hold) | 16398 | System hold state (retentive) |
| **C61** (Bin_Empty) | 16445 | Magazine bin empty indicator |
| **C60** (Dummy) | 16444 | Test/debug flag |

---

## Communication & Diagnostics

### Heartbeat Monitoring

| Register | Modbus Address | Function |
|:---------|:---------------|:---------|
| **C21** (Comms_HeartBeat) | 16405 | SCADA heartbeat signal |
| **T1** (Comms_Timer) | 145057 | Communication timeout timer |
| **TD1** (Comms_Timer_Max_Elapsed) | 445057 | Max elapsed time since last heartbeat |
| **DS30** (Comms_Timer_Max) | 400030 | Heartbeat timeout threshold |

**Function:**
- Node-RED toggles C21 periodically
- PLC monitors toggle rate
- If timeout exceeded, PLC enters safe state

### System Clocks

| Special Bit | Modbus Address | Frequency |
|:------------|:---------------|:----------|
| **SC7** (_1sec_Clock) | 161447 | 1 Hz |

Used for timing operations and heartbeat monitoring.

---

## Modbus TCP Communication

### Modbus Function Codes

| Function Code | Operation | Usage |
|:--------------|:----------|:------|
| **FC=01** | Read Coils | Read output states |
| **FC=02** | Read Discrete Inputs | Read input and timer states |
| **FC=03** | Read Holding Registers | Read data registers |
| **FC=05** | Write Single Coil | Write single output |
| **FC=06** | Write Single Register | Write single data register |
| **FC=15** | Write Multiple Coils | Write multiple outputs |
| **FC=16** | Write Multiple Registers | Write multiple data registers |

### Modbus Address Mapping

| Data Type | Address Range | Modbus Address | Example |
|:----------|:--------------|:---------------|:--------|
| **Inputs (X)** | X001-X032 | 100001-100032 | X001 → 100001 |
| **Outputs (Y)** | Y001-Y256 | 8193-8448 | Y001 → 8193 |
| **Control Relays (C)** | C1-C2000 | 16385-18384 | C1 → 16385 |
| **Timers (T)** | T1-T500 | 145057-145556 | T1 → 145057 |
| **Counters (CT)** | CT1-CT250 | 149153-149402 | CT1 → 149153 |
| **Data Registers (DS)** | DS1-DS4500 | 400001-404500 | DS1 → 400001 |
| **Double Registers (DD)** | DD1-DD2000 | 416385-420384 | DD1 → 416385 (2 words) |
| **Float Registers (DF)** | DF1-DF500 | 428671-429670 | DF16 → 428703 (2 words) |
| **Timer Data (TD)** | T1-T500 | 445057-445556 | TD1 → 445057 |
| **Counter Data (CTD)** | CT1-CT250 | 449153-449651 | CTD1 → 449153 (2 words) |

### Key Registers for SCADA Integration

#### Motion Status (Read-Only)
```
DD1  (416385) - X_CurrPos
DD2  (416387) - X_CurrVel
DD11 (416405) - Y_CurrPos
DD12 (416407) - Y_CurrVel
DD21 (416425) - Z_CurrPos
DD22 (416427) - Z_CurrVel
```

#### Motion Commands (Write)
```
C10  (16394)  - XY_Move trigger
C49  (16433)  - Z_Move trigger
DD3  (416389) - X_Target position
DD13 (416409) - Y_Target position
DD23 (416429) - Z_Target position
```

#### Card Operations (Write)
```
C68  (16452)  - Sort_Card_Start
C69  (16453)  - Sort_Card_Stop
DS26 (400026) - Sort_Bin_Index
```

#### System Status (Read)
```
C13  (16397)  - X_Homed
C23  (16407)  - Y_Homed
C34  (16418)  - Z_Homed
C30  (16414)  - EStop_Asserted
C58  (16442)  - Card_Attached
DS27 (400027) - Sort_Card_Count
```

---

## Program Structure

### Main Program Components

Based on the loader file structure:

| Component | Size | Description |
|:----------|:-----|:------------|
| **BIN** | 18 KB | Compiled ladder logic binary |
| **BIN.MN** | 7 KB | Memory map |
| **BIN.PA** | 120 KB | Program addresses and cross-references |
| **BIN.TA** | 36 KB | Tag/nickname database |
| **FW/** | 2.7 MB | PLC firmware files |
| **Setting.ini** | 261 bytes | Configuration parameters |

### Estimated Program Size

- **Ladder Logic**: ~18 KB compiled code
- **Tags/Nicknames**: ~180 unique addresses
- **Timers**: 20 active timers
- **Counters**: 3 counters (1 regular, 2 retentive)
- **Subroutines**: Multiple motion control, homing, and card handling routines

---

## Backup and Version Control

### Loader File Information

**File**: XYZT2_V56.cklx
**Type**: Click PLC Loader File
**Contents**:
- Complete program binary
- Tag database
- I/O configuration
- Firmware (optional)
- Slot configurations (Node-RED, OPC-UA ready)

**Recommended Backup Strategy**:
1. Export .cklx file after each major program change
2. Export Modbus address map as CSV
3. Export nickname database as CSV
4. Store in version control (Git)
5. Include date/version in filename

---

## Troubleshooting

### Common Issues

| Symptom | Possible Cause | Check Register |
|:--------|:--------------|:---------------|
| Axis won't home | Limit switch not detected | X001, X002, X003 |
| Motion error | Target out of range | DS1-DS6 (error codes) |
| Vacuum not holding | Pressure too low | X025 (Vacuum_Ok) |
| Card not detected | Sensor alignment | X022 (Tool_Card_Detect) |
| Communication timeout | Heartbeat not toggling | C21, TD1 |
| E-Stop active | Button pressed or wiring | C30 (EStop_Asserted) |

### Error Code Registers

| Register | Modbus | Function |
|:---------|:-------|:---------|
| **DS1** | 400001 | X_Home error code |
| **DS2** | 400002 | XY_Move error code |
| **DS3** | 400003 | Y_Home error code |
| **DS4** | 400004 | Z_Home error code |
| **DS5** | 400005 | Z_Move error code |
| **DS6** | 400006 | Z_Vel_Move error code |

---

## Performance Metrics

### Typical Operating Parameters

| Parameter | Value | Notes |
|:----------|:------|:------|
| **XY Move Speed** | 400 mm/sec | At maximum velocity setting |
| **XY Acceleration** | 200 mm/sec² | Calculated from steps and conversion |
| **Z Move Speed** | 240 mm/sec | At maximum velocity setting |
| **Homing Speed** | 50 mm/sec | Reduced for accuracy |
| **Position Accuracy** | ±0.2 mm | Based on microstep resolution |
| **Vacuum Response** | ~500 ms | Time to reach operational vacuum |

### Cycle Time Tracking

The PLC tracks cycle times for performance monitoring:

- **T15** (Sort_Card_Cycle_Time): Active timer during sorting
- **TD15** (Sort_Card_Cycle_Elapsed): Elapsed time in ms
- **DF20** (Sort_Card_Cycle_Average): Rolling average cycle time
- **DS27** (Sort_Card_Count): Total cards sorted (persistent)

**Target Performance**: 14-20 seconds per card

---

## Future Expansion

### Available Resources

| Resource | Used | Available | Notes |
|:---------|:-----|:----------|:------|
| **Inputs** | 9 | 15 | C2-14D2, C2-14DR modules |
| **Relay Outputs** | 1 | 5 | C2-14DR module |
| **DC Outputs** | 15 | 7 | C0-16TD1, C2-14D2 modules |
| **Control Relays** | ~77 | 1923 | C1-C2000 range |
| **Data Registers** | ~30 | 4470 | DS1-DS4500 range |
| **Timers** | 20 | 480 | T1-T500 range |
| **Counters** | 3 | 247 | CT1-CT250 range |

### Expansion Slot Capabilities

- **Slot 0**: Available for option modules (Analog I/O, Serial, etc.)
- **Slot 1**: Available for option modules
- **Node-RED**: Folder structure ready (SLOT0/NRED, SLOT1/NRED)
- **OPC-UA**: Folder structure ready (SLOT0/OPCUA, SLOT1/OPCUA)

---

## Appendix: Quick Reference

### Critical Start/Stop Commands

```
Home All Axes:     C17 (16401) = ON
Start Card Sort:   C68 (16452) = ON
Stop Card Sort:    C69 (16453) = ON
Emergency Stop:    Hardware E-Stop button
```

### Most Used Modbus Addresses

```
Motion Status:     DD1, DD11, DD21 (Current positions)
Motion Commands:   C10, C49 (Move commands)
Homing Status:     C13, C23, C34 (Homed flags)
Card Count:        DS27 (400027)
Sort Bin:          DS26 (400026)
Vacuum Status:     X025 (100021)
```

---

*This documentation was generated from PLC program XYZT2_V56 exported on 2026-04-22*
