# 2. Earthing concepts (IEC 60364)

IEC 60364 classifies LV earthing with two or three letters.

| Letter | Position | Meaning |
| --- | --- | --- |
| **T** | 1st | Source star point (or other point) is **directly earthed** |
| **I** | 1st | Source is **isolated** or earthed through a **high impedance** |
| **N** | 2nd | Installation exposed-conductive-parts are earthed via the **source earth** (PE from the utility) |
| **T** | 2nd | Installation exposed-conductive-parts have a **local, independent** earth electrode |
| **S** | 3rd | PE and N are **separate** |
| **C** | 3rd | PE and N are **combined** as PEN |

## The five arrangements

### TN-S

PE and N are separate from the transformer. Best EMC and no open-PEN hazard. Common in industrial buildings and some older city networks.

### TN-C

PEN all the way to the load. RCDs cannot be used on PEN. **Not permitted** as the final circuit to an EV connecting point.

### TN-C-S (PME / MEN / multi-grounded neutral)

PEN on the street, split into PE and N at the origin of the installation. This is the world’s default residential system (UK PME, AU/NZ MEN, German TN, North American MGN).

**EV issue:** if the utility PEN breaks, the PE of the installation (and therefore the car body, via the charging cable) can rise toward line potential relative to true earth. A person standing on the ground touching the car can be shocked.

UK BS 7671 722.411.4.1 therefore forbids using PME as the earth of an **outdoor** charging point unless extra measures are applied:

- electrical separation, or
- a local earth electrode with proven resistance, or
- an **open-PEN** device that disconnects live conductors **and PE** if PE-to-earth voltage exceeds **70 V rms** (within 5 s; faster at higher voltages), or
- a three-phase installation whose load balance keeps the PE-earth voltage ≤ 70 V on an open PEN.

IEC 60364-7-722 additionally: the **EV circuit itself shall not contain a PEN conductor**. After the main earthing terminal the run to the wallbox is always TN-S (separate PE).

### TT

Utility provides N (and its own earth at the transformer). The house PE is a **local electrode**. Earth-fault current is small (soil path), so **RCDs are the primary disconnection means**. Dominant in France, Italy, Spain, Japan, and much of Africa and South Asia. For EV this is straightforward: the 30 mA RCD already required for the connecting point is also the earth-fault device.

### IT

Source isolated (or impedance-earthed). First fault does not trip; an insulation monitor alarms. Norway still operates **~70 % of LV as 230 V IT**: three lines at 230 V to each other, **often no neutral**. Charging then looks like 230 V single-phase between two lines, or 230 V three-phase delta. Many onboard chargers were designed for 230 V L–N / 400 V L–L and will only use two wires on IT.

## Rules that always apply to AC EVSE (IEC 60364-7-722)

- Dedicated circuit per connecting point.
- No PEN on that circuit.
- RCD IΔn ≤ 30 mA, disconnecting **all live conductors**.
- Smooth-DC residual protection: **RCD Type B**, or **Type A/F + RDC-DD (IEC 62955, 6 mA DC)**.
- Non-conducting location and earth-free local bonding shall not be used.
