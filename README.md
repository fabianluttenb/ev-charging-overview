# AC networks for EV charging

Worldwide technical overview of the **low-voltage AC networks** that matter for **AC charging of electric cars** (up to 22 kW).

It covers earthing, voltages and tolerances, standards, currents and powers, and the connectors used for **home charging stations**. Country profiles are typical values for site planning — not a substitute for a survey or the local wiring rules.

Open **[index.html](index.html)** in a browser. No server is required.

AC wallbox comparison (per manufacturer, datasheet links) lives in [`charging-station-benchmark/`](charging-station-benchmark/README.md) and in the HTML **Charging stations** section.

---

## Quick start

1. Clone this repository.
2. Open `index.html` (double-click, or *Open with* a browser).
3. Use the left navigation, or start at **Site profile** and pick a country.

The page is self-contained: CSS, diagrams, calculator, and country data are embedded. The JSON under `data/` is the same information in machine-readable form.

---

## What this answers

Four facts decide a home or workplace AC installation:

1. **Voltage and phases** at the dwelling (230/400 V wye, 120/240 V split-phase, 208Y/120, 230 V IT, Japan 100/200 V, …).
2. **Earthing system** (TN-S, TN-C-S / PME / MEN, TT, IT) and the extra rules that follow (open-PEN, local electrode, no PEN on the EV circuit).
3. **Vehicle inlet** (Type 2, SAE J1772, NACS / J3400, GB/T AC).
4. **National installation rules** (IEC 60364-7-722, BS 7671 §722, NEC 625, DIN VDE 0100-722, AS/NZS 3000, GB/T 18487, …).

The interactive viewer also has:

- Clickable earthing schematics
- Voltage-tolerance bands (EN 50160, ANSI C84.1, GB/T 12325)
- Power calculator (family × phases × current → kW and breaker size)
- Supply vs onboard-charger matrix
- Connector pinouts and home supply plugs (hardwired, NEMA 14-50, IEC 60309, Mode 2 household)
- Filterable / sortable table of 76 countries
- AC wallbox benchmark (26 manufacturers, datasheet links)
- Special cases (Norway IT, UK PME, Belgium 3×230 V delta, US split-phase, Japan, China GB/T, Saudi 60 Hz)

---

## Repository layout

```
ev-charging-overview/
├── index.html                 Interactive viewer (start here)
├── charging-station-benchmark/  AC wallbox catalog (one folder per OEM)
├── README.md
├── data/                      Machine-readable datasets
│   ├── countries.json         Grid + charging profile by country
│   ├── connectors.json        Vehicle, station, and home-supply connectors
│   ├── standards.json         IEC / SAE / GB/T / national installation rules
│   ├── power-levels.json      Power, current, voltage combinations ≤ 22 kW
│   └── earthing.json          TN / TT / IT families and EVSE implications
├── docs/                      Written reference (same topics as the HTML)
│   ├── 01-overview.md
│   ├── 02-earthing-concepts.md
│   ├── 03-voltages-and-tolerances.md
│   ├── 04-standards.md
│   ├── 05-power-and-currents.md
│   ├── 06-connectors-home-use.md
│   ├── 07-special-cases.md
│   ├── 08-regional-summaries.md
│   └── 09-north-america-corner-cases.md
└── references/
    └── sources.md
```

`index.html` embeds a copy of `data/countries.json`. If you edit country data, update both (or re-inject the JSON into the `const DATA = …` block in the HTML).

---

## Scope

| In scope | Out of scope |
| --- | --- |
| Public LV AC used by home / workplace EVSE | DC fast charging (CCS, CHAdeMO, GB/T DC, NACS DC) except as context |
| Earthing (TN-C, TN-S, TN-C-S, TT, IT) | MV / HV transmission |
| Nominal voltages, frequency, tolerances | Onboard charger power-electronics |
| IEC 61851 Modes 1–3 | Wireless / inductive charging |
| Powers up to 22 kW AC | Public-charging business models |
| Home-use connectors (vehicle, wallbox, grid plug) | |

North America is several LV families, not one voltage. **Homes** are 120/240 V split-phase. **Apartments** are often 208Y/120 V (Level 2 at 208 V). **Large commercial** is **480Y/277 V**: 277 V is L–N of 480 V wye (lighting and some workplace AC EVSE), not a house voltage; 80 A × 277 V ≈ 22 kW AC. Also 480 V delta (no 277 V), high-leg 240 V delta, and Canada **600Y/347 V**. See [`docs/09-north-america-corner-cases.md`](docs/09-north-america-corner-cases.md).

---

## Typical home AC powers

| Connection | Current | Nominal power |
| --- | --- | --- |
| 1φ 230 V | 16 A | 3.7 kW |
| 1φ 230 V | 32 A | 7.4 kW |
| 3φ 400 V | 16 A | 11 kW |
| 3φ 400 V | 32 A | **22 kW** (upper bound of this overview) |
| 1φ 240 V (US/CA) | 32–48 A | 7.7–11.5 kW |

Delivered power is the **minimum** of EVSE rating, cable, vehicle onboard charger, and available grid current after load management. Many European cars stop at 11 kW AC even on a 22 kW post.

Protective-device rating is typically **≥ 125 %** of EVSE current (continuous load): a 32 A wallbox on a 40 A breaker.

---

## Disclaimer

This is an engineering overview compiled from public standards summaries and regional practice. Installations must follow the **national wiring rules** in force at the site (for example BS 7671, NEC, DIN VDE 0100-722, AS/NZS 3000, GB 50054) and the distribution-network operator’s requirements. Always verify against the current official text of the cited standard.

Sources are listed in [`references/sources.md`](references/sources.md).
