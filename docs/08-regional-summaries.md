# 8. Regional summaries

## Europe (except Norway IT islands)

- **Grid:** 230/400 V 50 Hz, EN 50160 ±10 %.
- **Earthing:** TN-C-S in DE/NL/Nordics/PL; **TT** in FR/ES/IT/BE.
- **Vehicle:** Type 2. Home EVSE Mode 3, 7.4 kW (1φ) or 11 kW (3φ). 22 kW where 3φ 32 A is available.
- **Household Mode 2:** Schuko / Type E / Type J / BS 1363 — backup only.
- **Industrial sockets:** IEC 60309 blue 16/32 A (1φ), red 16/32 A (3φ).

## United Kingdom & Ireland

- Single-phase 230 V, Type G, Type 2 vehicle, **7.4 kW** wallbox.
- PME open-PEN protection for outdoor points.
- 22 kW is a commercial/public figure, not a typical house.

## Norway

- Dual world: **230 V IT** vs **400 V TN**. Confirm at the meter.
- Type 2. Default 7.4 kW 1φ on IT.

## North America

- **Homes:** 120/240 V 60 Hz split-phase. J1772 and NACS, tethered, 32–48 A @ 240 V (7.7–11.5 kW). NEMA 14-50. NEC 625 / CEC, ANSI C84.1 ±5 % service.
- **Apartments:** often **208Y/120 V** (Level 2 at 208 V, −13 % vs 240 V).
- **Large commercial:** **480Y/277 V**. 277 V = L–N of 480 V wye (lighting / some AC EVSE). Not residential. 80 A @ 277 V ≈ 22 kW AC. DCFC on 480 V 3φ. Canada twin: **600Y/347 V**.
- Corner cases (high-leg delta, 480 V delta without 277 V, Mexico 127/220 V): [`09-north-america-corner-cases.md`](09-north-america-corner-cases.md).

## China

- 220/380 V 50 Hz, GB/T 12325 +7/−10 %.
- GB/T AC 7 kW home pile. Not Type 2.

## Japan

- 100/200 V, 50/60 Hz, TT, Type 1, 3–6 kW home.

## Korea / Taiwan

- KR: 220 V 60 Hz, TT, Type 1 historically.
- TW: 110/220 V 60 Hz, Type 1.

## India

- 230/400 V 50 Hz, TT, Type 2 for cars, often wide voltage swing — specify full IEC band.

## Australia & New Zealand

- 230/400 V 50 Hz, **MEN** (TN-C-S), Type I household, **Type 2** vehicle.
- Houses mostly 1φ → 7.4 kW. Three-phase houses 11/22 kW.

## Gulf

- 230–240 / 400–415 V, Type G, Type 2, TN-S. SA is **60 Hz**. Villas often 3φ.

## Africa (ZA as the mature EV market)

- ZA: 230/400 V 50 Hz, TN-C-S, Type 2, SANS 10142. Design for dips (load-shedding).
- North Africa: 220/380 V, Type E/F, TT, Type 2.

## Latin America

- Mixed 50/60 Hz and 127 vs 220 V. Type 2 is the new-vehicle AC target except where US-market cars bring J1772/NACS (Mexico, parts of Colombia).
