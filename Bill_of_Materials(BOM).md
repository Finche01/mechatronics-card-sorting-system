# Bill of Materials (BOM)

[← Back to Main README](README.md)

Complete parts list for the Mechatronics Card Sorting System.
1
---

## 📦 Complete Parts List

### Summary

| Category | Items | Estimated Cost |
|----------|-------|----------------|
| Mechanical Components | 20 | $350 - $450 |
| Electronics & Control | 15 | $400 - $600 |
| Pneumatics | 6 | $150 - $200 |
| Fasteners & Hardware | - | $50 - $80 |
| **Total** | **41+** | **$950 - $1,330** |

---

## 🔩 Mechanical Components

| # | Component | Specification | Qty | Unit Price | Total | Supplier | Notes |
|---|-----------|--------------|-----|------------|-------|----------|-------|
| 1 | Linear Rail | 20x20mm, 1000mm length | 3 | $25 | $75 | Amazon/AliExpress | For X, Y, Z axes |
| 2 | Linear Bearing | LM20UU | 12 | $3 | $36 | Amazon | 4 per axis |
| 3 | Lead Screw | 8mm diameter, 2mm pitch, 1000mm | 3 | $15 | $45 | Amazon | With brass nut |
| 4 | Flexible Coupler | 8mm to 6.35mm | 3 | $5 | $15 | Amazon | Motor to lead screw |
| 5 | Aluminum Extrusion | 2020 profile, various lengths | 6m | $3/m | $18 | Local/Online | Frame material |
| 6 | Corner Brackets | 2020 L-bracket | 16 | $1 | $16 | Amazon | Frame corners |
| 7 | T-Slot Nuts | M5 | 100 | $0.10 | $10 | Amazon | Assorted pack |
| 8 | Motor Mount Plate | Aluminum, NEMA 23 | 3 | $8 | $24 | Amazon | Custom or pre-made |
| 9 | Carriage Plate | Aluminum, custom cut | 3 | $12 | $36 | Local machine shop | 150x100mm |
| 10 | Gripper Mount | Aluminum bracket | 1 | $10 | $10 | Custom fabrication | - |

**Mechanical Subtotal: $285 - $350**

---

## ⚡ Electronics & Control

| # | Component | Specification | Qty | Unit Price | Total | Supplier | Notes |
|---|-----------|--------------|-----|------------|-------|----------|-------|
| 11 | Stepper Motor | NEMA 23, 2.8A, 1.8° | 3 | $25 | $75 | StepperOnline | High torque |
| 12 | Stepper Driver | TB6600, 4.5A | 3 | $12 | $36 | Amazon | Microstep capable |
| 13 | PLC Controller | Siemens S7-1200 | 1 | $250 | $250 | Automation Direct | Or equivalent |
| 13b | PLC Controller (Alt) | Arduino Mega + CNC Shield | 1 | $45 | $45 | Amazon | Budget alternative |
| 14 | Power Supply | 24V DC, 15A | 1 | $35 | $35 | Amazon | 360W minimum |
| 15 | USB Camera | 1080p, 60fps, USB 3.0 | 1 | $45 | $45 | Logitech/Amazon | C920 or similar |
| 16 | Limit Switch | Mechanical, SPDT | 6 | $2 | $12 | Amazon | 2 per axis |
| 17 | Emergency Stop Button | Twist-release, NC contact | 1 | $8 | $8 | Amazon | Red mushroom head |
| 18 | DIN Rail | 35mm, 1 meter | 1 | $8 | $8 | Amazon | For mounting |
| 19 | Terminal Blocks | 10-position | 5 | $3 | $15 | Amazon | Wire organization |
| 20 | Power Distribution | Fuse block, 6-circuit | 1 | $12 | $12 | Amazon | With fuses |
| 21 | Control Enclosure | IP65, 300x400x200mm | 1 | $40 | $40 | Amazon | Weatherproof |

**Electronics Subtotal: $386 - $536**

