APPENDIX Z: GLOSSARY OF TERMS AND DEFINITIONS

Standardized Terminology for the Phoenix Project (IEEE TBD)[Proposed: 802.BC]

1.0 ACRONYMS

GFDM (Generalized Frequency Division Multiplexing): A non-orthogonal multi-carrier modulation scheme that applies pulse shaping to individual subcarriers to minimize spectral bleed.

IMS (Integrated Media Stream): A synchronized data container holding both audio frames and visual assets (album art) in a single logical stream.

NEAF (National Emergency Alert Frequency): The designated AM frequencies (640 kHz and 1240 kHz) reserved for the "Lifeboat" service.

NGEAS (Next Generation Emergency Alert System): The overarching architecture combining terrestrial AM/FM alerts with mobile and data networks.

O-RDS (Orthogonal Radio Data System): A technique injecting secondary data onto the Quadrature (Q) axis of the legacy 57 kHz RDS subcarrier.

SIP (Station Identity Package): A compressed data burst sent at 1Hz containing station logos, colors, and layout logic ("The Heartbeat").

UMR (Universal Media Receiver): A regulatory device class capable of receiving and displaying both Radio and TV broadcast streams.

USII (United States Innovation Initiative): The proposed federal "Skunkworks" body responsible for rapid prototyping of critical infrastructure.

2.0 TECHNICAL CONCEPTS

First-Principle Thinking

First principles thinking is a problem-solving method that involves breaking down complex issues to their most fundamental truths, stripping away assumptions, and rebuilding knowledge from the ground up to find innovative solutions. Instead of reasoning by analogy (copying others), you question what's absolutely true and then reconstruct a new understanding or creation from those basic elements, much like building a song from notes rather than covers.

Recursive GFDM

The physical layer modulation standard for Project Phoenix. It utilizes a "Fractal" approach where the baseband is first channelized into "Sonic" (Audio) and "Supersonic" (Data) tiers, which are then independently modulated using GFDM filter banks before being upconverted to the carrier frequency. This achieves spectral efficiencies of >10 bps/Hz.

Phoenix Native Mode

A high-efficiency transport mode that strips standard IPv6/UDP headers (48 bytes) and replaces them with a 1-byte binary "Flow ID," utilizing Static Context Header Compression (SCHC) to increase throughput by up to 40% for small-packet services.

Virtual Channel Mapping (VCM)

A regulatory and software mechanism allowing a station to retain its legacy branding (e.g., "104.7") on the receiver display even if the physical transmission has moved to a different frequency (e.g., a digital multiplex).

Station Vector Profile (SVP)

A semantic metadata block containing weighted keywords (Mood, Genre, Artist Affinity) designed to be ingested by on-device AI for "Intent-Based Tuning" (e.g., "Play Queen").

3.0 HARDWARE CLASSIFICATIONS

The Lifeboat Radio

A Tier-1 Ultra-Low-Cost receiver (ASIC-based) designed solely for resilience. It features a Tamagotchi-style form factor, weeks of battery life, and is hard-coded to tune only to the NEAF (640/1240 kHz) BPSK signals.

The Wideband Sentinel

A background software process in Phoenix-compliant receivers that continuously digitizes the entire FM band (88-108 MHz) to cache metadata, enable instant switching, and support "Smart Hop" discovery notifications.

4.0 SPECTRUM ZONES (AM BAND RE-ALLOCATION)

Public Safety Zone

(640 kHz & 1240 kHz). Exclusive to the NGEAS "Lifeboat" signal.

Digital Resilience Zone

(650 kHz – 1230 kHz). A digital-only, encrypted government data layer utilizing Carrier Aggregation for secure, terrestrial point-to-point and broadcast communications.

Community Zone

(1400 kHz – 1710 kHz). Reserved for low-power, non-commercial, and hyper-local community broadcasting.
