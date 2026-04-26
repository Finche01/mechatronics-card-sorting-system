# PLC Control System Overview

The Programmable Logic Controller (PLC) serves as the central control unit of the Card Sorting System. It manages motion control, sequencing, sensor integration, and communication with external systems to ensure reliable and coordinated operation.

| Category              | Details                          |
|----------------------|----------------------------------|
| Programming Software | CLICK PLC Programming Software   |
| Language Used        | Ladder Logic                     |
| Communication        | Modbus TCP                       |
| Features Used        | Timers, counters, indexing, function calls |

---

## Program Sequence
<table>
  <tr>
    <td align="center">
      <strong>Initialization</strong><br>
      <img src="image/sequential_diagram_initialization.png" width="100%">
    </td>
    <td align="center">
      <strong>Sort_Ranks</strong><br>
      <img src="image/sequential_diagram_ranks.png" width="100%">
    </td>
  </tr>
</table>