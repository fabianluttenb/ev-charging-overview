# 4. Standards landscape

Think in **layers**. A home wallbox sits on all of them at once.

```
ISO 15118 / PWM          optional digital communication
IEC 62196-2 / J1772 …    coupler dimensions and pins
IEC 61851-1 / J1772      charging modes, control pilot, EVSE behaviour
IEC 62752 / UL 2231      Mode 2 IC-CPD or NA personnel protection
IEC 60364-7-722 / NEC 625 / BS 7671:722   installation (circuit, RCD, earthing)
IEC 60364 / NEC / AS/NZS 3000             building wiring and earthing system
IEC 60038 / EN 50160 / ANSI C84.1         what the public LV network actually is
```

## IEC 61851-1 charging modes

| Mode | What it is | Home charging station? |
| --- | --- | --- |
| **1** | Cable, no EVSE, no pilot, ≤ 16 A | No. Banned or restricted in UK, US, IL, and several others |
| **2** | Portable EVSE with **IC-CPD** (IEC 62752) in the cable | Temporary / travel. Household plug thermally limited |
| **3** | Dedicated EVSE, pilot PWM, tethered cable or Type 2 socket | **Yes — this is a home charging station** |
| **4** | DC, off-board charger | Out of AC scope |

SAE language: **AC Level 1** = 120 V, **AC Level 2** = 208–240 V (and, on commercial 480Y, 277 V if the EVSE is listed for it). Level 2 corresponds to Mode 3 (or a 240 V Mode 2 portable). NEC 625 also lists 480Y/277, 480, 600Y/347, and 600 as AC system voltages.

## Control pilot (every Mode 2/3 session)

The EVSE puts a ±12 V 1 kHz square wave on CP. Duty cycle announces **maximum available current**. The vehicle never requests more than that, and never more than the onboard charger.

- 10–85 % duty ≈ I = duty × 0.6 A (example: 53 % ≈ 32 A)
- 5 % duty = “use digital communication” (ISO 15118)

Proximity (PP / CS): confirms connector insertion and, on Type 2, codes the **cable’s** current rating with a resistor to PE (20 A / 32 A / 63 A / 70 A).

## Installation (IEC 60364-7-722 and national clones)

Shared core:

- One dedicated circuit per connecting point
- No PEN on that circuit
- 30 mA RCD on all live conductors
- DC residual: Type B **or** Type A/F + 6 mA RDC-DD (IEC 62955)

National extras that change home design:

| Country / region | Extra |
| --- | --- |
| UK / Ireland | Open-PEN protection on PME for outdoor points (BS 7671 722.411.4.1) |
| Germany | VDE-AR-N 4100: notify DSO from 3.6 kW; 11 kW typical; 22 kW often needs permission |
| France | TT + NF C 15-100; Linky tariff / subscribed power |
| USA / Canada | NEC/CEC 125 % continuous-load sizing; GFCI / UL 2231 CCID |
| Norway | 230 V IT vs 400 V TN — vehicle compatibility |
| Australia / NZ | MEN earthing; Type 2; demand-response (AS/NZS 4755) in some networks |
| China | GB/T 18487 + 20234.2 gender-reversed AC coupler |

## Connector standards (AC)

| Coupler | Standard | Phases | Home regions |
| --- | --- | --- | --- |
| Type 2 | IEC 62196-2 | 1 and 3 | Europe, UK, AU/NZ, ME, Africa, India 4W |
| Type 1 | IEC 62196-2 = SAE J1772 | 1 | USA, CA, JP, KR, TW |
| NACS | SAE J3400 | 1 (AC) | North America (transition) |
| GB/T AC | GB/T 20234.2 | 1 and 3 | China |
| Type 3 | IEC 62196-2 | 1 and 3 | Legacy IT/FR — do not use new |
