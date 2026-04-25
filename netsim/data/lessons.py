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
            "- MAC = RIADENIE PRÍSTUPU VIACERÝCH STANÍC K ZDIEĽANÉMU MÉDIU\n"
            "- CIEĽ: ELIMINÁCIA KOLÍZIÍ + EFEKTIVITA, SPRAVODLIVOSŤ, QOS\n"
            "- RANDOM A RIADENÝ PRÍSTUP\n"
            "- MULTIPLEXING A MODERNÉ PRÍSTUPY"
        ),
        preview=(
            "- RANDOM PRÍSTUP: ALOHA, SLOTTED ALOHA, CSMA\n"
            "- ALOHA -> VYSIELANIE KEDYKOĽVEK, KOLÍZIE -> BACKOFF\n"
            "- SLOTTED ALOHA -> ČASOVÉ SLOTY, VYŠŠIA EFEKTIVITA\n"
            "- CSMA -> POČÚVA MÉDIUM PRED VYSIELANÍM\n"
            "- CSMA/CD -> DETEKCIA KOLÍZIÍ (ETHERNET)\n"
            "- CSMA/CA -> VYHÝBANIE SA KOLÍZIÁM (WI-FI)\n"
            "- CSMA STRATÉGIE: 1-PERSISTENT, NON-PERSISTENT, P-PERSISTENT\n"
            "- CSMA/CA: LISTEN -> IFS -> BACKOFF -> VYSIELANIE -> ACK\n"
            "- RTS/CTS -> RIEŠENIE HIDDEN NODE PROBLÉMU\n"
            "- PROBLÉMY BEZDRÔTU: HIDDEN TERMINAL, EXPOSED TERMINAL, NEAR-FAR\n"
            "- RIADENÝ PRÍSTUP: REZERVÁCIA, POLLING, TOKEN PASSING\n"
            "- MULTIPLEXING: FDMA, TDMA, CDMA, OFDMA, SC-FDMA, NOMA"
        ),
        detail=(
            "Bezdrôtové prostredie je zdieľané a vyžaduje koordináciu prístupu medzi "
            "viacerými stanicami.\n\n"
            "Focus areas:\n"
            "- random vs riadený prístup\n"
            "- CSMA/CA a riešenie kolízií\n"
            "- problémy bezdrôtového média\n"
            "- FDMA, TDMA, CDMA, OFDMA, SC-FDMA a NOMA"
        ),
        ascii_header=LESSON_HEADERS["medium_access_control"],
    ),
    Lesson(
        key="mesh_routing",
        title="WIRELESS WIDE NETWORKS / MOBILE NETWORKS",
        description=(
            "- BUNKOVÉ SIETE = ROZDELENIE PRIESTORU NA BUNKY + REUSE FREKVENCIÍ\n"
            "- HEXAGONÁLNY MODEL A COLORING PROBLEM\n"
            "- VÝVOJ 1G AŽ 5G\n"
            "- ARCHITEKTÚRA 4G/5G A CORE NETWORK"
        ),
        preview=(
            "- BUNKOVÉ SIETE -> REUSE FREKVENCIÍ, RUŠENIE SUSEDNÝCH BUNIEK\n"
            "- ARCHITEKTÚRA: UE, BTS, BSC, MSC + CORE NETWORK\n"
            "- 1G = ANALÓG, OKRUHY\n"
            "- 2G = DIGITÁL, GSM, SMS, TDMA/FDMA\n"
            "- 2.5G = GPRS (PAKETY), EDGE (VYŠŠIA RÝCHLOSŤ)\n"
            "- 3G = UMTS, MULTIMÉDIÁ, NODEB + RNC\n"
            "- 4G = LTE, PLNE IP, PACKET SWITCHING\n"
            "- 5G = VYSOKÉ RÝCHLOSTI, NÍZKA LATENCIA, IOT\n"
            "- 4G EPC: HSS, MME, SGW, PCRF, IMS\n"
            "- 5G: SBA, CUPS, NF (AMF, SMF, UPF, AUSF), NETWORK SLICING\n"
            "- 4G VS 5G SIGNALIZÁCIA: DIAMETER -> HTTP/2 + REST\n"
            "- SDN: NORTHBOUND VS SOUTHBOUND API, REST, OPENFLOW\n"
            "- SIMULÁCIE: UERANSIM, OPEN-SOURCE 5G STACK"
        ),
        detail=(
            "Mobilné siete umožňujú bezdrôtový prístup na veľké vzdialenosti pomocou "
            "bunkovej architektúry a evolúcie od 1G po 5G.\n\n"
            "Focus areas:\n"
            "- bunkový model a reuse frekvencií\n"
            "- vývoj generácií 1G až 5G\n"
            "- 4G EPC a 5G service-based architektúra\n"
            "- network slicing, SDN a simulácie"
        ),
        ascii_header=LESSON_HEADERS["mesh_routing"],
    ),
    Lesson(
        key="wsn_iot",
        title="WIRELESS MESH NETWORKS (SMEROVANIE)",
        description=(
            "- MULTI-HOP SIETE = KOMUNIKÁCIA CEZ MEDZILEHLÉ UZLY\n"
            "- WMN VS AD HOC\n"
            "- ROUTING PROTOKOLY\n"
            "- DEZENTRALIZOVANÉ SMEROVANIE"
        ),
        preview=(
            "- WMN -> ROUTING ROBIA ŠPECIÁLNE ROUTERY\n"
            "- AD HOC -> ROUTING ROBIA SAMOTNÉ UZLY\n"
            "- VLASTNOSTI AD HOC: DYNAMICKÁ TOPOLOGIA, ŽIADNY CENTRÁLNY UZOL, NÍZKA ENERGIA\n"
            "- TYPY ROUTINGU: PROAKTÍVNE, REAKTÍVNE, HYBRIDNÉ, HIERARCHICKÉ\n"
            "- DV: LEN INFO OD SUSEDOV, PROBLÉM CYKLY A COUNT-TO-INFINITY\n"
            "- DSDV -> SEQUENCE NUMBERS PROTI CYKLOM\n"
            "- DSR -> SOURCE ROUTING, RREQ -> RREP\n"
            "- AODV -> TABUĽKY LEN PRE AKTÍVNE CESTY, RREQ / RREP / RERR\n"
            "- HWMP -> HYBRID PRE WI-FI MESH, AIRTIME METRIKA\n"
            "- B.A.T.M.A.N -> L2 ROUTING, SELF-HEALING, DEZENTRALIZOVANÝ\n"
            "- RPL -> IOT SIETE, DODAG STROM, ENERGETICKÁ EFEKTIVITA"
        ),
        detail=(
            "Mesh a ad hoc siete využívajú viacskokový prenos a decentralizované "
            "smerovanie medzi uzlami.\n\n"
            "Focus areas:\n"
            "- multi-hop komunikácia a forwarding\n"
            "- WMN vs ad hoc prístup k routingu\n"
            "- proaktívne, reaktívne a hybridné protokoly\n"
            "- DSDV, DSR, AODV, HWMP, B.A.T.M.A.N a RPL"
        ),
        ascii_header=LESSON_HEADERS["wsn_iot"],
    ),
    Lesson(
        key="short_range",
        title="WIRELESS SENSOR NETWORKS (ZIGBEE, 802.15.4)",
        description=(
            "- WSN = VEĽA JEDNODUCHÝCH UZLOV, NÍZKA SPOTREBA, MALÉ DÁTA\n"
            "- HLAVNÝ CIEĽ: VÝDRŽ BATÉRIE, NIE VÝKON\n"
            "- IEEE 802.15.4\n"
            "- ZIGBEE A THREAD"
        ),
        preview=(
            "- 802.15.4 RIEŠI LEN PHY + MAC\n"
            "- MALÉ RÁMCE (127 B MAX), NÍZKE RÝCHLOSTI, NÍZKA SPOTREBA\n"
            "- PHY: PÁSMA 868 / 915 / 2.4 GHZ, CCA, CRC, KANÁLY\n"
            "- MAC: CSMA/CA, ACK VS SPOTREBA, BEACON VS NON-BEACON, GTS\n"
            "- ZARIADENIA: FFD VS RFD\n"
            "- ROLY: COORDINATOR / ROUTER / END DEVICE\n"
            "- ZIGBEE -> NETWORK LAYER + ROUTING, TOPOLOGIE STAR / TREE / MESH\n"
            "- THREAD -> IP-BASED (IPV6 + 6LOWPAN), MESH ROUTING (RPL)\n"
            "- THREAD ROLY: LEADER, ROUTER, END DEVICE\n"
            "- BORDER ROUTER = PREPOJENIE DO IP SIETE"
        ),
        detail=(
            "Senzorové siete sú navrhnuté pre nízku spotrebu, malé objemy dát a dlhú "
            "výdrž batérie.\n\n"
            "Focus areas:\n"
            "- 802.15.4 PHY a MAC vrstva\n"
            "- roly zariadení a energetická efektivita\n"
            "- Zigbee topológie a routing\n"
            "- Thread, 6LoWPAN, RPL a border router"
        ),
        ascii_header=LESSON_HEADERS["short_range"],
    ),
    Lesson(
        key="wifi_networks",
        title="WIRELESS PERSONAL AREA NETWORKS (BLUETOOTH)",
        description=(
            "- WPAN = KRÁTKY DOSAH, NÍZKA SPOTREBA, JEDNODUCHÉ ZARIADENIA\n"
            "- BLUETOOTH V 2.4 GHZ ISM PÁSME\n"
            "- BR/EDR VS BLE\n"
            "- TOPOLÓGIA A BEZPEČNOSŤ"
        ),
        preview=(
            "- BLUETOOTH -> AD-HOC KOMUNIKÁCIA (PICONET), KRÁTKY DOSAH, NÍZKY VÝKON\n"
            "- 2 HLAVNÉ VETVY: BR/EDR = AUDIO, BLE = IOT A SENZORY\n"
            "- PICONET = 1 PRIMARY + MAX 7 ACTIVE SECONDARY\n"
            "- SCATTERNET = VIAC PREPOJENÝCH PICONETOV\n"
            "- PRÍSTUP K MÉDIU: TDD + SLOTY 625 US, PRIMARY RIADI KOMUNIKÁCIU\n"
            "- ŽIADNE CSMA\n"
            "- RF: FHSS, 79 KANÁLOV, 1600 HOPS/S\n"
            "- FHSS ZNIŽUJE INTERFERENCIE\n"
            "- LOGICKÉ SPOJE: SCO = HLAS, ACL = DÁTA + ARQ\n"
            "- BEZPEČNOSŤ: PAIRING -> LINK KEY, AUTENTIZÁCIA, ŠIFROVANIE"
        ),
        detail=(
            "WPAN technológie slúžia na spojenie jednoduchých zariadení na krátku "
            "vzdialenosť s dôrazom na nízky výkon a jednoduchú komunikáciu.\n\n"
            "Focus areas:\n"
            "- Bluetooth BR/EDR a BLE\n"
            "- piconet, scatternet a prístup k médiu\n"
            "- FHSS, SCO a ACL spoje\n"
            "- pairing, autentizácia a šifrovanie"
        ),
        ascii_header=LESSON_HEADERS["wifi_networks"],
    ),
    Lesson(
        key="mobile_networks",
        title="WIRELESS LOCAL AREA NETWORKS (WI-FI, 802.11)",
        description=(
            "- WI-FI = BEZDRÔTOVÁ LAN TECHNOLÓGIA (IEEE 802.11)\n"
            "- DOMINANTNÉ PRIPOJENIE ZARIADENÍ\n"
            "- BSS / ESS / DS ARCHITEKTÚRA\n"
            "- PHY, MAC A BEZPEČNOSŤ"
        ),
        preview=(
            "- ZÁKLADNÉ VLASTNOSTI: TDD, POLODUPLEX, ROAMING MEDZI AP\n"
            "- TOPOLOGIE: INFRAŠTRUKTÚRNA (AP) A AD-HOC (IBSS)\n"
            "- PRÍSTUP K MÉDIU: CSMA/CA (DCF), ACK + BACKOFF\n"
            "- RTS/CTS RIEŠI HIDDEN NODE\n"
            "- MAC RÁMEC: AŽ 4 ADRESY, TO DS / FROM DS URČUJÚ SMER\n"
            "- ROAMING: SCANNING -> AUTENTIZÁCIA -> ASOCIÁCIA\n"
            "- L2 VS L3 ROAMING\n"
            "- PHY: OFDM, DSSS, RÔZNE GENERÁCIE WI-FI\n"
            "- BEZPEČNOSŤ: WEP, WPA, WPA2, WPA3\n"
            "- 4-WAY HANDSHAKE, PMK -> PTK"
        ),
        detail=(
            "Wi‑Fi siete patria medzi najbežnejšie bezdrôtové LAN technológie a tvoria "
            "základ lokálneho bezdrôtového pripojenia.\n\n"
            "Focus areas:\n"
            "- architektúra BSS, ESS a DS\n"
            "- CSMA/CA, roaming a MAC rámce\n"
            "- PHY vrstvy a generácie 802.11\n"
            "- WPA2/WPA3 a 4-way handshake"
        ),
        ascii_header=LESSON_HEADERS["mobile_networks"],
    ),
)
