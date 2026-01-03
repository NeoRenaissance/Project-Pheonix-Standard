EXHIBIT G (REV 2.0): APPLICATION EFFICIENCY AND SYNCHRONIZATION

The "Station Heartbeat" and Integrated Media Stream Architecture

1.0 THE BANDWIDTH REALITY

With a usable throughput of ~3.2 Mbps per channel via Recursive GFDM, the constraints of legacy bandwidth no longer apply.

Proposal: We allocate a dedicated 200 kbps "Side Channel" specifically for the rapid, repetitive transmission of Station Assets.

Impact: This consumes only ~6% of the total channel capacity, leaving 94% for high-fidelity content.

2.0 THE "STATION HEARTBEAT" PROTOCOL

To ensure immediate interface population for new listeners (travelers, battery resets), the station transmits a Station Identity Package (SIP) once every second.

2.1 The SIP Payload (Sent @ 1Hz)

The SIP is a highly compressed archive (e.g., .phx) containing:

Station Logo: Scalable Vector Graphic (SVG) for perfect resolution at any size.

Brand Colors: Primary/Secondary Hex codes for UI theming.

Station Name/Slogan: Text metadata.

Layout Manifest: A lightweight JSON defining the visual structure.

2.2 The User Experience

Tuning Event: User tunes to "104.7".

T+0ms: Audio begins decoding immediately (Priority 1). The UI shows a generic "Loading..." or the default OS radio interface.

T+1000ms (Max): The receiver captures the next "Heartbeat" SIP.

T+1050ms: The UI instantly "hydrates," applying the station's logo, colors, and layout. The transition is seamless.

3.0 THE INTEGRATED MEDIA STREAM (IMS)

To prevent synchronization errors between audio and visual elements (e.g., showing the wrong album art for the current song), the standard mandates an Atomic Stream Container.

3.1 The "Muxed" Packet Structure

Instead of sending Audio on Port A and Images on Port B, we interleave them into a single logical stream (The IMS).

Packet Sequence: [Audio Frame 1] [Audio Frame 2] [Image Fragment A] [Audio Frame 3]...

Synchronization: Every Audio Frame is time-stamped. Every Image is tagged with the start time and end time of the song it belongs to.

3.2 Embedded Album Art

Format: WebP or JPEG 2000 (High efficiency).

Frequency: The full image is transmitted at the start of the song and repeated periodically (e.g., every 10 seconds) for listeners tuning in mid-song.

Integration: The receiver buffers the image and reveals it exactly when the audio start-time marker hits the speaker.

4.0 CONCLUSION

This architecture trades a small amount of bandwidth (6%) for a massive improvement in User Experience. It eliminates the need for complex caching strategies or background scanning. A listener can drive into a new city, tune to a new station, and have the full, branded visual experience within one second.
