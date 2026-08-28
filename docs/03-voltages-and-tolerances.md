# 3. Voltages and tolerances

## Harmonised IEC voltages

IEC 60038 replaced the old 220/380 V and 240/415 V targets with **230/400 V**. Equipment is specified around 230 V ±10 %. Many countries still **name** 220 V or 240 V on paper; the product is in the same family.

| Quantity | IEC 230/400 V wye | NA split-phase | NA 208Y/120 | NA 480Y/277 | Japan | Norway IT |
| --- | --- | --- | --- | --- | --- | --- |
| L–N | 230 V | 120 V | 120 V | **277 V** | 100 V | — (often no N) |
| L–L | 400 V | 240 V | 208 V | 480 V | 200 V | 230 V |
| Frequency | 50 Hz (SA: 60 Hz) | 60 Hz | 60 Hz | 60 Hz | 50 / 60 Hz | 50 Hz |
| Typical site | Most of world | US/CA houses | Apartments, small commercial | Large commercial / industrial | Japan | Norway LV |

**277 V is not a US region and not a house voltage.** It is the phase-to-neutral of a **480Y/277 V** wye, used nationwide for commercial lighting and some workplace EVSE. Canada’s analogue is **600Y/347 V**. See [North America corner cases](09-north-america-corner-cases.md).

## Supply-voltage tolerance

### Europe — EN 50160

At the **supply terminals**, under normal conditions, excluding interruptions:

- 95 % of the 10-minute mean r.m.s. values in any week: **Un ± 10 %**
- 100 % of those 10-minute values: **+10 % / −15 %**
- Isolated / remote networks: **+10 % / −15 %** as the normal band

For Un = 230 V that is **207–253 V** (95 % band) and down to **195.5 V** for every 10-minute value.

UK historical declaration after 230 V harmonisation: **230 V +10 % / −6 %** (216.2–253 V). Design EVSE for the full EN 50160 band.

Frequency (interconnected 50 Hz systems): 50 Hz ±1 % (49.5–50.5 Hz) during 99.5 % of a year; 47–52 Hz as the wider band.

### North America — ANSI C84.1

| | Range A (normal) | Range B (limited duration) |
| --- | --- | --- |
| Service voltage | ±5 % (114–126 V, 228–252 V) | +6 % / −8.3 % |
| Utilization voltage | +5 % / −10 % (108–126 V) | +5.8 % / −13.3 % |

Service voltage is at the meter; utilization voltage is at the equipment after building drop. The same ±5 % Range A band applies to 208 V, 240 V, 277 V, and 480 V service voltages.

### China — GB/T 12325

- 220 V single-phase: **+7 % / −10 %** (198–235.4 V)
- 380 V three-phase: **±7 %**
- Remote areas: wider exceptions

### Japan

100 V class typically **101 ± 6 V**. 200 V class is derived from the same transformers (two 100 V legs). Frequency is a hard regional split (50 Hz east of the Fujigawa, 60 Hz west), but EV onboard chargers are universal 50/60 Hz.

### Australia / New Zealand

Nominal 230 V. NZ widened the statutory band to **±10 %** in 2025 (previously ±6 %). Australia is in the same IEC 60038 family; Western Australia still often quoted as 240 V.

## Why tolerance matters for 22 kW-class charging

Power is proportional to voltage. A 32 A single-phase wallbox:

| Voltage | Power |
| --- | --- |
| 207 V (−10 %) | 6.6 kW |
| 230 V | 7.4 kW |
| 253 V (+10 %) | 8.1 kW |

Three-phase 32 A:

| U_LL | Power |
| --- | --- |
| 360 V | 20.0 kW |
| 400 V | 22.2 kW |
| 440 V | 24.4 kW |

The nameplate “22 kW” is a **nominal**. The vehicle and EVSE must remain within current limits; they do not hold constant power if the mains sag.
