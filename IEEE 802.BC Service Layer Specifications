IEEE 802.BC SERVICE LAYER SPECIFICATIONS

Unified Codec Profiles and Universal Broadcast Architecture

1.0 THE "DRAG-AND-DROP" BROADCASTER EXPERIENCE

To drive adoption, the complexity of the physical layer (Recursive GFDM) must be abstracted away. We propose a Virtual Slot Architecture. The broadcaster sees a "Capacity Bucket" (e.g., 3.2 Mbps for a standard FM channel) and simply drags services into it.

1.1 Standardized Audio Codec: Opus

The standard mandates Opus as the universal audio codec due to its royalty-free status, ultra-low latency, and incredible scaling from speech to transparent music.

The "Phoenix" Audio Tiers:

Tier Name

Target Use Case

Bitrate (Opus)

Audio Quality Description

Capacity Usage*

Phoenix Master

Main Station Feed

128 kbps

Transparent Stereo. Indistinguishable from CD/Lossless to the human ear.

~4.0%

Phoenix Music

HD2/HD3 Sub-channels

64 kbps

High-Fidelity Stereo. Superb quality, superior to 128kbps MP3.

~2.0%

Phoenix Voice

Talk Radio / Sports / News

12 kbps

Wideband Speech. Crystal clear voice, vastly superior to legacy AM's 3kHz bandwidth.

~0.4%

Phoenix Lossless

Audiophile Subscription

Variable

FLAC/ALAC bit-perfect streaming.

Variable

*Capacity Usage based on a conservative 3.2 Mbps channel throughput.

The "Leftover" Opportunity:
Even with a Main Feed (128k), two Music Sub-channels (64k + 64k), and a Talk channel (12k), a broadcaster has used only 268 kbps.

Remaining Capacity: ~2.9 Mbps.

Opportunity: This massive surplus allows the broadcaster to lease bandwidth for data services, firmware updates, or even video streams without degrading audio quality.

2.0 EXPANSION TO TELEVISION (THE ATSC 3.0 REPLACEMENT)

ATSC 3.0 (NextGen TV) utilizes OFDM, which is an improvement over older standards, but it still suffers from guard-band inefficiencies and legacy overhead. Recursive GFDM is frequency-agnostic and spectrally superior.

We propose IEEE 802.BC-TV, applying the Phoenix standard to the UHF/VHF Television bands.

2.1 The Unified Silicon Argument

Currently, device manufacturers need separate tuners for Radio and TV.

The Phoenix Solution: A single Software-Defined Radio (SDR) ASIC handles all terrestrial broadcast.

Universal Decoding: The device tunes to a frequency (e.g., 500 MHz), identifies the Recursive GFDM header, and decodes the stream. The device doesn't "know" it's a TV station until it sees the video packets.

2.2 Video Profiles (H.265 / AV1)

Leveraging the 3.2 Mbps throughput of a single 200 kHz slice (and scaling up for 6 MHz TV channels), 802.BC outperforms ATSC 3.0:

Single 6 MHz TV Channel Capacity (Recursive GFDM):

Standard ATSC 3.0: ~25-57 Mbps (depending on robustness).

IEEE 802.BC: ~96 Mbps (theoretical max at 16 bps/Hz across 6 MHz).

Implication: A single TV station could broadcast uncompressed or lightly compressed 8K video, or dozens of 4K streams, utilizing the same spectrum that currently struggles to carry a few HD channels.

3.0 THE UNIVERSAL RECEIVER CONCEPT

By standardizing the modulation (Recursive GFDM) and the codecs (Opus for audio, AV1 for video) across ALL bands (AM, FM, TV), we create a unified consumer device class.

The "Phoenix" Device Capability:

Scanner Mode: The device scans from 500 kHz to 900 MHz.

Stream Identification: It identifies "Lifeboat" BPSK signals, standard Audio streams, and Video streams.

Unified Interface:

User clicks "101.1 FM" -> Device plays 128k Opus Audio.

User clicks "Ch 5 TV" -> Device plays 4K AV1 Video.

User clicks "Emergency" -> Device tunes 640 kHz BPSK.

User clicks "File Download" -> Device caches a firmware update.

4.0 CONCLUSION

The distinction between "Radio" and "Television" is an analog artifact. In the digital domain, there is only bandwidth and throughput. IEEE 802.BC unifies all terrestrial broadcasting under a single, hyper-efficient standard, drastically reducing hardware costs and complexity while exponentially increasing broadcaster revenue potential.
