# 9. North America — corner cases

North America is not one voltage. Homes, apartments, shops, and plants sit on **different LV families**. A wallbox rated 208–240 V is correct for a house and **wrong** on a 277 V lighting panel. Survey the **service type**, not the country.

## Service families

| Family | L–N | L–L | Where | AC charging |
| --- | --- | --- | --- | --- |
| Split-phase 120/240 V | 120 V | 240 V | Almost all US/CA houses | Level 1 120 V; Level 2 240 V |
| 208Y/120 V wye | 120 V | 208 V | Apartments, small commercial | Level 2 at **208 V** (−13 % vs 240 V nameplate) |
| **480Y/277 V wye** | **277 V** | **480 V** | Large commercial / industrial | 277 V 1φ EVSE **if rated for it**; DCFC on 480 V 3φ |
| 480 V delta | — | 480 V | Older / some industrial | **No 277 V** (no wye N). Do not assume a lighting tap |
| 240 V high-leg delta | 120 V (A,C) / 208 V (B) | 240 V | Older commercial | Never put L–N EVSE on the **high leg** |
| 600Y/347 V wye | 347 V | 600 V | Canada commercial (some US plants) | 347 V analogue of 277 V |
| Mexico 127/220 V | 127 V | 220 V | MX dwellings | Not 120/240 V; confirm the site |

ANSI C84.1 Range A at the meter is **±5 %** (tighter than EN 50160 ±10 %), then extra drop is allowed inside the building.

---

## 277 V (480Y/277 V) — the one that is not a house

**277 V is the phase-to-neutral of a 480 V wye.** It is **not** a US region and **not** a residential voltage.

\[
277 \approx 480 / \sqrt{3}
\]

Same idea as Europe’s 230 V L–N from 400 V L–L, one step higher.

- **Where:** office towers, hospitals, schools, warehouses, factories, malls, parking garages of those buildings — **nationwide**.
- **What uses it:** commercial lighting (historic fluorescent ballasts, now 120–277 V LED drivers); some branch loads; **some** workplace AC EVSE.
- **480 V L–L / 3φ:** HVAC, motors, elevators, **DC fast chargers**.
- **Homes:** 120/240 V split-phase. 480Y/277 is not a dwelling service (rare exceptions: very large estates with a 480 V HVAC plant — still not a garage 14-50).

### Charging on 277 V

| Current | Power at 277 V | Notes |
| --- | --- | --- |
| 32 A | 8.9 kW | Only if the EVSE is 277 V rated |
| 48 A | 13.3 kW | Commercial wall unit |
| 80 A | **22.2 kW** | NACS / J1772 AC ceiling on 277 V — this is the North American **22 kW AC** figure, **not** 3φ 400 V |

Rules:

- Many Level 2 boxes are **208–240 V only**. Landing them on 277 V destroys the supply or is refused by the installer. Check the nameplate.
- NACS (SAE J3400) allows AC up to 80 A at 277 V in the standard; residential product is still 32–48 A at **240 V**.
- A 277 V circuit is **one phase + N + PE** (single-pole breaker on a 480Y panel), not three-phase to the car. J1772 / NACS stay single-phase.
- Workplace “we have three-phase” often means **480 V motors** plus **277 V lights**. The garage EVSE may actually be on a **208Y** step-down — survey the panel.

---

## 208Y/120 V — apartments and small commercial

Three-phase wye at the building; dwellings take one or two phases + N.

- Level 2 is **208 V L–L**, not 240 V.
- Power is \(208/240 \approx 87 %\) of a 240 V nameplate (32 A → **6.7 kW**, not 7.7 kW).
- EVSE must be listed **208–240 V**. A “240 V only” unit may not start or may run hot.
- Receptacles stay 120 V. There is no 240 V dryer-style split-phase in a pure 208Y suite.

---

## High-leg (wild-leg) 240 V delta

