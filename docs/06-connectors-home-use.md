# 6. Connectors for home AC charging

Three different plugs appear in a home installation. Mixing them up is the usual source of confusion.

```
Grid / consumer unit  --(A)--  EVSE wallbox  --(B)--  cable  --(C)--  vehicle inlet
```

| Interface | Role | Typical home choice |
| --- | --- | --- |
| **A** | Supply of the EVSE | Hardwired dedicated circuit; or NEMA 14-50 / IEC 60309 |
| **B** | Station front | Tethered vehicle connector, **or** Type 2 socket (untethered) |
| **C** | Vehicle | Type 2, Type 1/J1772, NACS, or GB/T AC — **fixed by the car** |

## C — Vehicle inlet (cannot be chosen freely)

### Type 2 (IEC 62196-2) — default outside NA/JP/CN

Seven pins: L1, L2, L3, N, PE, CP, PP. Single- or three-phase. EU law made this the AC inlet. Home wallboxes are either:

- **Untethered:** Type 2 socket-outlet on the wall. The driver brings a Type 2–Type 2 Mode 3 cable. Common in Europe.
- **Tethered:** Type 2 connector permanently on the EVSE. Simpler for a single-car household.

Max at home: **22 kW** (3φ 32 A). Locking actuator on the inlet is standard.

### Type 1 / SAE J1772 — North America (non-NACS) and Japan

Five pins: L1, N, PE, CP, PP. **Single-phase only.** Home EVSE is almost always **tethered** (there is no popular J1772 wall socket). Practical home power 7.7–11.5 kW at 240 V (32–48 A). Japan uses the same coupler at 200 V.

### NACS / SAE J3400 — North America (Tesla and adopters)

Five pins; the two large contacts carry **either AC or DC**. For **AC home charging** it is electrically the same as J1772 Level 2 (240 V, typically 32–48 A). Wall Connector is tethered NACS. J1772 wallboxes still work with a passive adapter.

### GB/T 20234.2 AC — China

Seven pins, Type 2 *look-alike* but **reversed gender** and CC instead of PP. Home piles: typically **7 kW** (220 V 32 A) with a GB/T AC socket or tethered plug. Do not insert into an IEC Type 2 inlet.

### Type 3 (Scame)

Deprecated. Do not specify for new homes.

## B — Station front for a home charging station (Mode 3)

| Region | Usual home EVSE front |
| --- | --- |
| Europe, UK, AU/NZ, ME, ZA, IN | Type 2 socket or tethered Type 2 |
| USA / Canada | Tethered J1772 **or** tethered NACS |
| Japan | Tethered Type 1 |
| China | GB/T AC socket or tethered GB/T AC |

A home charging **station** is Mode 3. A Schuko / BS 1363 / NEMA 5-15 lead is Mode 2, not a station.

## A — Connection to the house

Preferred: **hardwired** on a dedicated circuit with the correct RCD.

Plug-in alternatives used at homes:

| Plug | Rating useful for EV | Where |
| --- | --- | --- |
| NEMA 5-15 | 1.4 kW | US Level 1 |
| NEMA 14-50 | 9.6 kW (40 A @ 240 V) | Dominant US plug-in wallbox |
| NEMA 6-50 | 9.6 kW | US welder outlet |
| NEMA 14-30 | 5.8 kW | US dryer |
| Schuko / Type E | ~2.3 kW continuous | EU Mode 2 only |
| BS 1363 | ~2.3 kW | UK Mode 2 only |
| AS/NZS 3112 15 A | ~3.5 kW | AU/NZ Mode 2 |
| IEC 60309 blue 16 A | 3.7 kW | EU garage / campsite |
| IEC 60309 blue 32 A | 7.4 kW | EU 1φ industrial |
| IEC 60309 red 16 A 3φ | 11 kW | EU 3φ |
| IEC 60309 red 32 A 3φ | 22 kW | EU 3φ — top of this overview |
| IEC 60309 blue 3φ 230 V | 6.4–12.7 kW | Norway IT only |

IEC 60309 colour and clock-hour encode voltage. **Red 400 V 6h** and **blue 230 V 3φ (Norway)** are not interchangeable.

## Mode 2 household plugs — use, but do not design a station around them

Household sockets are not designed for 8-hour 16 A EV sessions. Contact temperature is the limit. Treat them as **backup**. A home charging station is a Mode 3 wallbox on a dedicated circuit.