---

## 💨 Pneumatics

| # | Component | Specification | Qty | Unit Price | Total | Supplier | Notes |
|---|-----------|--------------|-----|------------|-------|----------|-------|
| 22 | Pneumatic Gripper | 2-jaw parallel, 10mm stroke | 1 | $35 | $35 | Amazon/McMaster | MHZ2 series |
| 23 | Solenoid Valve | 5/2-way, 24V DC | 1 | $15 | $15 | Amazon | Pneumatic control |
| 24 | Air Compressor | 6 bar, 50L tank | 1 | $120 | $120 | Local/Harbor Freight | Or shop air |
| 25 | Pressure Regulator | 0-10 bar, with gauge | 1 | $15 | $15 | Amazon | Inline |
| 26 | Pneumatic Tubing | 6mm OD, 10m | 1 | $12 | $12 | Amazon | Polyurethane |
| 27 | Quick Connect Fittings | 6mm push-to-connect | 10 | $1 | $10 | Amazon | Various types |

**Pneumatics Subtotal: $207**

---

## 🔌 Wiring & Connectors

| # | Component | Specification | Qty | Unit Price | Total | Supplier | Notes |
|---|-----------|--------------|-----|------------|-------|----------|-------|
| 28 | Power Cable | 18 AWG, stranded | 20m | $0.50/m | $10 | Amazon | Black/Red pair |
| 29 | Signal Cable | 22 AWG, 4-conductor | 15m | $0.80/m | $12 | Amazon | Shielded |
| 30 | Ethernet Cable | Cat6, 5m | 2 | $5 | $10 | Amazon | PLC connection |
| 31 | USB Cable | USB 3.0, 3m | 1 | $8 | $8 | Amazon | Camera cable |
| 32 | Cable Glands | PG13.5, various | 10 | $1 | $10 | Amazon | Enclosure entry |
| 33 | Cable Ties | Various sizes, 500pc | 1 | $8 | $8 | Amazon | Organization |
| 34 | Ferrules | Bootlace, assorted | 200 | $10 | $10 | Amazon | Wire termination |
| 35 | Heat Shrink Tubing | Assorted kit | 1 | $12 | $12 | Amazon | Protection |

**Wiring Subtotal: $80**

---

## 🔧 Fasteners & Hardware

| # | Component | Specification | Qty | Supplier | Notes |
|---|-----------|--------------|-----|----------|-------|
| 36 | M5 Bolts | Various lengths, 100pc | 1 | Amazon | Frame assembly |
| 37 | M4 Bolts | Various lengths, 100pc | 1 | Amazon | Motor mounting |
| 38 | M3 Bolts | Various lengths, 50pc | 1 | Amazon | Electronics |
| 39 | Washers | M3, M4, M5 assorted | 1 | Amazon | 200pc kit |
| 40 | Lock Washers | M3, M4, M5 assorted | 1 | Amazon | 100pc kit |
| 41 | Nylock Nuts | M3, M4, M5 assorted | 1 | Amazon | 150pc kit |

**Fasteners Subtotal: $50 - $80** (depends on existing stock)

---

## 🎨 Optional Components

| # | Component | Specification | Unit Price | Purpose |
|---|-----------|--------------|------------|---------|
| 42 | LED Strip Lighting | White, 12V, 2m | $15 | Better card imaging |
| 43 | Touch Screen | 7" HMI display | $80 | Alternative interface |
| 44 | Cooling Fan | 120mm, 24V | $12 | Enclosure cooling |
| 45 | Status Light Tower | Red/Yellow/Green | $35 | Visual status |
| 46 | Buzzer | 24V, 85dB | $5 | Audio alerts |
| 47 | Card Feeder Mechanism | Custom design | $50 | Automated loading |
| 48 | RFID Reader | USB, 13.56MHz | $25 | Card tracking |

**Optional Subtotal: $222**

---

[← Back to Main README](README.md)
