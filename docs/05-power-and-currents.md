# 5. Powers and currents (up to 22 kW)

## Formulae

- Single-phase or split-phase: \(P = U \times I\)
- Three-phase wye (400 V L–L / 230 V L–N): \(P = \sqrt{3} \times U_{LL} \times I = 3 \times U_{LN} \times I\)
- Three-phase 230 V IT (L–L only): \(P = \sqrt{3} \times 230 \times I\)

Currents below are **EVSE / vehicle AC current**. Protective-device rating is typically **≥ 125 %** of that current (continuous load). A 32 A wallbox is placed on a **40 A** breaker.

## The four IEC powers everyone quotes

| Name | Connection | Current | Nominal power |
| --- | --- | --- | --- |
| 3.7 kW | 1φ 230 V | 16 A | 3.68 kW |
| 7.4 kW | 1φ 230 V | 32 A | 7.36 kW |
| 11 kW | 3φ 400 V | 16 A | 11.09 kW |
| 22 kW | 3φ 400 V | 32 A | 22.17 kW |

These four cover almost all Mode 3 home wallboxes outside North America and Japan.

## North America (split-phase 240 V)

| Circuit breaker | Continuous current (80 %) | Power @ 240 V | Typical outlet |
| --- | --- | --- | --- |
| 15 A | 12 A | 1.4 kW | NEMA 5-15 (Level 1, 120 V → 1.4 kW) |
| 20 A | 16 A | 3.8 kW | NEMA 6-20 |
| 40 A | 32 A | 7.7 kW | hardwired |
| 50 A | 40 A | 9.6 kW | NEMA 14-50 |
| 60 A | 48 A | 11.5 kW | hardwired (common modern wall unit) |
| 100 A | 80 A | 19.2 kW | J1772 theoretical max — rare in homes |

J1772 / NACS are **single-phase**. There is no 22 kW three-phase residential AC in the US/Canada. SAE J3068 (Type 2 three-phase) exists for depots, not houses.

## Japan

| Circuit | Power |
| --- | --- |
| 100 V 15 A | 1.5 kW |
| 200 V 16 A | 3.2 kW |
| 200 V 30 A | 6.0 kW |

## Norway 230 V IT

| Connection | Power |
| --- | --- |
| 2-wire 16 A (two lines) | 3.7 kW |
| 2-wire 32 A | 7.4 kW |
| 3-line 16 A (if vehicle accepts 230 V 3φ) | 6.4 kW |
| 3-line ~28 A (Tesla class) | ~11 kW |
| TN 400 V 16 / 32 A (newer areas) | 11 / 22 kW |

## Supply vs onboard charger (what you actually get)

A 22 kW wallbox does not make a 7.4 kW car charge at 22 kW. The **minimum** of supply, cable, EVSE setting, and onboard charger wins.

| Supply \ OBC | 1φ 32 A car (7.4 kW) | 3φ 16 A car (11 kW) | 3φ 32 A car (22 kW) |
| --- | --- | --- | --- |
| 1φ 16 A | 3.7 | 3.7 | 3.7 |
| 1φ 32 A | 7.4 | 7.4 | 7.4 |
| 3φ 16 A | **3.7** (one phase only) | 11 | 11 |
| 3φ 32 A | **7.4** | **11** | 22 |

Most modern European cars are **11 kW** onboard. Specifying 22 kW at home is useful for a future car or a workplace post; it is wasted on an 11 kW vehicle.

## Cable and connector current

Type 2 PP resistors code the **cable**:

| PP resistance to PE | Cable rating |
| --- | --- |
| 1 500 Ω | 13 A |
| 680 Ω | 20 A |
| 220 Ω | 32 A |
| 100 Ω | 63 A |

The EVSE must also respect this. A 22 kW socket with a 20 A cable must advertise ≤ 20 A on CP.
