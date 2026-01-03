EXHIBIT F: DATA TRANSPORT PROTOCOL

Adopting Standard IP Multicast for Unidirectional Broadcast

1.0 PHILOSOPHY: THE "AIR ETHERNET" CONCEPT

To ensure maximum compatibility with modern operating systems (Android, Linux, Automotive OS), the Phoenix Standard avoids proprietary transport layers.

Concept: The Recursive GFDM Physical Layer acts as a unidirectional "Ethernet cable."

Implementation: The receiver chip presents itself to the Host OS as a virtual Network Interface (e.g., tun0 or radio0).

2.0 THE PROTOCOL STACK

The system utilizes a standard IETF-compliant stack, modified only for unidirectional efficiency.

Layer

Protocol

Description

Application

RTP / FLUTE

Real-time audio/video (RTP) and File Delivery (FLUTE).

Transport

UDP

User Datagram Protocol. Connectionless, low overhead. No ACKs required.

Network

IPv6 Multicast

Future-proof addressing. Allows billions of unique multicast groups.

Link (MAC)

GSE (Generic Stream Encapsulation)

Efficiently packs variable-length IP packets into fixed-length GFDM frames.

Physical

Recursive GFDM

The underlying modulation.

3.0 MULTICAST ADDRESSING STRATEGY

Services are mapped to standard IPv6 Multicast Groups. This allows the receiver to "tune" to a service simply by joining a multicast group at the software level.

Example Addressing Scheme:

ff0x::101 - Main Audio Stream (Opus)

ff0x::102 - HD2 Music Stream

ff0x::200 - Video Stream (AV1)

ff0x::911 - NGEAS Emergency Alert Data (High Priority)

ff0x::500 - Firmware Update / File Carousel

4.0 UNIDIRECTIONAL RELIABILITY (NO FEEDBACK)

Since the receiver cannot send an Acknowledgment (ACK) packet back to the tower to request re-transmission of lost data, we implement Application Layer Forward Error Correction (AL-FEC).

4.1 RaptorQ (RFC 6330)

We mandate the use of RaptorQ codes for file transfers (FLUTE).

Mechanism: The broadcaster sends the data packets plus a stream of "repair symbols."

Benefit: If a car goes under a bridge and loses 10% of the packets, the receiver uses the repair symbols to mathematically reconstruct the missing data without needing to contact the transmitter.

5.0 SERVICE DISCOVERY (Electronic Service Guide)

How does the receiver know which IP address belongs to which station?

Service Announcement Protocol (SAP): A low-bitrate "Announcement Stream" is broadcast on a well-known IP (e.g., ff0x::1).

Content: It contains a JSON or XML file mapping Station Names ("Z100") to Multicast IPs ("ff0x::101") and establishing the schedule.

6.0 CONCLUSION

By using UDP/IP Multicast, we democratize development. An app developer does not need to understand RF physics or modulation. They simply write standard code to listen to a socket. This ensures the Phoenix Standard is ready for the "Internet of Things" immediately upon launch.
