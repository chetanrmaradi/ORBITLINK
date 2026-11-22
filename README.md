
# ORBITLINK 🚀

### Reliable Store-and-Forward Communication for Planetary Exploration

ORBITLINK is an engineering project that simulates a spacecraft communication system in which a planetary lander relies on an orbiter to relay data to mission control during intermittent communication windows.

The project explores reliable communication, packet prioritization, data buffering, acknowledgements, retransmissions, and embedded systems through software simulation and physical hardware.

---

## 🌌 Project Overview

In planetary exploration, a lander may not have a continuous communication link with Earth. Planetary obstruction, orbital motion, and limited communication availability can create periods of communication blackout.

ORBITLINK addresses this problem using a **Store-and-Forward Communication Architecture**.

The Lander collects and stores mission data locally. When an Orbiter enters communication range, the Lander transmits stored data according to priority. The Orbiter receives, validates, acknowledges, and relays the data toward Mission Control.

---

## 🎯 Objectives

- Simulate intermittent communication windows.
- Implement Store-and-Forward data transmission.
- Develop priority-based packet scheduling.
- Implement packet identification and acknowledgements.
- Simulate packet loss and communication delays.
- Implement retransmission and timeout mechanisms.
- Detect duplicate packets.
- Resume interrupted data transfers.
- Monitor communication performance through Mission Control.
- Transition from software simulation to physical embedded hardware.

---

## 🛰️ System Architecture

```text
                  ┌──────────────────────┐
                  │    MISSION CONTROL   │
                  │ Monitoring & Analysis│
                  └──────────▲───────────┘
                             │
                      Data Relay Link
                             │
                  ┌──────────┴───────────┐
                  │       ORBITER         │
                  │ Receive, Store, ACK   │
                  │ Relay Mission Data    │
                  └──────────▲─────────────┘
                             │
                    Intermittent Link
                    Contact Windows
                             │
                  ┌──────────┴───────────┐
                  │        LANDER         │
                  │ Sensors & Data Queue  │
                  │ Priority Scheduling  │
                  │ Store-and-Forward    │
                  └──────────────────────┘
```

### System Components

| Component | Responsibility |
|---|---|
| Lander | Generates, prioritizes, stores, and transmits mission data |
| Orbiter | Receives, validates, acknowledges, stores, and relays packets |
| Communication Link | Simulates contact windows, packet loss, and delays |
| Mission Control | Monitors communication status and received data |
| Protocol | Manages packet IDs, priorities, ACKs, retries, and integrity |

---

## 📡 Communication Features

### Store-and-Forward

Mission data is stored locally when communication is unavailable and transmitted when the next communication window opens.

### Priority-Based Scheduling

Packets are transmitted according to importance.

| Priority | Category | Description |
|---|---|---|
| P0 | Emergency | Critical alerts |
| P1 | High | Important operational telemetry |
| P2 | Medium | Science and routine measurements |
| P3 | Low | Bulk data and images |

Lower priority numbers represent higher importance.

### Reliable Delivery

ORBITLINK is designed to implement:

- Packet IDs
- Acknowledgements (ACK)
- Timeout detection
- Retransmission
- Duplicate detection
- Data integrity verification

### Communication Windows

Communication availability is controlled by simulated contact windows. Data remains queued during communication outages.

---

## 🧠 Protocol Design

The ORBITLINK communication protocol is designed around the following principles:

- Every packet has a unique identifier.
- Packet IDs remain unchanged during retransmission.
- Packets are acknowledged after successful reception.
- Unconfirmed packets remain pending.
- Duplicate packets are detected.
- Duplicate data must not be processed more than once.
- Emergency packets receive higher transmission priority.

---

## 🛠️ Technology Stack

### Software

- Python
- Git
- GitHub
- Visual Studio Code

### Embedded Systems

- ESP32
- Embedded C/C++
- Arduino framework

### Communication

- LoRa wireless communication
- Store-and-Forward networking
- Packet-based communication

### Planned Hardware

- ESP32 development boards
- LoRa transceiver modules
- MicroSD storage
- OLED displays
- Sensors
- Breadboards and jumper wires

---

## 📂 Repository Structure

```text
ORBITLINK/
│
├── docs/
│   ├── architecture/
│   │   └── system_architecture.md
│   │
│   ├── hardware/
│   │   └── bill_of_materials.md
│   │
│   ├── protocol/
│   │   └── protocol_specification_v1.md
│   │
│   └── testing/
│       └── test_plan.md
│
├── firmware/
│   ├── lander/
│   └── orbiter/
│
├── mission_control/
│
├── simulator/
│
├── tests/
│
├── logs/
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🧪 Planned Testing

ORBITLINK will be tested against scenarios including:

- Communication outage
- Packet loss
- ACK loss
- Packet retransmission
- Duplicate packet reception
- Priority scheduling
- Interrupted transfers
- Communication window reopening
- Queue recovery
- Data integrity validation

---

## 🗺️ Development Roadmap

- [x] Project initialization
- [x] Repository structure
- [x] Initial system architecture
- [x] Hardware planning
- [x] Initial testing plan
- [x] Communication fundamentals
- [x] Protocol specification planning

- [ ] Python communication simulator
- [ ] Lander data generation
- [ ] Orbiter receiver
- [ ] Contact window simulation
- [ ] Priority scheduler
- [ ] Packet loss simulation
- [ ] ACK and timeout handling
- [ ] Retransmission mechanism
- [ ] Duplicate packet detection
- [ ] Persistent data storage
- [ ] Mission Control dashboard
- [ ] ESP32 Lander implementation
- [ ] ESP32 Orbiter implementation
- [ ] LoRa integration
- [ ] Hardware testing
- [ ] End-to-end validation

---

## 📈 Project Status

**Current Stage:** Documentation and protocol design

**Next Milestone:** Build the first Python-based Lander–Orbiter communication simulator.

ORBITLINK is being developed incrementally, beginning with software simulation before progressing to embedded hardware and wireless communication.

---

## 👨‍💻 Developer

**Chetankumar R Maradi**

Electronics and Communication Engineering

---

## 📜 License

This project is licensed under the MIT License.

---

> Developed as an independent engineering project to explore embedded systems, communication protocols, reliable data transmission, and spacecraft-inspired networking architectures.
