# 1. Overview

AC charging of an electric car uses the **public low-voltage network** and an **onboard charger** in the vehicle. The wallbox (EVSE) is not a charger in the power-electronics sense: it is a controlled, protected connection that tells the car how much AC current it may draw.

Worldwide, almost every home AC installation falls into one of a few **grid families**:

| Family | Nominal voltages | Frequency | Typical home AC power |
| --- | --- | --- | --- |
| IEC 230/400 V wye | 230 V L–N, 400 V L–L | 50 Hz (60 Hz in Saudi Arabia) | 3.7 / 7.4 kW (1φ) or 11 / 22 kW (3φ) |
| Legacy 220/380 V wye | 220 V L–N, 380 V L–L | 50 Hz | same, slightly lower kW |
| North American split-phase | 120 / 240 V | 60 Hz | 1.4 kW (Level 1) or 7.7–11.5 kW (Level 2) |
| Japan 100/200 V | 100 V / 200 V | 50 Hz east, 60 Hz west | ~3–6 kW on 200 V |
| 230 V IT (Norway) | 230 V L–L, often no N | 50 Hz | 3.7–7.4 kW 1φ; ~11 kW 3φ only if the car allows it |

**22 kW** (400 V three-phase 32 A) is the practical upper bound of this overview. It is a home option only where three-phase service and the main fuse allow it. Many vehicles’ onboard chargers stop at **11 kW**.

Four questions decide a home installation:

1. **What voltage and how many phases** does the dwelling actually have?
2. **Which earthing system** (TN-S, TN-C-S/PME, TT, IT)?
3. **Which vehicle inlet** (Type 2, Type 1/J1772, NACS, GB/T AC)?
4. **Which national installation rules** apply (RCD type, open-PEN, dedicated circuit, notification of the DSO)?

The interactive `index.html` answers these by region and country.
