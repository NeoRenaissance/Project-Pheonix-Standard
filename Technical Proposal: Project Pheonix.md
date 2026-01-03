TECHNICAL PROPOSAL: PROJECT PHOENIX

Reimagining the 530–1710 kHz and 87.9 MHz Bands for National Resilience

I. EXECUTIVE SUMMARY

This proposal outlines a comprehensive modernization of the Medium Frequency (MF) and Very High Frequency (VHF) bands. It addresses the decline of legacy AM broadcasting by facilitating a voluntary migration of broadcasters to a new Digital FM standard, while simultaneously repurposing the vacated AM spectrum into a tiered National Resilience Network. Central to this proposal is the Next Generation Emergency Alert System (NGEAS), a self-healing, multi-band digital architecture designed for high-fidelity communication during atmospheric and geomagnetic disturbances.

II. SPECTRUM ALLOCATION & BAND PLAN

The proposal restructures the current AM broadcast band (530–1710 kHz) into three distinct functional zones:

Public Safety Zone (NEAF): Dedicated National Emergency Alert Frequencies at 640 kHz and 1240 kHz. These utilize ultra-robust BPSK modulation for "Lifeboat" audio.

Digital Resilience Zone (650–1230 kHz): A high-power, government-managed digital backbone for secure, point-to-point and broadcast data using high-order Recursive GFDM.

Community/Local Zone (1250–1710 kHz): Reserved for low-power, hyper-local community broadcasting.

The Multimedia Alert Channel (87.9 MHz): A dedicated VHF channel for high-capacity video and data feeds (e.g., Presidential addresses, evacuation maps) accessible by specialized digital receivers.

III. TECHNICAL SPECIFICATIONS: RECURSIVE GFDM

To maximize spectral efficiency, the project introduces Recursive Generalized Frequency Division Multiplexing (GFDM).

Fractal Modulation Architecture: The baseband is channelized into "sonic" and "supersonic" sub-bands. Each sub-band is independently modulated with GFDM before final carrier modulation.

Spectral Efficiency: By applying filters to individual subcarriers and sub-bands, guard bands are virtually eliminated. This allows for:

FM Band: 4096-QAM ($12 \text{ bps/Hz}$)

AM Band: 1024-QAM ($10 \text{ bps/Hz}$)

Throughput: Achieving a theoretical efficiency of up to $16 \text{ bps/Hz}$, allowing a standard 200 kHz FM channel to carry approximately $3.2 \text{ Mbps}$ of raw data.

IV. THE NGEAS INFRASTRUCTURE

The Next Generation Emergency Alert System (NGEAS) evolves beyond the legacy EAS/WEA models:

Self-Healing SFN with Active Beamforming: Transmitter sites utilize active beamforming to maintain a uniform omnidirectional pattern. In the event of a transmitter failure, neighboring nodes adjust phasing and power to dynamically recover the coverage gap.

Solar Storm Resilience: A pre-determined "Solar Storm MCS" (Modulation and Coding Scheme) allows broadcasters to instantly switch to 4-QAM (QPSK) with aggressive 1/3 SCCC coding to ensure signal penetration during geomagnetic scintillation.

HHS Integration: Deployment and management are spearheaded by the Department of Health and Human Services (HHS), treating emergency communication as a critical public health utility.

V. RECEIVER ECOSYSTEM

To ensure universal access, the project utilizes a tiered hardware approach:

Phoenix Lifeboat Radio: A keychain-sized (Tamagotchi form factor) ASIC-based receiver.

Hardware: Single-chip SoC, ferrite rod antenna, passive RFID tag for search-and-rescue tracking.

Function: Dedicated to BPSK alerts on 640/1240 kHz.

Radio-First Android Terminals: Repurposed, low-cost smartphone hardware adjusted for dedicated RF reception.

Function: High-fidelity audio, video data from 87.9 MHz, and rich-media government briefings.

VI. THE LICENSE EXCHANGE PROGRAM (THE "CARROT")

Broadcasters are incentivized to migrate via a voluntary license exchange:

The Swap: Surrender MF (AM) licenses in exchange for a digital-only FM subchannel or a new 200 kHz digital FM allocation.

The Mandate: Migrated broadcasters must install an NGEAS transceiver to monitor NEAF frequencies and automatically rebroadcast "Level 1" alerts to their local communities.

VII. CONCLUSION

The Phoenix Project provides the FCC with a turnkey solution to spectrum congestion and emergency resilience. It preserves the heritage of terrestrial broadcast while catapulting its technical capabilities into the 21st century.
