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
        title="INTRODUCTION TO WIRELESS NETWORKS",
        description=(
            "- WHAT WIRELESS NETWORKS ARE\n"
            "- HOW THEY DIFFER FROM WIRED SYSTEMS\n"
            "- MAIN BENEFITS\n"
            "- MAIN LIMITATIONS"
        ),
        preview=(
            "This lesson introduces the core idea of wireless communication and how data is "
            "transmitted without physical cables. You will learn the basic components of "
            "wireless systems and how devices communicate over the air. The focus is on "
            "understanding the environment and constraints of wireless networking."
        ),
        detail=(
            "Wireless networks exchange data through electromagnetic waves rather than fixed cables.\n\n"
            "Focus areas:\n"
            "- what wireless networks are\n"
            "- why they differ from wired networks\n"
            "- key benefits and limitations\n\n"
            "This lesson screen is the placeholder for the full interactive content."
        ),
        ascii_header=LESSON_HEADERS["intro_wireless"],
    ),
    Lesson(
        key="types_topologies",
        title="NETWORK TYPES AND TOPOLOGIES",
        description=(
            "- WPAN\n"
            "- WLAN\n"
            "- WSN\n"
            "- WWAN\n"
            "- INFRASTRUCTURE VS AD HOC\n"
            "- SINGLE-HOP VS MULTI-HOP\n"
            "- STAR\n"
            "- TREE\n"
            "- MESH"
        ),
        preview=(
            "This section explains how networks are structured and categorized. You will "
            "learn about different network types (LAN, WAN, PAN) and topologies such as "
            "star, mesh, and bus. The goal is to understand how design choices affect "
            "performance, reliability, and scalability."
        ),
        detail=(
            "Wireless systems come in several scales and shapes.\n\n"
            "Focus areas:\n"
            "- WPAN, WLAN, WSN, WWAN\n"
            "- infrastructure vs ad hoc\n"
            "- single-hop vs multi-hop\n"
            "- star, tree, mesh basics"
        ),
        ascii_header=LESSON_HEADERS["types_topologies"],
    ),
    Lesson(
        key="radio_signal_basics",
        title="RADIO AND SIGNAL BASICS",
        description=(
            "- FREQUENCY\n"
            "- WAVELENGTH\n"
            "- BANDWIDTH\n"
            "- SIGNAL STRENGTH\n"
            "- SNR\n"
            "- BASIC CAPACITY INTUITION"
        ),
        preview=(
            "Here you explore how wireless communication relies on electromagnetic waves. "
            "You will learn about frequency, wavelength, signal strength, and noise. "
            "This lesson builds the physical foundation needed to understand wireless behavior."
        ),
        detail=(
            "Radio communication depends on how signals occupy spectrum and survive noise.\n\n"
            "Focus areas:\n"
            "- frequency\n"
            "- wavelength\n"
            "- bandwidth\n"
            "- signal strength / SNR\n"
            "- very basic capacity intuition"
        ),
        ascii_header=LESSON_HEADERS["radio_signal_basics"],
    ),
    Lesson(
        key="wireless_propagation",
        title="WIRELESS PROPAGATION",
        description=(
            "- PATH LOSS\n"
            "- INTERFERENCE\n"
            "- FADING\n"
            "- LOS VS NLOS\n"
            "- MULTIPATH BASICS"
        ),
        preview=(
            "This lesson focuses on how signals travel through real environments. You will "
            "learn about attenuation, reflection, diffraction, and interference. The goal "
            "is to understand why signal strength and quality change over distance and obstacles."
        ),
        detail=(
            "Signals weaken, reflect, scatter, and interfere with each other as they move through space.\n\n"
            "Focus areas:\n"
            "- path loss\n"
            "- interference\n"
            "- fading\n"
            "- LOS vs NLOS\n"
            "- multipath basics"
        ),
        ascii_header=LESSON_HEADERS["wireless_propagation"],
    ),
    Lesson(
        key="medium_access_control",
        title="MEDIUM ACCESS CONTROL",
        description=(
            "- SHARED MEDIUM CONCEPT\n"
            "- COLLISIONS\n"
            "- CSMA/CA\n"
            "- BACKOFF\n"
            "- CHANNEL ACCESS BASICS"
        ),
        preview=(
            "This section explains how multiple devices share the same wireless medium. "
            "You will learn how collisions occur and how protocols like CSMA/CA help "
            "avoid them. The key idea is coordination in a shared and unpredictable environment."
        ),
        detail=(
            "Because everyone uses the same air, wireless systems need rules for who speaks and when.\n\n"
            "Focus areas:\n"
            "- shared medium concept\n"
            "- collisions\n"
            "- CSMA/CA\n"
            "- backoff\n"
            "- channel access basics"
        ),
        ascii_header=LESSON_HEADERS["medium_access_control"],
    ),
    Lesson(
        key="mesh_routing",
        title="MESH AND AD HOC ROUTING",
        description=(
            "- MULTI-HOP FORWARDING\n"
            "- ROUTE DISCOVERY\n"
            "- PROACTIVE VS REACTIVE ROUTING\n"
            "- DSDV INTUITION\n"
            "- DSR INTUITION\n"
            "- AODV INTUITION"
        ),
        preview=(
            "This lesson introduces decentralized network structures where devices "
            "communicate directly. You will learn how routing works without a central "
            "controller. The focus is on flexibility, resilience, and dynamic topology changes."
        ),
        detail=(
            "Ad hoc and mesh systems rely on nodes forwarding for one another across multiple hops.\n\n"
            "Focus areas:\n"
            "- multi-hop forwarding\n"
            "- route discovery\n"
            "- proactive vs reactive routing\n"
            "- DSDV / DSR / AODV intuition"
        ),
        ascii_header=LESSON_HEADERS["mesh_routing"],
    ),
    Lesson(
        key="wsn_iot",
        title="WIRELESS SENSOR NETWORKS AND IOT",
        description=(
            "- LOW-POWER DESIGN\n"
            "- SLEEPY DEVICES\n"
            "- COORDINATOR\n"
            "- ROUTER\n"
            "- END DEVICE\n"
            "- 802.15.4\n"
            "- ZIGBEE\n"
            "- THREAD"
        ),
        preview=(
            "This section explores networks made of many small, low-power devices. You "
            "will learn about energy constraints, data collection, and scalability challenges. "
            "The lesson highlights how IoT systems operate in real-world scenarios."
        ),
        detail=(
            "Sensor and IoT networks optimize for long battery life, small frames, and lightweight protocols.\n\n"
            "Focus areas:\n"
            "- low-power design\n"
            "- sleepy devices\n"
            "- coordinator / router / end device\n"
            "- 802.15.4, ZigBee, Thread overview"
        ),
        ascii_header=LESSON_HEADERS["wsn_iot"],
    ),
    Lesson(
        key="short_range",
        title="SHORT-RANGE WIRELESS TECHNOLOGIES",
        description=(
            "- NFC BASICS\n"
            "- BLUETOOTH\n"
            "- WPAN ROLE\n"
            "- VERY SHORT-RANGE USE CASES"
        ),
        preview=(
            "This lesson covers technologies like Bluetooth, NFC, and ZigBee. You will "
            "learn their use cases, limitations, and trade-offs. The goal is to understand "
            "when and why each technology is used."
        ),
        detail=(
            "Short-range systems prioritize convenience, low power, and close-proximity interactions.\n\n"
            "Focus areas:\n"
            "- NFC basics\n"
            "- Bluetooth / WPAN role\n"
            "- very short-range communication use cases"
        ),
        ascii_header=LESSON_HEADERS["short_range"],
    ),
    Lesson(
        key="wifi_networks",
        title="WI-FI NETWORKS",
        description=(
            "- ACCESS POINTS\n"
            "- CLIENTS\n"
            "- CHANNELS\n"
            "- 2.4 GHZ\n"
            "- 5 GHZ\n"
            "- 6 GHZ\n"
            "- COVERAGE VS THROUGHPUT"
        ),
        preview=(
            "This section focuses on how modern wireless LANs operate. You will learn "
            "about access points, channels, interference, and performance factors. The "
            "lesson connects theory with practical Wi-Fi deployment concepts."
        ),
        detail=(
            "Wi-Fi networks balance coverage, interference, channel width, and client density.\n\n"
            "Focus areas:\n"
            "- access points and clients\n"
            "- channels\n"
            "- 2.4 GHz vs 5 GHz vs 6 GHz\n"
            "- coverage vs throughput intuition"
        ),
        ascii_header=LESSON_HEADERS["wifi_networks"],
    ),
    Lesson(
        key="mobile_networks",
        title="MOBILE NETWORKS",
        description=(
            "- CELLULAR CONCEPT\n"
            "- LTE / 4G BASICS\n"
            "- 5G BASICS\n"
            "- HANDOVER\n"
            "- CORE-NETWORK INTUITION"
        ),
        preview=(
            "This lesson explains how cellular networks enable wide-area wireless "
            "communication. You will learn about network generations, cell structure, "
            "and mobility management. The focus is on how large-scale wireless systems "
            "are designed and operated."
        ),
        detail=(
            "Mobile networks scale wireless access across large regions using cells, cores, and mobility control.\n\n"
            "Focus areas:\n"
            "- cellular concept\n"
            "- LTE / 4G basics\n"
            "- 5G basics\n"
            "- handover and core-network intuition"
        ),
        ascii_header=LESSON_HEADERS["mobile_networks"],
    ),
)
