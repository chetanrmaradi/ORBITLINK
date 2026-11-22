# \# ORBITLINK

# 

# \### Reliable Store-and-Forward Communication for Planetary Exploration

# 

# ORBITLINK is an embedded communication system inspired by spacecraft communication architectures, where a lander cannot maintain continuous communication with Earth and relies on an orbiter acting as a relay.

# 

# The project implements a store-and-forward architecture that buffers data during communication outages and transfers it during scheduled communication windows.

# 

# \## Objectives

# 

# \- Simulate intermittent communication windows.

# \- Store outgoing data when the link is unavailable.

# \- Support priority-based message scheduling.

# \- Implement packet identification and acknowledgements.

# \- Recover lost packets through retransmission.

# \- Prevent duplicate packet processing.

# \- Monitor communication performance through Mission Control.

# \- Transition from software simulation to physical embedded hardware.

# 

# \## System Architecture

# 

# The project consists of:

# 

# \- \*\*Lander Node\*\* – Generates and queues mission data.

# \- \*\*Orbiter Node\*\* – Receives and relays data.

# \- \*\*Communication Protocol\*\* – Handles packet IDs, validation, acknowledgements and retries.

# \- \*\*Mission Control\*\* – Displays link state, packets and performance statistics.

# 

# \## Development Roadmap

# 

# 1\. Development environment setup

# 2\. Communication fundamentals

# 3\. Communication simulator

# 4\. Packet protocol

# 5\. Lander firmware

# 6\. Orbiter firmware

# 7\. Contact-window management

# 8\. Reliable transmission

# 9\. Persistent storage

# 10\. Mission Control dashboard

# 11\. Hardware integration

# 12\. Testing and validation

# 

# \## Technologies

# 

# \- Python

# \- Embedded C/C++

# \- ESP32

# \- Wireless communication

# \- Git

# \- Arduino framework

# 

# \## Project Status

# 

# Currently in development.

# 

# \## Author

# 

# Chetankumar R Maradi

# 

# \---

# 

# This project is developed as an independent engineering and learning project.

