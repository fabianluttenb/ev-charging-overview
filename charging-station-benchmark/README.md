# AC charging station benchmark

Home and workplace **Mode 3 AC** wallboxes (up to 22 kW IEC / ~12 kW NA Level 2). Each manufacturer has its own folder with product notes, features, and links to official product pages and datasheets.

Open the repo **[index.html](../index.html)** and jump to **Charging stations** for a filterable comparison. Specs are from public datasheets and product pages (2024–2026). Always verify the current official sheet before specifying.

## Folder layout

```
charging-station-benchmark/
├── README.md
├── catalog.json                 Machine-readable comparison (also embedded in index.html)
└── manufacturers/
    ├── abb/
    ├── keba/
    ├── wallbox/
    └── …
```

Each manufacturer folder contains `README.md` (human notes) and `products.json` (the same records as in `catalog.json`).

## Scope

| In | Out |
| --- | --- |
| Mode 3 AC wallboxes ≤ 22 kW (IEC) / ≤ ~50 A (NA) | DC fast chargers except as a brand context |
| Home, workplace, light commercial | Public DC hubs, pantograph, MCS |
| Connectors, RCD, OCPP, load/PV, IP/IK | Pricing (varies too fast) |

## How to read a row

- **Power** is the *maximum nameplate*. Delivered power is min(EVSE, cable, OBC, grid).
- **40 A** in Taiwan/US often means the **breaker**, not the EVSE current (32 A EVSE → 40 A NFB).
- **OCPP** versions and whether they are native vs cloud-to-cloud differ by SKU.
- **MID / Eichrecht** only matters if you bill a third party (company car, tenants).

Sources are listed per manufacturer. Regenerating folders: `python tools/generate_benchmark.py` from the repo root.
