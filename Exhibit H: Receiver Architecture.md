EXHIBIT H: RECEIVER ARCHITECTURE

Wideband Capture and Multi-Zone Virtualization

1.0 PHILOSOPHY: THE "WIDEBAND CAPTURE" STANDARD

The Phoenix Standard mandates that automotive and fixed receivers utilize Direct RF Sampling or Wideband IF architectures capable of digitizing the entire broadcast band simultaneously.

The Paradigm Shift:

Legacy: The tuner looks at the world through a straw (200 kHz view).

Phoenix: The tuner looks at the world through a panoramic window (20 MHz view).

2.0 THE "ALWAYS-AWARE" BACKGROUND SENTINEL

Because the receiver digitizes the entire band, it runs a background process known as the Spectrum Sentinel.

2.1 Continuous Metadata Ingestion

Even while the user is listening to "104.7", the Sentinel is decoding the Station Heartbeat (SIP) of every other station in the market (88.1, 92.3, 101.1, etc.) in parallel.

User Benefit:

Instant Lists: The "Available Stations" list is always 100% up to date.

No "Seeking": The "Seek" button is obsolete. The radio already knows where every station is.

Smart Recommendations: The radio can alert the user: "You are listening to Jazz on 104.7, but a live Jazz concert just started on 89.3."

3.0 MULTI-ZONE VIRTUAL TUNERS

The digitization of the full band allows for Hardware Virtualization. A single physical receiver unit can spawn multiple Virtual Tuners.

3.1 The "Family Car" Scenario

Hardware: One Antenna, One Receiver Chip (SoC), One Central Processor.

Virtualization: The SoC extracts multiple sub-bands from the master Wideband Stream.

Virtual Tuner A (Driver): Extracts 104.7 MHz -> Decodes Opus -> Routes to Front Speakers.

Virtual Tuner B (Rear Left): Extracts 92.3 MHz -> Decodes Opus -> Routes to Bluetooth Headphones.

Virtual Tuner C (Rear Right): Extracts 87.9 MHz -> Decodes AV1 Video -> Routes to Rear Screen.

Economic Efficiency:
This capability requires zero additional RF hardware. It is purely a software calculation, drastically reducing the cost of premium "Rear Seat Entertainment" packages for automakers.

4.0 SEAMLESS HANDOVER (PREDICTIVE ROAMING)

The Background Sentinel enables flawless switching between transmitters.

Scenario: Driving between City A and City B.

Action: The Sentinel detects that the signal for "Station X" on 104.7 is fading, but the same Station ID is appearing strong on 101.1.

Result: The receiver phase-aligns the two streams and cross-fades them invisibly. The user never hears a pop, click, or dropout.

5.0 CONCLUSION

By mandating Wideband Capture, the Phoenix Standard transforms the receiver from a passive "listener" into an active "spectrum analyzer," capable of serving multiple users and maintaining total situational awareness of the broadcast environment.
