#!/usr/bin/env python3
"""Download FCC / Wikimedia / ZDI teardown and product images into manufacturer folders."""
from __future__ import annotations

import json
import re
import ssl
import urllib.parse
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MFG = ROOT / "charging-station-benchmark" / "manufacturers"
UA = (
    "Mozilla/5.0 (compatible; ev-charging-overview/1.0; "
    "+https://github.com/fabianluttenb/ev-charging-overview) "
    "AppleWebKit/537.36 Chrome/120.0.0.0"
)
CTX = ssl.create_default_context()

# wiki:<FileName> is resolved via the Commons API.
# yt:<id> is a YouTube maxres/hq thumbnail of a teardown or internals video.
# Other URLs are fetched directly.

DOWNLOADS: dict[str, list[tuple[str, str]]] = {
    "abb": [
        ("commons-terra-chargers.jpg", "wiki:ABB-Terra-chargers.jpg"),
        ("commons-iaa-2023-munich.jpg", "wiki:IAA Mobility 2023, Munich (P1110321).jpg"),
        ("brochure-terra-ac.pdf", "https://library.e.abb.com/public/8adddd9cf393467bb98a960832aa7662/9AKK108472A2560_en_Brochure_C_Terra%20AC%20Wallbox.pdf"),
    ],
    "keba": [
        ("commons-p30-graz-wall.jpg", "wiki:KEBA_P30_c-series_wall-mounted_charging_station_at_Straßganger_Straße_380_b+e_in_Graz,_Styria,_Austria-wallbox_PNr°1163.jpg"),
        ("commons-p30-wiesbaden.jpg", "wiki:Electric vehicle AC charging station, Wiesbaden (LRM 20250714 172851).jpg"),
        ("commons-honda-evse-keba.jpg", "wiki:Honda EVSE.jpg"),
        ("commons-p30-keba-lrm.jpg", "wiki:Keba KeContact P30 (LRM 20250627 074447).jpg"),
        ("datasheet-p30.pdf", "https://www.keba.com/download/x/be0ccce36d/kecontact_p30_technicaldata_dben.pdf"),
    ],
    "wallbox": [
        ("munro-pulsar-plus-teardown-thumb.jpg", "yt:MBq81HjC00w"),
        ("fcc-2BB8L-RFID02-internal.pdf", "https://fccid.io/pdf.php?id=7184885"),
        ("fcc-2BB8L-RFID02-internal-alt.pdf", "https://fcc.report/FCC-ID/2BB8L-RFID02/7184885.pdf"),
        ("datasheet-pulsar-family.pdf", "https://d1lnencgr7glws.cloudfront.net/wp-content/uploads/2024/07/31122738/EN_Pulsar_Family_Datasheets.pdf"),
    ],
    "easee": [
        ("efixx-rcd-test-thumb.jpg", "yt:r1VzrJVRgLo"),
        ("efixx-review-open-cover-thumb.jpg", "yt:e_aJRe5bf04"),
        ("install-guide.pdf", "https://download.easee.com/m/48f3bf628744a32b/original/EN_Home_Charge_IG.pdf"),
    ],
    "zaptec": [
        ("commons-zaptec-go.jpg", "wiki:Zaptec Go.jpg"),
        ("commons-zaptec-go-asphalt.jpg", "wiki:Zaptec Go..jpg"),
        ("commons-zaptec-go-unbox.jpg", "wiki:Zaptec Go i orginalförpackning.jpg"),
        ("brucon-teardown-thumb.jpg", "yt:raZHd1Q4Vrc"),
    ],
    "alfen": [
        ("commons-eve-double-pro-line.jpg", "wiki:Borne de recharge Alfen Eve Double Pro-line.jpg"),
        ("commons-twin-winschoten.jpg", "wiki:Blijhamsterstraat Allego charging station and parking sign, Winschoten (2023) 02.jpg"),
        ("commons-icu-hague.jpg", "wiki:ICU Charging Equipment charging station, The Hague (2019) 05.jpg"),
        ("datasheet-eve-single.pdf", "https://eu-assets.contentstack.com/v3/assets/blt08d332658a89f766/blta4f9411e56ab5073/68122bc8e6f15cbfb092b5e1/904460xxx-ace-ds-1200-1.2-en_datasheet_eve_single_int.pdf"),
    ],
    "evbox": [
        ("commons-elvi-or-businessline-tauber.jpg", "wiki:Elektroauto Ladestation an einem Renault Autohaus in Tauberbischofsheim 2.jpg"),
        ("commons-alize-tournefeuille.jpg", "wiki:Borne de recharge alizé à Tournefeuille.jpg"),
        ("commons-wetherby.jpg", "wiki:Electric car charging point, Cluster of Nuts car park, Wetherby (8th April 2020).jpg"),
    ],
    "mennekes": [
        ("commons-amtron-alfa-romeo.jpg", "wiki:Alfa Romeo Junior IMG 0475.jpg"),
        ("commons-type2-front.png", "wiki:Type 2 connector-front-alpha PNr°0527b.png"),
        ("commons-type2-side.png", "wiki:Type 2 connector-side-alpha PNr°0526b.png"),
        ("commons-type2-socket-detail.jpg", "wiki:Chargingstation socket VDE-AR-E-2623-2-2 mennekes detailed.jpg"),
        ("commons-icu-hague.jpg", "wiki:ICU Charging Equipment charging station, The Hague (2019) 01.jpg"),
    ],
    "go-e": [
        ("zerobrain-gemini-flex-teardown-thumb.jpg", "yt:B0KHW3OnVRg"),
        ("datasheet-pro.pdf", "https://cdn.shopify.com/s/files/1/0729/7584/3675/files/go-e-charger-pro-datenblatt.pdf"),
    ],
    "heidelberg": [
        ("commons-amperfied.jpg", "wiki:Hdm2024105 amperfied z7n4068 small.jpg"),
        ("commons-horchheim-ladesaeule.jpg", "wiki:Horchheim Jeschek Ladesäule.jpg"),
    ],
    "abl": [
        ("commons-jcrg-hof.jpg", "wiki:E-Ladestation am JCRG Hof 20210809 HOF02789.jpg"),
        ("commons-ladesaeulen.jpg", "wiki:Ladesäulen.jpg"),
    ],
    "schneider-electric": [
        ("commons-evlink-pro-ac-metal.jpg", "wiki:Schneider Electric EVLink Pro AC Metal used for a Coles EV Charging Station.jpg"),
        ("commons-evlink-1.jpg", "wiki:EVLinkSchneiderElectric.jpg"),
        ("commons-evlink-2.jpg", "wiki:EVLinkSchneiderElectric2.jpg"),
        ("commons-evlink-pont-veyle.jpg", "wiki:Borne Recharge Électrique EVlink Parc Château Pont Veyle 1.jpg"),
    ],
    "siemens": [
        ("commons-versicharge-ac.jpg", "wiki:Siemens VersiCharge AC Series Charging Station.jpg"),
    ],
    "tesla": [
        ("fcc-2AEIM-1470138-internal.pdf", "https://fccid.io/pdf.php?id=6836392"),
        ("fcc-2AEIM-1470138-internal-fcc-report.pdf", "https://fcc.report/FCC-ID/2AEIM-1470138/6836392.pdf"),
        ("fcc-2AEIM-1470138-external.pdf", "https://fccid.io/pdf.php?id=6836391"),
        ("zdi-pcb-top.jpg", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/95a0a5b5-3e35-4166-8a81-adfd78a326a5/Picture1.jpg?format=2500w"),
        ("zdi-pcb-bottom.jpg", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/4ec56b9b-b6ef-4a8f-a7a4-3be177e9b00b/Picture2.jpg?format=2500w"),
        ("zdi-debug-headers.jpg", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/ae4747b1-4744-40cf-b375-3f6f50e927de/Picture3.jpg?format=2500w"),
        ("zdi-flash-vias.jpg", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/c4802bcc-8050-46c8-991d-0a297d36cc04/Picture4.jpg?format=2500w"),
        ("munro-teardown-thumb.jpg", "yt:4wVhiySuZw4"),
        ("commons-wall-connector-newton-1.jpg", "wiki:Tesla Wall Connector EV charging station installed outdoors in Newton MA 1.jpg"),
        ("commons-wall-connector-newton-2.jpg", "wiki:Tesla Wall Connector EV charging station installed outdoors in Newton MA 2.jpg"),
        ("commons-nacs-vs-type2.jpg", "wiki:Tesla-charging-iec-type-2-outlet-tesla02-outlet.jpg"),
    ],
    "chargepoint": [
        ("zdi-cpu-side0.png", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/d82e13d8-7918-46a6-8c81-9588e48984bb/ChargePoint-Home-Flex-CPU-Board-Side-0.png?format=2500w"),
        ("zdi-cpu-side1.png", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/213e7321-1b65-4ae5-b80f-b05edf0b7092/ChargePoint-Home-Flex-CPU-Board-Side-1.png?format=2500w"),
        ("zdi-metrology-side0.png", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/ba8568a2-f580-480c-9a37-ac2e8d96cea7/ChargePoint-Home-Flex-Metrology-Board-Side-0.png?format=2500w"),
        ("zdi-metrology-side1.png", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/1f102a55-0ff7-4b2f-8f50-2e12fa5884a8/ChargePoint-Home-Flex-Metrology-Board-Side-1.png?format=2500w"),
        ("commons-home-charger.jpg", "wiki:ChargePoint Home Charger.jpg"),
        ("commons-home-install.jpg", "wiki:Closer ChargePoint Install At Home.jpg"),
        ("datasheet-home-flex.pdf", "https://docs.chargepoint.com/ref-docs-sec/content/pdfs/1-home/flex/flex-ds.pdf"),
        ("fcc-w38-28010087-internal.pdf", "https://fccid.io/pdf.php?id=2809822"),
    ],
    "emporia": [
        ("zdi-main-board.jpg", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/07fc18ce-9add-42ea-be33-306cfdebe9fe/Emporia-IMG_3307.JPG?format=2500w"),
        ("zdi-msp430-detail.jpg", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/d97b71f8-390a-44a3-8dc3-cee50e9101bc/Emporia-IMG_3324.jpg?format=2500w"),
        ("fcc-2AS6P-EMEVSE1-internal.pdf", "https://fccid.io/pdf.php?id=5330031"),
        ("fcc-2AS6P-EMEVSE1-internal-fcc-report.pdf", "https://fcc.report/FCC-ID/2AS6P-EMEVSE1/5330031.pdf"),
        ("fcc-2AS6P-EMEVSE1-external.pdf", "https://fccid.io/pdf.php?id=5329990"),
    ],
    "autel": [
        ("zdi-metrology.png", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/90a704e5-c84d-4b60-96fb-0781706abd41/Autel-Maxi-IMG_7467.png?format=2500w"),
        ("zdi-modem.png", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/50756b89-cb42-429d-94ba-033bfde135f9/Autel-Maxi-IMG_7466.png?format=2500w"),
        ("zdi-cpu.png", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/d1c29348-76b1-48ab-949d-6a25c120cb5f/Autel-Maxi-IMG_7464.png?format=2500w"),
        ("zdi-cpu-reverse.png", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/b05d9c21-1437-481d-9b70-a8dabb988ee2/Autel-Maxi-IMG_7465.png?format=2500w"),
        ("zdi-barrot-bt.jpeg", "https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/57f4a670-1f64-4917-b0e1-2d94b0c54f36/Autel-Barrot-BT.jpeg?format=2500w"),
        ("fcc-2A5NP-AUTELNEACL-internal.pdf", "https://fccid.io/pdf.php?id=5940315"),
        ("fcc-2A5NP-AUTELNEACL-internal-fcc-report.pdf", "https://fcc.report/FCC-ID/2A5NP-AUTELNEACL/5940315.pdf"),
        ("fcc-2A5NP-AUTELNEACL-external.pdf", "https://fccid.io/pdf.php?id=5940155"),
    ],
    "delta": [
        ("commons-evpt3215mwe.jpg", "wiki:Delta Electronics EVPT3215MWE 20190601.jpg"),
        ("commons-ev-ac-charger-2014.jpg", "wiki:Delta Electronics EV AC Charger 20140606.jpg"),
        ("commons-awt-70215aem.jpg", "wiki:Delta Electronics AWT-70215AEM 20161008.jpg"),
        ("catalog-ev-charging-tw.pdf", "https://filecenter.deltaww.com/Products/download/21/2101/Catalogue/EV%20Charging%20Solution_Catalog_TW_202103.pdf"),
    ],
    "evalue": [
        ("datasheet.pdf", "https://www.evalue.com.tw/upload/files/1760427543048.pdf"),
    ],
    "fronius": [
        ("commons-wattpilot-bregenz.jpg", "wiki:Bregenz-Vorarlberger Kraftwerke-Inverter Test bay-Fronius Wattpilot-01ASD.jpg"),
    ],
    "myenergi": [
        ("eeworld-zappi-teardown-article.html", "https://en.eeworld.com.cn/mp/EEWorld/a398869.jspx"),
    ],
    "charge-amps": [],
    "smappee": [],
    "huawei": [],
    "hypervolt": [
        ("commons-home-3-pro.jpg", "wiki:Hypervolt Home 3 Pro.jpg"),
    ],
    "ohme": [
        ("sdg-home-pro-teardown-thumb.jpg", "yt:1z6OCoxqJrE"),
    ],
}

LINKS: dict[str, list[tuple[str, str]]] = {
    "abb": [
        ("product photos / brochure", "https://new.abb.com/ev-charging/terra-ac-wallbox"),
        ("ADAC 2025 test (benchmark, joint 2nd / 1.7)", "https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/laden/wallboxen-fuer-dienstwagen-test/"),
        ("Wikimedia Category:ABB Terra AC", "https://commons.wikimedia.org/wiki/Category:ABB_Terra_AC"),
    ],
    "keba": [
        ("Wikimedia P30 category", "https://commons.wikimedia.org/wiki/Category:KEBA_KeContact_P30"),
        ("ADAC 2025 winner P40 (benchmark 1.6)", "https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/laden/wallboxen-fuer-dienstwagen-test/"),
        ("install manual exploded views / MID module", "https://www.keba.com/download/x/b7756bf6dd/kecontactp40mid_hbde.pdf"),
    ],
    "wallbox": [
        ("Munro Live teardown E4 Pulsar Plus", "https://www.youtube.com/watch?v=MBq81HjC00w"),
        ("Munro Live playlist EV Home Chargers Teardown", "https://www.youtube.com/playlist?list=PLkiDlGyJnprebWZT0AwEVKkhcmLYXUyoU"),
        ("FCC RFID module 2BB8L-RFID02", "https://fccid.io/2BB8L-RFID02"),
        ("MotorTrend Pulsar Plus photo gallery", "https://www.motortrend.com/reviews/wallbox-pulsar-plus-40a-48a-home-ev-charger-review/photos"),
    ],
    "easee": [
        ("eFIXX review — cover off / Chargeberry", "https://www.youtube.com/watch?v=e_aJRe5bf04"),
        ("eFIXX RCD internals test", "https://www.youtube.com/watch?v=r1VzrJVRgLo"),
        ("ADAC 2022 Easee Home note 1.9", "https://www.adac.de/"),
        ("install drawings", "https://download.easee.com/m/192768bcc61516ed/original/EN_PnP_IUG.pdf"),
    ],
    "zaptec": [
        ("BruCON 0x0F reverse-engineering / PCB photos in video", "https://www.youtube.com/watch?v=raZHd1Q4Vrc"),
        ("Wikimedia Zaptec Go product photos", "https://commons.wikimedia.org/wiki/File:Zaptec_Go.jpg"),
    ],
    "alfen": [
        ("Wikimedia Alfen Twin", "https://commons.wikimedia.org/wiki/Category:Alfen_Twin"),
        ("ADAC 2025 Eve Single Pro-line 1.9", "https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/laden/wallboxen-fuer-dienstwagen-test/"),
    ],
    "evbox": [
        ("Wikimedia EVBox stations", "https://commons.wikimedia.org/wiki/Category:Electric_vehicle_charging_stations_by_EVBox"),
    ],
    "mennekes": [
        ("Type 2 connector origin photos (CC)", "https://commons.wikimedia.org/wiki/Category:Type_2_connectors"),
        ("ADAC 2025 AMTRON 4Business 1.9", "https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/laden/wallboxen-fuer-dienstwagen-test/"),
    ],
    "go-e": [
        ("Zerobrain Gemini Flex 22 kW teardown (PCB, relays, RCD)", "https://www.youtube.com/watch?v=B0KHW3OnVRg"),
        ("PRO datasheet", "https://cdn.shopify.com/s/files/1/0729/7584/3675/files/go-e-charger-pro-datenblatt.pdf"),
        ("open API / community (evcc)", "https://docs.evcc.io/"),
    ],
    "heidelberg": [
        ("Amperfied (Heidelberg successor) product photos", "https://www.amperfied.com/"),
        ("Wikimedia Amperfied stations", "https://commons.wikimedia.org/wiki/Category:Amperfied_charging_stations"),
        ("ADAC Energy Control 2022 note 2.2", "https://www.adac.de/"),
    ],
    "abl": [
        ("Wikimedia ABL stations", "https://commons.wikimedia.org/wiki/Category:Electric_vehicle_charging_stations_by_ABL"),
        ("ADAC 2025 eM4 Single 1.9; eMH1 2018 1.0", "https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/laden/wallboxen-fuer-dienstwagen-test/"),
    ],
    "schneider-electric": [
        ("Wikimedia Schneider charging stations", "https://commons.wikimedia.org/wiki/Category:Schneider_Electric_charging_stations"),
        ("EVlink catalogue", "https://www.se.com/ww/en/product-range/22127-evlink/"),
    ],
    "siemens": [
        ("Wikimedia VersiCharge AC Series", "https://commons.wikimedia.org/wiki/File:Siemens_VersiCharge_AC_Series_Charging_Station.jpg"),
        ("VersiCharge product page", "https://www.siemens.com/global/en/products/energy/medium-voltage/systems/emobility/versicharge.html"),
    ],
    "tesla": [
        ("FCC Gen 3 internal photos 2AEIM-1470138", "https://fccid.io/2AEIM-1470138"),
        ("FCC Universal Wall Connector 2AEIM-1735511", "https://fccid.io/2AEIM-1735511"),
        ("Munro Live teardown E1 Tesla Wall Connector", "https://www.youtube.com/watch?v=4wVhiySuZw4"),
        ("ZDI PCB photos (STM32, ADE7854, AW-CU300)", "https://www.thezdi.com/blog/2024/12/16/detailing-the-attack-surfaces-of-the-tesla-wall-connector-ev-charger"),
        ("smart EMOTION teardown (contactors, CTs)", "https://www.smart-emotion.de/article/327-teardown-what-s-in-the-tesla-wallbox-and-how-does-it-work/"),
        ("TMC Gen3 disassembly / relay overheating", "https://teslamotorsclub.com/tmc/threads/gen3-hpwc-disassembly-with-overheating-issues-explained.223104/"),
        ("official internal components diagram", "https://energylibrary.tesla.com/docs/Public/Charging/WallConnector/Gen3/Install/J1772/en-us/GUID-AE1A657C-F246-448F-B847-616B0945C1CB.html"),
    ],
    "chargepoint": [
        ("ZDI Pwn2Own: Home Flex CPU (AT91SAM9N12) + Panda AC 50 metrology (MSP430)", "https://www.zerodayinitiative.com/blog/2023/11/28/a-detailed-look-at-pwn2own-automotive-ev-charger-hardware"),
        ("Wikimedia ChargePoint Home Charger", "https://commons.wikimedia.org/wiki/File:ChargePoint_Home_Charger.jpg"),
    ],
    "emporia": [
        ("FCC internal photos 2AS6P-EMEVSE1", "https://fccid.io/2AS6P-EMEVSE1"),
        ("ZDI: single-board ESP32 + MSP430F6736A", "https://www.zerodayinitiative.com/blog/2023/11/28/a-detailed-look-at-pwn2own-automotive-ev-charger-hardware"),
        ("Wirecutter 2026 top pick (benchmark)", "https://www.nytimes.com/wirecutter/reviews/best-electric-vehicle-chargers-for-home/"),
    ],
    "autel": [
        ("FCC internal photos 2A5NP-AUTELNEACL", "https://fccid.io/2A5NP-AUTELNEACL"),
        ("ZDI Autel Maxi PCB set (STM32, GD32, ESP32, Quectel EC25)", "https://www.zerodayinitiative.com/blog/2023/11/28/a-detailed-look-at-pwn2own-automotive-ev-charger-hardware"),
        ("spec sheets", "https://autelenergy.us/pages/downloads"),
    ],
    "delta": [
        ("Wikimedia Delta EV chargers", "https://commons.wikimedia.org/wiki/Category:Electric_vehicle_charging_stations_by_Delta_Electronics"),
    ],
    "evalue": [
        ("product photos / datasheet PDFs", "https://www.evalue.com.tw/"),
    ],
    "fronius": [
        ("Wattpilot product photos", "https://www.fronius.com/en/solar-energy/installers-partners/products-solutions/residential-energy/e-mobility/wattpilot"),
        ("ADAC 2023 Wattpilot Home 11 note 1.6", "https://www.adac.de/"),
        ("Wikimedia Wattpilot at VKW Bregenz", "https://commons.wikimedia.org/wiki/File:Bregenz-Vorarlberger_Kraftwerke-Inverter_Test_bay-Fronius_Wattpilot-01ASD.jpg"),
    ],
    "myenergi": [
        ("EEWorld Zappi 7 kW teardown (relays, RCD, CT, DC-DC)", "https://en.eeworld.com.cn/mp/EEWorld/a398869.jspx"),
        ("Zappi product photos", "https://www.myenergi.com/product/zappi/"),
    ],
    "charge-amps": [
        ("ADAC 2025 Dawn Professional DE joint 2nd / 1.7", "https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/laden/wallboxen-fuer-dienstwagen-test/"),
        ("product photos", "https://www.chargeamps.com/"),
    ],
    "smappee": [
        ("ADAC 2025 EV Wall Eichrecht 1.8", "https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/laden/wallboxen-fuer-dienstwagen-test/"),
        ("product photos", "https://www.smappee.com/ev-wall/"),
    ],
    "huawei": [
        ("FusionCharge product photos", "https://solar.huawei.com/"),
    ],
    "hypervolt": [
        ("Wikimedia Home 3 Pro colourways", "https://commons.wikimedia.org/wiki/File:Hypervolt_Home_3_Pro.jpg"),
        ("What Car? 2025 owner-survey winner", "https://www.thisismoney.co.uk/money/article-15306285/best-electric-vehicle-home-chargers_.html"),
    ],
    "ohme": [
        ("SDG #314 Home Pro teardown (PCB, Panasonic relays, CT)", "https://www.youtube.com/watch?v=1z6OCoxqJrE"),
        ("Speak EV Ohme cable teardown thread", "https://www.speakev.com/threads/ohme-smart-charging-cable-tests-and-teardown.146077/"),
        ("product photos", "https://www.ohme-ev.com/"),
    ],
}

WIKI_CACHE: dict[str, str] = {}


def wiki_original_url(filename: str) -> str | None:
    if filename in WIKI_CACHE:
        return WIKI_CACHE[filename]
    title = filename if filename.startswith("File:") else f"File:{filename}"
    api = (
        "https://commons.wikimedia.org/w/api.php?action=query"
        f"&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url|size|mime&format=json"
    )
    req = Request(api, headers={"User-Agent": UA})
    with urlopen(req, timeout=30, context=CTX) as r:
        data = json.loads(r.read().decode())
    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        infos = page.get("imageinfo") or []
        if infos and infos[0].get("url"):
            WIKI_CACHE[filename] = infos[0]["url"]
            return infos[0]["url"]
    return None


def resolve(url: str) -> list[str]:
    if url.startswith("wiki:"):
        resolved = wiki_original_url(url[5:])
        return [resolved] if resolved else []
    if url.startswith("yt:"):
        vid = url[3:]
        return [
            f"https://img.youtube.com/vi/{vid}/maxresdefault.jpg",
            f"https://img.youtube.com/vi/{vid}/hqdefault.jpg",
        ]
    return [url]


def looks_ok(data: bytes, dest: Path) -> bool:
    if len(data) < 800:
        return False
    head = data[:200].lower()
    if dest.suffix == ".pdf":
        if data[:5] != b"%PDF-":
            return False
    if dest.suffix in {".jpg", ".jpeg"}:
        if data[:3] != b"\xff\xd8\xff" and not (data[:4] == b"RIFF" and data[8:12] == b"WEBP"):
            return False
    if dest.suffix == ".png":
        if data[:8] != b"\x89PNG\r\n\x1a\n" and not (data[:4] == b"RIFF" and data[8:12] == b"WEBP"):
            return False
    if dest.suffix == ".webp":
        if not (data[:4] == b"RIFF" and data[8:12] == b"WEBP"):
            return False
    if dest.suffix in {".html", ".htm"}:
        if b"<html" not in head and b"<!doctype" not in head:
            return False
    if dest.suffix not in {".html", ".htm"} and (b"<html" in head or b"<!doctype html" in head):
        return False
    return True


def fetch_bytes(url: str) -> bytes | None:
    try:
        req = Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        with urlopen(req, timeout=60, context=CTX) as r:
            return r.read()
    except Exception as e:
        print(f"    fail {url[:90]} … {e}")
        return None


def fetch_to(url_spec: str, dest: Path) -> bool:
    for url in resolve(url_spec):
        if not url:
            continue
        data = fetch_bytes(url)
        if data is None:
            continue
        if not looks_ok(data, dest):
            print(f"    skip bad payload {dest.name} ({len(data)} bytes) from {url[:80]}")
            continue
        dest.write_bytes(data)
        print(f"    ok {dest.name} ({len(data)} bytes)")
        return True
    return False


def write_images_md(mid: str, saved: list[str]) -> None:
    links = LINKS.get(mid, [])
    lines = [
        f"# Images, teardowns, benchmarks — {mid}",
        "",
        "Local files. FCC exhibits are public US filings. Wikimedia files keep their original CC licence. ZDI photos are from published Pwn2Own hardware write-ups.",
        "",
        "## Local files",
        "",
    ]
    if saved:
        for s in saved:
            lines.append(f"- `{s}`")
    else:
        lines.append("- *(no binary downloaded — see links below)*")
    lines += ["", "## Teardown / internal / benchmark links", ""]
    for title, url in links:
        lines.append(f"- {title}: {url}")
    lines += [
        "",
        "## Notes",
        "",
        "- Full PCB teardowns are uncommon for EU wallboxes (KEBA / Alfen / Easee). Best internals: **FCC ID internal photos** (NA SKUs) and **Munro Live / BruCON / ZDI / Zerobrain** videos.",
        "- ADAC Dienstwagen-Wallboxentest 2025 is the main independent EU benchmark (notes 1.6–1.9). Photos from that test are not redistributed here.",
        "- Do not treat manufacturer brochure renders as teardowns.",
        "- YouTube files stored here are public video thumbnails used as a visual index of the teardown, not frame grabs of the PCB.",
        "",
    ]
    dest = MFG / mid / "images"
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "IMAGES.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    catalog = json.loads((ROOT / "charging-station-benchmark" / "catalog.json").read_text(encoding="utf-8"))
    ids = [m["id"] for m in catalog["manufacturers"]]
    summary = {}
    for mid in ids:
        imgdir = MFG / mid / "images"
        imgdir.mkdir(parents=True, exist_ok=True)
        saved: list[str] = []
        print(mid)
        for name, url in DOWNLOADS.get(mid, []):
            dest = imgdir / name
            if dest.exists() and dest.stat().st_size > 800:
                print(f"    keep {name}")
                saved.append(name)
                continue
            if fetch_to(url, dest):
                saved.append(name)
            elif dest.exists() and dest.stat().st_size < 800:
                dest.unlink(missing_ok=True)
        write_images_md(mid, saved)
        summary[mid] = saved
        print(f"  -> {len(saved)} files")
    print("\n=== SUMMARY ===")
    for mid, files in summary.items():
        print(f"{mid:22} {len(files):2}  {', '.join(files) or '(links only)'}")


if __name__ == "__main__":
    main()