Older commercial 120/240 V **three-phase four-wire delta**. One winding is centre-tapped for 120 V loads. The opposite phase (orange, “high leg”) is **208 V to neutral** and **240 V to the other phases**.

- **Never** connect 120 V loads or an L–N EVSE to the high leg.
- 240 V L–L (two hots, no N) can feed a 240 V EVSE if the two legs are a proper 240 V pair and the breaker is two-pole.
- Easy to mis-identify as 208Y. Measure all three L–N voltages: 120 / 120 / 208 means high-leg, not 208Y (which is 120 / 120 / 120).

---

## 480 V delta — no 277 V

Ungrounded, corner-grounded, or high-resistance-grounded **delta** has 480 V L–L and **no 277 V** tap.

- EVSE that need a **neutral** (control supply, 277 V lighting-style 1φ) will not have one.
- Corner-grounded B-phase is a shock/identification trap. Do not treat any phase as “neutral”.
- Derive 208Y/120 or 480Y with a transformer if you need N for charging.

---

## 600Y/347 V (Canada)

Canadian large-commercial twin of 480Y/277: **347 V L–N** lighting, **600 V** motors. A few US industrial sites near the border use it. Same warning: EVSE must be **347 V rated**; a 277 V or 240 V box is not a substitute.

---

## Mexico

Dwellings are often **127/220 V** split-phase (not 120/240). Commercial may be 220 V 3φ or 480Y. NOM, not NEC. Vehicle inlets follow the US (J1772 / NACS) more than Type 2.

---

## Couplers and “22 kW”

- Vehicle AC is **J1772 (Type 1)** or **NACS (J3400)** — **single-phase only**. There is no Type 2 three-phase on a US house.
- **SAE J3068** (Type 2 3φ) exists for depots / medium-duty, not residences.
- Stations are almost always **tethered**. There is no popular J1772 wall socket like a European Type 2 outlet.
- NACS↔J1772 **AC** adapters are passive; DC adapters are a different product.
- European **22 kW = 3φ 32 A @ 400 V**. North American **22 kW AC ≈ 80 A @ 277 V** on a commercial 480Y — rare, and not a home circuit.

---

## Installation traps (NEC / UL)

- **Continuous load 125 %** (NEC 625): 32 A EVSE → 40 A breaker; 40 A → 50 A (14-50); 48 A → 60 A hardwired.
- **Load calculation:** a 60 A EV circuit is a large slice of a 100 A dwelling service. NEC 220 / 625.42 (energy management) often required.
- **NEMA 14-50:** 50 A 125/250 V, four-wire (L1, L2, N, PE). Most EVSE ignore N. **6-50** is 50 A without N (welder). **14-30** dryer = 24 A continuous ≈ 5.8 kW. **5-15** = Level 1 only (1.4 kW).
- **UL 2231 CCID** (typically 5 mA personnel protection) is not an IEC Type B / 6 mA RDC-DD. Do not specify European RCD types on an NEC installation unless the product listing says so.
- **GFCI** on a 14-50 or dryer outlet: nuisance trips with some EVSE; use the EVSE listing and NEC 625, not a kitchen GFCI philosophy.
- **Multi-grounded neutral** is a TN-C-S analogue. NEC does **not** copy BS 7671’s outdoor 70 V open-PEN disconnect. A lost utility neutral is still a real shock/fire hazard; it is handled by utility practice and bonding, not by a standard EV O-PEN box.

---

## What to specify

| Site | Typical AC EVSE |
| --- | --- |
| US/CA house | 240 V 1φ, 32–48 A, J1772 or NACS, hardwired or 14-50 |
| Apartment garage | **208 V** 1φ, confirm 208Y vs 240 V, load management |
| Workplace in a 480Y building | Confirm panel: **208 V** step-down vs **277 V** lighting vs **480 V** 3φ for DCFC |
| Canada commercial | 208 V, 240 V, **347 V**, or 600 V 3φ — read the panel |
| Mexico house | 220 V 1φ (127/220), J1772/NACS |
