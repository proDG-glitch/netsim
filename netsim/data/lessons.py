"""Lesson definitions for NetSim."""

from __future__ import annotations

from dataclasses import dataclass

from netsim.data.lesson_headers import LESSON_HEADERS


@dataclass(frozen=True)
class Lesson:
    key: str
    title: str
    description: str
    preview: str
    detail: str
    ascii_header: str | None = None


LESSONS = (
    Lesson(
        key="intro_wireless",
        title="ÚVOD",
        description=(
            "- ZÁKLADNÁ ORIENTÁCIA V PREDMETE\n"
            "- ČO SÚ BEZDRÔTOVÉ SIETE\n"
            "- HLAVNÉ OBLASTI KURZU\n"
            "- PREHĽAD TÉM"
        ),
        preview=(
            "- GUIDED VS UNGUIDED (KABEL VS VZDUCH + ANTÉNY)\n"
            "- VLASTNOSTI: DYNAMICKÁ TOPOLOGIE, ŠUM/INTERFERENCE, SDÍLENÉ MÉDIUM\n"
            "- VÝHODY: MOBILITA, JEDNODUCHÉ NASAZENÍ\n"
            "- OSI BASICS: FYZICKÁ (BITY), LINKOVÁ (RÁMCE), SÍŤOVÁ (PAKETY), TRANSPORTNÍ (SEGMENTY)\n"
            "- ARCHITEKTURY: INFRASTRUCTURE VS AD HOC VS HYBRID\n"
            "- TYPY SÍTÍ: WWAN, WMAN, WLAN, WPAN, WSN\n"
            "- SINGLE-HOP VS MULTI-HOP\n"
            "- MANET, WSN, IOT (GATEWAY NUTNÁ)\n"
            "- NEVÝHODY: INTERFERENCE, LATENCE, NIŽŠÍ BEZPEČNOST"
        ),
        detail=(
            "Táto lekcia predstavuje úvod do problematiky bezdrôtových sietí.\n\n"
            "Focus areas:\n"
            "- základná terminológia\n"
            "- prehľad technológií\n"
            "- štruktúra tém kurzu"
        ),
        ascii_header=LESSON_HEADERS["intro_wireless"],
    ),
    Lesson(
        key="types_topologies",
        title="ZÁKLADY PRENOSU DÁT",
        description=(
            "- PRENOS DÁT\n"
            "- KANÁL A MÉDIUM\n"
            "- RÝCHLOSŤ A LATENCIA\n"
            "- ZÁKLADNÉ POJMY"
        ),
        preview=(
            "- SIGNÁL = NOSIČ INFORMACE (ČASOVÁ ZMĚNA VLASTNOSTÍ MÉDIA)\n"
            "- ELEKTROMAGNETICKÉ VLNĚNÍ: VLNOVÁ DÉLKA, FREKVENCE, RYCHLOST\n"
            "- KÓDOVÁNÍ = PŘEVOD DAT DO FORMY VHODNÉ PRO PŘENOS\n"
            "- DATA VS SIGNÁLY: ANALOGOVÉ I DIGITÁLNÍ, VŽDY SE PŘEVÁDÍ NA EM SIGNÁL\n"
            "- DECIBEL (DB) = LOGARITMICKÁ MÍRA POMĚRU VÝKONŮ\n"
            "- SNR = POMĚR SIGNÁLU K ŠUMU, URČUJE MAX RYCHLOST\n"
            "- ŠUM -> CHYBY V PŘENOSU, VYŠŠÍ RYCHLOST = VYŠŠÍ BER\n"
            "- ŠÍŘKA PÁSMA -> OVLIVŇUJE MAXIMÁLNÍ PŘENOSOVOU RYCHLOST\n"
            "- NYQUIST (BEZ ŠUMU), SHANNON (SE ŠUMEM)\n"
            "- PŘEPOJOVÁNÍ OKRUHŮ VS PAKETŮ (GARANCE VS FLEXIBILITA)\n"
            "- ACK, TIMEOUT, ARQ = SPOLEHLIVÝ PŘENOS DAT"
        ),
        detail=(
            "Táto lekcia sa venuje základom prenosu dát a súvisiacim pojmom.\n\n"
            "Focus areas:\n"
            "- médium a kanál\n"
            "- prenosová rýchlosť\n"
            "- latencia a spoľahlivosť"
        ),
        ascii_header=LESSON_HEADERS["types_topologies"],
    ),
    Lesson(
        key="radio_signal_basics",
        title="NFC",
        description=(
            "- NEAR FIELD COMMUNICATION\n"
            "- KRÁTKA VZDIALENOSŤ\n"
            "- PÁROVANIE A IDENTIFIKÁCIA\n"
            "- PRAKTICKÉ POUŽITIE"
        ),
        preview=(
            "- NFC = PODMNOŽINA RFID, 13.56 MHZ, ISO/IEC 14443\n"
            "- FUNGUJE NA PRINCÍPE MAGNETICKEJ INDUKCIE (CIEVKY, LC OBVOD), NIE KLASICKEJ EM VLNY\n"
            "- VEĽMI KRÁTKY DOSAH (~4 CM)\n"
            "- ROZDIEL NFC VS UHF RFID (INDUKCIA VS EM VLNA)\n"
            "REŽIMY NFC:\n"
            "- READER/WRITER (ČÍTANIE TAGOV, NDEF)\n"
            "- CARD EMULATION (MOBIL AKO KARTA, APDU)\n"
            "- PEER-TO-PEER (2 ZARIADENIA, LLCP)\n"
            "- TYPY NFC TAGOV (TYPE 2, 3, 4, 5) + RÝCHLOSTI (106–848 KBPS)\n"
            "HCE VS SECURE ELEMENT:\n"
            "- HCE = SOFTWARE, OS, MENEJ BEZPEČNÉ\n"
            "- SE = DEDIKOVANÝ ČIP, BEZPEČNÉ ULOŽENIE KĽÚČOV\n"
            "ISO 14443 STACK:\n"
            "- FYZICKÁ VRSTVA (RF, 13.56 MHZ)\n"
            "- ANTI-COLLISION / ACTIVATION\n"
            "- TRANSPORT (ISO-DEP)\n"
            "- APLIKÁCIA (APDU, ISO 7816)\n"
            "PRIEBEH KOMUNIKÁCIE:\n"
            "- REQA -> SELECT -> RATS -> APDU (AID, READ, AC)"
        ),
        detail=(
            "NFC je technológia pre komunikáciu na veľmi krátku vzdialenosť.\n\n"
            "Focus areas:\n"
            "- princíp blízkeho poľa\n"
            "- jednoduchá výmena dát\n"
            "- typické scenáre použitia"
        ),
        ascii_header=LESSON_HEADERS["radio_signal_basics"],
    ),
    Lesson(
        key="wireless_propagation",
        title="BEZDRÁTOVÝ PRENOS DAT",
        description=(
            "- RÁDIOVÝ PRENOS\n"
            "- ŠÍRENIE SIGNÁLU\n"
            "- RUŠENIE\n"
            "- PARAMETRE PRENOSU"
        ),
        preview=(
            "- EM SPEKTRUM: RÁDIOVÉ VLNY, MIKROVLNY (HLAVNÉ PRE KOMUNIKÁCIU)\n"
            "- NÍZKE FREKVENCIE -> DLHÝ DOSAH, PRECHÁDZAJÚ PREKÁŽKAMI\n"
            "- VYSOKÉ FREKVENCIE -> VYŠŠIA KAPACITA, MENŠÍ DOSAH, CITLIVÉ NA PREKÁŽKY\n"
            "- HF SA ODRÁŽA OD IONOSFÉRY, VHF/MIKROVLNY = LINE-OF-SIGHT\n"
            "- ANTÉNY: PREVOD ELEKTRICKÁ <-> EM ENERGIA, SMEROVÉ VS VŠESMEROVÉ\n"
            "- VYŠŠÍ ZISK = SÚSTREDENIE ENERGIE, NIE JEJ ZVÝŠENIE\n"
            "- ÚTLM RASTIE SO VZDIALENOSŤOU A FREKVENCIOU\n"
            "- MULTIPATH -> INTERFERENCIA (MÔŽE ZLEPŠIŤ AJ ZHORŠIŤ SIGNÁL)\n"
            "- DOPPLER -> ZMENA FREKVENCIE PRI POHYBE\n"
            "- ISI = PREKRYV SYMBOLOV KVÔLI ONESKORENIU\n"
            "- RIEŠENIE: GUARD INTERVAL, CYCLIC PREFIX (OFDM)\n"
            "- MIMO -> VIAC ANTÉN, VYŠŠIA KAPACITA BEZ VÄČŠIEHO PÁSMA"
        ),
        detail=(
            "Bezdrôtový prenos dát závisí od vlastností média a podmienok šírenia.\n\n"
            "Focus areas:\n"
            "- kvalita signálu\n"
            "- rušenie a dosah\n"
            "- praktické obmedzenia"
        ),
        ascii_header=LESSON_HEADERS["wireless_propagation"],
    ),
    Lesson(
        key="medium_access_control",
        title="ŘÍZENÍ PŘÍSTUPU K BEZDRÁTOVÉMU MÉDIU",
        description=(
            "- SDÍLENÉ MÉDIUM\n"
            "- KOLIZE\n"
            "- CSMA/CA\n"
            "- ZÁKLADY PŘÍSTUPU K MÉDIU"
        ),
        preview=(
            "Lekcia sa zameriava na pravidlá, podľa ktorých sa viaceré zariadenia delia o "
            "rovnaké bezdrôtové médium."
        ),
        detail=(
            "Bezdrôtové prostredie je zdieľané a vyžaduje koordináciu prístupu.\n\n"
            "Focus areas:\n"
            "- kolízie\n"
            "- vyhýbanie sa kolíziám\n"
            "- základné MAC princípy"
        ),
        ascii_header=LESSON_HEADERS["medium_access_control"],
    ),
    Lesson(
        key="mesh_routing",
        title="WIRELESS WIDE NETWORKS / MOBILE NETWORKS",
        description=(
            "- LTE\n"
            "- 5G\n"
            "- BUNKOVÉ SIETE\n"
            "- MOBILITA"
        ),
        preview=(
            "Táto lekcia pokrýva širokoplošné mobilné siete, ich generácie a základné "
            "vlastnosti moderných bunkových systémov."
        ),
        detail=(
            "Mobilné siete umožňujú bezdrôtový prístup na veľké vzdialenosti.\n\n"
            "Focus areas:\n"
            "- LTE a 5G\n"
            "- bunková architektúra\n"
            "- mobilita používateľa"
        ),
        ascii_header=LESSON_HEADERS["mesh_routing"],
    ),
    Lesson(
        key="wsn_iot",
        title="WIRELESS MESH NETWORKS (SMEROVANIE)",
        description=(
            "- MULTI-HOP\n"
            "- FORWARDING\n"
            "- ROUTING\n"
            "- MESH TOPOLOGY"
        ),
        preview=(
            "Lekcia predstavuje mesh siete a smerovanie v decentralizovanom bezdrôtovom "
            "prostredí."
        ),
        detail=(
            "Mesh siete využívajú viacskokový prenos a smerovanie medzi uzlami.\n\n"
            "Focus areas:\n"
            "- multi-hop komunikácia\n"
            "- objavovanie trás\n"
            "- odolnosť topológie"
        ),
        ascii_header=LESSON_HEADERS["wsn_iot"],
    ),
    Lesson(
        key="short_range",
        title="WIRELESS SENSOR NETWORKS (ZIGBEE, 802.15.4)",
        description=(
            "- ZIGBEE\n"
            "- 802.15.4\n"
            "- NÍZKA SPOTREBA\n"
            "- SENZOROVÉ UZLY"
        ),
        preview=(
            "Táto časť sa venuje senzorovým sieťam, nízkoenergetickému prenosu a rodine "
            "technológií okolo Zigbee a IEEE 802.15.4."
        ),
        detail=(
            "Senzorové siete sú navrhnuté pre nízku spotrebu a jednoduchú komunikáciu.\n\n"
            "Focus areas:\n"
            "- 802.15.4\n"
            "- Zigbee\n"
            "- nízkoenergetické uzly"
        ),
        ascii_header=LESSON_HEADERS["short_range"],
    ),
    Lesson(
        key="wifi_networks",
        title="WIRELESS PERSONAL AREA NETWORKS (BLUETOOTH)",
        description=(
            "- BLUETOOTH\n"
            "- WPAN\n"
            "- PÁROVANIE\n"
            "- KRÁTKA VZDIALENOSŤ"
        ),
        preview=(
            "Lekcia sa sústreďuje na osobné bezdrôtové siete a hlavne technológiu Bluetooth."
        ),
        detail=(
            "WPAN technológie slúžia na spojenie zariadení na krátku vzdialenosť.\n\n"
            "Focus areas:\n"
            "- Bluetooth\n"
            "- párovanie zariadení\n"
            "- typické použitie WPAN"
        ),
        ascii_header=LESSON_HEADERS["wifi_networks"],
    ),
    Lesson(
        key="mobile_networks",
        title="WIRELESS LOCAL AREA NETWORKS (WI-FI, 802.11)",
        description=(
            "- WI-FI\n"
            "- IEEE 802.11\n"
            "- ACCESS POINT\n"
            "- KANÁLY A PÁSMA"
        ),
        preview=(
            "Záverečná lekcia pokrýva lokálne bezdrôtové siete Wi‑Fi a základné princípy "
            "štandardu 802.11."
        ),
        detail=(
            "Wi‑Fi siete patria medzi najbežnejšie bezdrôtové LAN technológie.\n\n"
            "Focus areas:\n"
            "- 802.11 rodina štandardov\n"
            "- access point a klienti\n"
            "- pásma a kanály"
        ),
        ascii_header=LESSON_HEADERS["mobile_networks"],
    ),
)
