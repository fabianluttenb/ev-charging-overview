# 7. Special cases that break the “230/400 V Type 2” mental model

## Norway and 230 V IT

About 70 % of Norwegian LV is **IT, 230 V line-to-line, often without a neutral**. A “three-phase” house still only has 230 V between any two lines.

- Default safe choice: **single-phase Mode 3**, 16 or 32 A (3.7 or 7.4 kW).
- Three-phase IT at ~11 kW works only if the **onboard charger** is specified for 230 V 3φ (some Teslas; not a universal property).
- Renault Zoé-class chargers have historically been incompatible with IT.
- Newer neighbourhoods: **TN 400 V**, then 11/22 kW as in the rest of Europe.
- Blue IEC 60309 3φ 230 V plugs are **not** red 400 V plugs.

## Belgium (and some French pockets) — 3×230 V delta, no N

Some LV islands are three-phase **230 V delta without a distributed neutral**. Household loads sit across two phases. EVSE that measure N–PE or that need a neutral-referenced control supply can refuse to start. Survey the supply before specifying a wallbox; an isolating transformer to a local TN-S is the robust fix.

## United Kingdom / Ireland — PME open PEN

Most dwellings are **TN-C-S (PME)** and **single-phase**. A 22 kW wallbox is almost never a residential option (no 3φ). The distinctive requirement is **open-PEN protection** for outdoor charging: if PEN is lost, disconnect L, N **and** PE from the vehicle (voltage-operated device, 70 V criterion) or create a true TT island with a suitable electrode. 7.4 kW (32 A) is the standard home rating.

## United States / Canada — several LV families, not one “NA voltage”

Full list: [`09-north-america-corner-cases.md`](09-north-america-corner-cases.md).

- **Homes:** 120/240 V split-phase. Level 1 = 120 V; Level 2 = 240 V, 32–48 A (7.7–11.5 kW). J1772 or NACS, almost always tethered. Breaker = 125 % of charger current. NEMA 14-50 = 40 A continuous (9.6 kW).
- **Apartments / small commercial:** **208Y/120 V**. Level 2 at 208 V is ~13 % below a 240 V nameplate (32 A → 6.7 kW). EVSE must be 208–240 V.
- **Large commercial / industrial:** **480Y/277 V**. **277 V is L–N of 480 V wye** — lighting and some workplace AC EVSE, **not** a house voltage. 80 A × 277 V ≈ **22 kW** is the NA AC ceiling (NACS/J1772), not European 3φ 400 V. Many wallboxes are 208–240 V only — do not land them on 277 V. DCFC sits on **480 V three-phase**.
- **480 V delta** has **no 277 V** (no wye N). **High-leg 240 V delta:** never put L–N EVSE on the orange 208 V-to-N leg.
- **Canada commercial** often **600Y/347 V** (347 V lighting). Mexico dwellings **127/220 V**, not 120/240 V.
- No residential three-phase AC to the car (SAE J3068 is depot/fleet). UL 2231 CCID ≠ IEC Type B.

## Taiwan — 110/220 V 60 Hz, and yes they have 40 A

Homes are **1φ 3-wire 110/220 V at 60 Hz** (US-style split-phase, but 110/220 not 120/240). Type A/B sockets are 110 V. A home charging station is a **dedicated 220 V** circuit.

- Default wallbox: **32 A @ 220 V ≈ 7.0 kW**, SAE J1772 / CNS 15511 Type 1. Tesla Taiwan currently sells a **Type 2** Wall Connector as well.
- **40 A almost always means the breaker**, not the car current: a 32 A EVSE is paired with a **40 A NFB** (continuous-load 125 %, same idea as NEC). Tesla TW’s home-charging page quotes a **40 A breaker** for Model 3 / Y (~40 km of range per hour).
- **40 A EVSE output also exists:** domestic SKUs such as Evalue CSDA-X40A / CBDA-X40A are **40 A / 8.8 kW @ 220 V**, on a **50 A** RCCB. Adjustable boxes list 16 / 24 / 32 / **40** / 50 A. Not the default apartment install, but it is a listed, CNS-certified current.
- Above that: 48 A (≈10.5 kW, e.g. Delta), 50 A (11 kW), 60 A (MSI 13.2 kW), 80 A (≈17.6 kW) — service-capacity limited, not typical 表燈 dwellings.
- Building supplies also include **3φ 3-wire 220 V** and **3φ 4-wire 220/380 V**. Taipower guidance for new EV feeders prefers 1φ 110/220 or 3φ 4-wire 220/380, not extra 3φ 3-wire 220 V (phase balance).
- NEMA 14-50 shows up on portable EVSE; it is **not** a standard Taiwan wall outlet.

## Japan — 100/200 V, 50/60 Hz split, Type 1, TT

Home charging is **200 V single-phase Type 1**, typically 3–6 kW. 100 V is trickle only. East/west frequency split does not affect modern EVSE. Many household outlets are ungrounded Type A — Mode 2 on those is poor practice; use a grounded 200 V circuit.

## China — 220 V, GB/T AC, 7 kW home piles

The AC coupler looks like Type 2 and is **not** Type 2 (reversed gender, CC vs PP). Home AC is almost always **7 kW 1φ**. Three-phase AC exists in the standard (up to 63 A) but is not a typical apartment product.

## Saudi Arabia — 230/400 V at **60 Hz**

Treat as IEC 230/400 V family but **60 Hz**. Type G household plugs, Type 2 vehicle, TN-S. Villas often have three-phase service, so 11/22 kW is realistic.

## Brazil — 127 V *or* 220 V, 60 Hz, Type N

Voltage is a **state-level** fact. A “Brazilian” wallbox must be selected for the site voltage. Type 2 is the emerging vehicle inlet.

## Single-phase car on a three-phase wallbox

The car uses **one** phase. On a 22 kW (3×32 A) post it still charges at 7.4 kW and **unbalances** the service. Load management should rotate phases across multiple parking spots.

## 22 kW at home — when it is real

Needs **all** of:

1. Three-phase 400 V (or 380 V) at the dwelling
2. Main fuse / contracted power that can spare 3×32 A plus the house
3. A vehicle onboard charger that is actually 22 kW (minority of cars)
4. DSO permission if the national grid code requires it (Germany and others)

Otherwise specify **11 kW** (3×16 A) or **7.4 kW** (1×32 A).
