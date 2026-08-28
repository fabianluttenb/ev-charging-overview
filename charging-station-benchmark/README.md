# AC charging station benchmark

Home and workplace **Mode 2 portable IC-CPDs** and **Mode 3 AC wallboxes** (up to 22 kW IEC / ~12 kW NA Level 2). Each manufacturer has its own folder with product notes, features, IEC 61851 mode, and links to official product pages and datasheets.

Open the repo **[index.html](../index.html)** and jump to **Charging stations** for a filterable comparison. Specs are from public datasheets and product pages (2024–2026). Always verify the current official sheet before specifying.

## Folder layout

```
charging-station-benchmark/
├── README.md
├── catalog.json                 Machine-readable comparison (also embedded in index.html)
├── images-index.json            Local photo / PDF filenames per OEM
└── manufacturers/
    ├── abb/
    │   ├── README.md
    │   ├── products.json
    │   └── images/              FCC internals, Wikimedia, ZDI PCB, teardown thumbs
    ├── keba/
    ├── wallbox/
    └── …
```

Each manufacturer folder contains `README.md` (human notes), `products.json` (the same records as in `catalog.json`), and `images/` with whatever public teardown or product photos could be stored locally. Sources are listed in `images/IMAGES.md`.

**Teardown coverage is uneven.** NA SKUs (Tesla, Emporia, Autel, ChargePoint, Wallbox RFID) have FCC internal-photo PDFs and ZDI Pwn2Own PCB photos. EU wallboxes rarely publish internals — those folders hold Wikimedia product shots, ADAC benchmark *links*, and teardown-video thumbnails (Munro Live, BruCON, Zerobrain, eFIXX). Do not treat brochure renders as teardowns.

Refresh downloads: `python tools/download_station_images.py` from the repo root.

## Scope

| In | Out |
| --- | --- |
| Mode 3 AC wallboxes ≤ 22 kW (IEC) / ≤ ~50 A (NA) | DC fast chargers except as a brand context |
| Mode 2 portable IC-CPDs (NRGkick, Juice Booster, go-e flex, Tesla Mobile Connector, …) | Public DC hubs, pantograph, MCS |
| Home, workplace, travel, light commercial | Unnamed generic 8–13 A “granny” cables |
| Connectors, RCD, OCPP, load/PV, IP/IK, IEC 61851 mode | Pricing (varies too fast) |

**Mode 2** = in-cable control and protection device (IC-CPD, IEC 62752) on a household or industrial socket. **Mode 3** = dedicated EVSE (wallbox). Some portables (NRGkick, Juice Booster) are Mode 2 on CEE/Schuko and Mode 3 when used as a Type 2 charging cable.

## How to read a row

- **Power** is the *maximum nameplate*. Delivered power is min(EVSE, cable, OBC, grid).
- **40 A** in Taiwan/US often means the **breaker**, not the EVSE current (32 A EVSE → 40 A NFB).
- **OCPP** versions and whether they are native vs cloud-to-cloud differ by SKU.
- **MID / Eichrecht** only matters if you bill a third party (company car, tenants).

Sources are listed per manufacturer. Regenerating folders: `python tools/generate_benchmark.py` from the repo root.
