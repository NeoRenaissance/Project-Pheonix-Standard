EXHIBIT I: THE HYBRID TRANSITION PROTOCOL

Facilitating Backward Compatibility via Baseband Multiplexing

1.0 THE BRIDGE STRATEGY

Recognizing that a "Flash Cut" to all-digital operations is not economically feasible for all markets immediately, the Phoenix Standard defines a Hybrid Transition Mode.

Concept: The 200 kHz channel is managed dynamically. We utilize the FM Baseband (the signal modulating the carrier) to stack Analog and Digital services vertically in the frequency domain.

2.0 OPERATIONAL MODES

Broadcasters may select their operating mode based on their content strategy and market readiness.

Mode 1: Hybrid Stereo (The "Audiophile" Bridge)

Designed for Music Stations that must maintain legacy Analog Stereo compatibility.

0 - 53 kHz: Legacy Analog (Mono L+R, Pilot, Stereo L-R).

57 - 99 kHz: Digital Resilience Tier (Recursive GFDM).

Result: Legacy radios hear perfect Stereo. New radios decode ~600 kbps of digital data (enough for Album Art, Metadata, and a Lossless Digital Stream).

Mode 2: Hybrid Mono (The "Talk Radio" Powerhouse)

Designed for News/Talk stations where Stereo separation is unnecessary, or Music stations willing to trade Analog Stereo for Digital Power.

0 - 15 kHz: Legacy Analog (Mono L+R).

16 - 19 kHz: Guard Band.

20 - 99 kHz: High-Capacity Digital Tier.

Result: Legacy radios hear clear Mono audio. By reclaiming the spectrum previously wasted on the fragile Analog Stereo subcarrier, the digital throughput doubles to ~1.2 Mbps.

Mode 3: All-Digital (The Phoenix Native)

The eventual end-state. The Analog Carrier is extinguished.

Full 200 kHz Mask: Dedicated to Recursive GFDM.

Throughput: ~3.2 Mbps.

3.0 SPECTRAL NON-INTERFERENCE

Unlike legacy "HD Radio" (IBOC), which injects digital noise into the adjacent sidebands (causing interference to neighboring stations), the Phoenix Hybrid signal is fully contained within the host carrier's deviation mask.

Filtering: The Recursive GFDM subcarriers are strictly filtered to ensure they do not bleed down into the Analog Audio baseband (preventing "hiss" on old radios).

4.0 THE "SOFT LANDING" SUNSET

This protocol allows for a consumer-driven sunset of analog.

Phase 1: Broadcasters run Mode 1 (Hybrid Stereo).

Phase 2: As digital receiver penetration hits 50%, broadcasters switch to Mode 2 (Hybrid Mono) to increase digital bandwidth for HD Video/Data services.

Phase 3: When analog listenership drops below 5%, the station switches to Mode 3 (All-Digital).

5.0 CONCLUSION

This addendum ensures that no listener is left behind. A 1975 Ford Pinto and a 2026 Tesla can both tune to the same frequency; the Pinto hears the Analog baseband, while the Tesla decodes the massive Digital payload sitting silently above it.
