# Hardware Overview

## 3-Axis Gantry

| Assembled Configuration | Component Identification |
|-------------------------|--------------------------|
| ![3-Axis Platform - Assembled View](image/hardware_images/3-axis_overview.png)<br><br>The complete assembly showing the XYZ gantry system with dual Y-axis motors and aluminum extrusion frame construction. | ![3-Axis Platform - Exploded View](image/hardware_images/3-axis_explosion.png)<br><br>Exploded view highlighting key mechanical and electronic components. |


**Key Components:**

| Component | Description | Function |
|-----------|-------------|----------|
| **X-Axis** | Horizontal gantry carriage with stepper motor | Left-right motion control |
| **Y-Axis (1)** | Left-side rail motor assembly | Front-back motion (dual motor synchronization) |
| **Y-Axis (2)** | Right-side rail motor assembly | Front-back motion (dual motor synchronization) |
| **Z-Axis** | Vertical spindle/tool carriage | Up-down motion control |
| **USB CAM** | Integrated camera module | Visual positioning and alignment |
| **Limit Switch** | End-stop position sensor | Axis homing and travel limits |
| **Photoelectric Sensor** | Workpiece detection/homing | Z-axis probing and workpiece detection |
| **Suction Cup** | Workpiece holding fixture | Part retention during operations |


---

## Enclosure Configurations

| Configuration | Image | Description |
|---------------|-------|-------------|
| **1. Folding Frame Assembly**<br>(Transportation Mode) | ![Enclosure - Folding Configuration](image/hardware_images/Assembly_fold.png) | Two-tier enclosure design with collapsible upper section for compact storage or transport. The folding mechanism allows the top frame to nest with the base. |
| **2. Vertical Frame Assembly**<br>(Operational Mode) | ![Enclosure - Vertical Configuration](image/hardware_images/Assembly_vertical.png) | Standard vertical enclosure configuration providing full working envelope access while protecting the motion platform. |

---

## Technical Specifications
### Motion System
| Axis | Travel (mm) | Motor Type | Drive System |
|------|-------------|------------|--------------|
| X    | TBD         | NEMA 17/23 | Belt/Lead Screw |
| Y    | TBD         | NEMA 17/23 (Dual) | Belt/Lead Screw |
| Z    | TBD         | NEMA 17/23 | Lead Screw |
