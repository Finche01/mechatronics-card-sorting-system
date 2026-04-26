# PLC Control System Overview

The Programmable Logic Controller (PLC) serves as the central control unit of the Card Sorting System. It manages motion control, sequencing, sensor integration, and communication with external systems to ensure reliable and coordinated operation.

| Category              | Details                          |
|----------------------|----------------------------------|
| Programming Software | CLICK PLC Programming Software   |
| Language Used        | Ladder Logic                     |
| Communication        | Modbus TCP                       |
| Features Used        | Timers, counters, indexing, function calls |

### PLC I/O Mapping Summary

| Type   | Address | Tag Name                  | Function / Description                     |
|--------|---------|---------------------------|--------------------------------------------|
| INPUT  | X001    | X_LmtNeg                  | X-axis negative limit switch               |
| INPUT  | X002    | Y_LmtNeg                  | Y-axis negative limit switch               |
| INPUT  | X003    | Z_LmtPos                  | Z-axis positive limit switch               |
| INPUT  | X004    | Motor_Enable_Feedback     | Motor driver enable feedback               |
| INPUT  | X005    | Flipper_LSW_Normal        | Flipper in normal position                 |
| INPUT  | X006    | Flipper_LSW_Flipped       | Flipper in flipped position                |
| INPUT  | X021    | Tool_Compression          | Tool compression sensor (card contact)     |
| INPUT  | X022    | Tool_Card_Detect          | Card presence detection                    |
| INPUT  | X025    | Vacuum_Ok                 | Vacuum pressure confirmation               |

| Type   | Address | Tag Name                  | Function / Description                     |
|--------|---------|---------------------------|--------------------------------------------|
|OUTPUT | Y001–Y006 | X/Y/Z Pulse & Direction | Stepper motor control signals for X, Y, Z axes
| OUTPUT | Y026    | Main_Cage_LED             | System status lighting                     |
| OUTPUT | Y101    | Motor_Disable             | Motor disable control                      |
| OUTPUT | Y102    | Vision_LED                | Illumination for camera                    |
| OUTPUT | Y104    | Vacuum_Pump               | Vacuum pump activation                     |
| OUTPUT | Y105    | Tool_Vacuum               | Suction cup enable                         |
| OUTPUT | Y106    | Tool_Release              | Release suction                            |
| OUTPUT | Y107    | Flipper_Vacuum            | Flipper suction enable                     |
| OUTPUT | Y108    | Flipper_Release           | Flipper suction release                    |
| OUTPUT | Y113    | Flipper_RUN               | Flipper motor enable                       |
| OUTPUT | Y114    | Flipper_FWD               | Flipper forward direction                  |
| OUTPUT | Y115    | Flipper_REV               | Flipper reverse direction                  |

---

## Program Sequence
<table>
  <tr>
    <td align="center"><strong>Initialization</strong></td>
    <td align="center"><strong>Sort Ranks</strong></td>
  </tr>
  <tr>
    <td align="center">
      <img src="image/sequential_diagram_initialization.png" width="100%">
    </td>
    <td align="center">
      <img src="image/sequential_diagram_ranks.png" width="100%">
    </td>
  </tr>
</table>