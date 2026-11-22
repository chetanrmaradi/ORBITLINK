\# ORBITLINK System Architecture



\## 1. Overview



ORBITLINK simulates a communication system in which a planetary lander

cannot communicate continuously with a remote mission control station.



An orbiter acts as an intermediate relay. Data is collected and stored

by the lander until a communication window becomes available.



During a communication window, queued data is transferred to the orbiter.



\## 2. Main Components



\### 2.1 Lander Node



Responsibilities:



\- Generate science and telemetry data.

\- Assign a unique ID to every message.

\- Assign priority levels.

\- Store messages in an outgoing queue.

\- Retain unacknowledged messages.

\- Transmit when communication is available.



\### 2.2 Orbiter Node



Responsibilities:



\- Receive packets from the lander.

\- Validate received data.

\- Identify duplicate packets.

\- Send acknowledgements.

\- Store successfully received data.

\- Forward data to mission control.



\### 2.3 Communication Link



The link represents the wireless connection between the lander

and orbiter.



The link can:



\- Become available during scheduled windows.

\- Become unavailable outside contact windows.

\- Lose packets.

\- Experience simulated delays.



\### 2.4 Mission Control



Mission Control provides monitoring and visualization.



It will display:



\- Communication state.

\- Received messages.

\- Packet priorities.

\- Transmission statistics.

\- Retries.

\- Packet losses.

\- Queue size.



\## 3. Store-and-Forward Operation



1\. The lander generates a data message.

2\. The message receives an ID and priority.

3\. The message is placed into the outgoing queue.

4\. If the communication link is unavailable, the message remains stored.

5\. When the link becomes available, the lander transmits queued messages.

6\. The orbiter validates the packet.

7\. The orbiter acknowledges successful reception.

8\. The lander removes acknowledged packets from its pending queue.

9\. Unacknowledged packets remain available for retransmission.



\## 4. Reliability Requirements



The system should:



\- Avoid losing queued messages during temporary link outages.

\- Detect missing acknowledgements.

\- Retry transmission.

\- Avoid processing duplicate packets more than once.

\- Prioritize urgent data.

\- Resume transmission after communication interruptions.



\## 5. Development Strategy



The project will initially be developed and tested using a software simulator.



Once the protocol and system behavior are validated, the software will be transferred to ESP32 hardware.



This allows communication logic to be tested before physical radio integration.

