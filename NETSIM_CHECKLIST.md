# NetSim Build Checklist

Use this as the step-by-step implementation checklist for NetSim.

## Build Order

- [ ] Build the UI framework with split panels and reusable screen layout
- [ ] Implement Foundations
- [ ] Implement Radio & Signal Basics
- [ ] Implement Mesh & Ad Hoc Routing
- [ ] Implement WSN / IoT
- [ ] Implement WPAN / NFC
- [ ] Implement WWAN
- [ ] Implement WLAN
- [ ] Implement Quiz / Challenge Mode

## Content Structure

### 1. Foundations

- [ ] Add Infrastructure vs Ad hoc
- [ ] Add Single-hop vs Multi-hop
- [ ] Add network types: WPAN, WLAN, WSN, WWAN
- [ ] Add OSI relevance

### 2. Radio & Signal Basics

- [ ] Add frequency, wavelength, and bandwidth
- [ ] Add SNR and capacity basics using Nyquist/Shannon
- [ ] Add modulation basics: ASK, FSK, PSK, QAM
- [ ] Add spectrum overview

### 3. Propagation & Antennas

- [ ] Add path loss and distance effect
- [ ] Add multipath and fading
- [ ] Add LOS vs NLOS
- [ ] Add omni vs directional antennas

### 4. Medium Access (MAC)

- [ ] Add CSMA/CA
- [ ] Add ALOHA basics
- [ ] Add FDMA, TDMA, CDMA, OFDMA
- [ ] Add collisions and backoff

### 5. Mesh & Ad Hoc Routing

- [ ] Add multi-hop routing
- [ ] Add distance vector basics and count-to-infinity
- [ ] Add DSDV
- [ ] Add DSR
- [ ] Add AODV
- [ ] Add Mesh vs MANET

### 6. WSN / IoT (802.15.4, ZigBee, Thread)

- [ ] Add node roles: coordinator, router, end device
- [ ] Add sleep cycles
- [ ] Add 127-byte frame limits
- [ ] Add ZigBee vs Thread
- [ ] Add 6LoWPAN basics

### 7. WPAN / NFC

- [ ] Add near-field communication at 13.56 MHz
- [ ] Add modes: reader/writer, peer-to-peer, card emulation
- [ ] Add HCE vs Secure Element

### 8. WLAN (Wi-Fi)

- [ ] Add AP + clients using the infrastructure model
- [ ] Add channels in 2.4 GHz, 5 GHz, and 6 GHz
- [ ] Add interference basics
- [ ] Add throughput vs range

### 9. WWAN (LTE / 5G)

- [ ] Add cell concept and frequency reuse
- [ ] Add 1G to 5G evolution
- [ ] Add 4G IP-based core
- [ ] Add 5G core components: AMF, SMF, UPF
- [ ] Add network slicing

### 10. Quiz / Challenge Mode

- [ ] Add MCQs
- [ ] Add scenario-based questions
- [ ] Add "choose best tech" questions
- [ ] Add routing/debug challenges

## Folder Structure

```text
netsim/
├── src/
│   ├── core/          # app, routing, state
│   ├── ui/            # layout (split screen)
│   ├── modules/
│   │   ├── foundations/
│   │   ├── radio/
│   │   ├── mac/
│   │   ├── mesh/
│   │   ├── wsn/
│   │   ├── nfc/
│   │   ├── wlan/
│   │   ├── wwan/
│   │   └── quiz/
│   └── engine/        # simulations + animations
├── data/
│   ├── quizzes/
│   └── scenarios/
└── assets/
    └── ascii/
```

## Suggested Implementation Passes

- [ ] Pass 1: Create `src/`, `data/`, and `assets/` structure
- [ ] Pass 2: Build core app shell and state handling
- [ ] Pass 3: Build reusable UI panels and navigation
- [ ] Pass 4: Add Foundations module content
- [ ] Pass 5: Add Radio module content
- [ ] Pass 6: Add Propagation and MAC module content
- [ ] Pass 7: Add Mesh routing interactions
- [ ] Pass 8: Add WSN and NFC modules
- [ ] Pass 9: Add WLAN and WWAN modules
- [ ] Pass 10: Add quiz engine, questions, and challenge mode
- [ ] Pass 11: Add scenarios, polish, and ASCII assets
