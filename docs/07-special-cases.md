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

## United States / Canada — split-phase, two AC couplers, 125 % sizing

- 120 V Level 1 and 240 V Level 2 on the **same** split-phase service.
- Apartments may only have **208 V** (wye); power is 208/240 ≈ 13 % lower than a 240 V nameplate.
- Vehicle inlet is **J1772 or NACS**, not Type 2.
- Breaker = 125 % of charger current (48 A charger → 60 A breaker).
- NEMA 14-50 is the default plug-in home outlet (40 A continuous).

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
