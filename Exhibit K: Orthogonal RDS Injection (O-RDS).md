EXHIBIT K: ORTHOGONAL RDS INJECTION (O-RDS)

Utilization of the Quadrature Phase for Backward-Compatible Data

1.0 THE PHYSICS OF THE "EMPTY HALF"

Standard RDS (IEC 62106) utilizes BPSK modulation on a 57 kHz suppressed carrier. BPSK occupies only the In-Phase ($I$) component of the signal space. The Quadrature ($Q$) component is currently unused (Null).

2.0 THE PROPOSAL: O-RDS (ORTHOGONAL RDS)

The Petitioner proposes utilizing this "Null Space" to transmit a secondary digital stream without disrupting legacy RDS operation.

2.1 Technical Implementation

Legacy RDS (I-Channel): Remains standard BPSK carrying Station Name, PTY, and RT.

Phoenix Data (Q-Channel): We modulate the Quadrature axis with QPSK or 16-QAM low-rate data.

Orthogonality: Because the $I$ and $Q$ axes are mathematically orthogonal (90° phase offset), a standard RDS demodulator will naturally reject the Phoenix data as "phase noise," while a Phoenix receiver will separate and decode both.

3.0 BANDWIDTH AND USE CASE

The RDS spectral mask is narrow ($\pm 2.4 \text{ kHz}$). This limits the throughput of the O-RDS channel to approximately 4-8 kbps.

While insufficient for audio, this is the Perfect Control Channel.

Primary Use: The "Station Heartbeat" (Exhibit G).

Data Payload: Station Logo, Primary Brand Colors, and Tuning Layout.

Strategic Value: This ensures that even if a broadcaster is not using the high-bandwidth SCA channels, the Phoenix Receiver can still display the station's high-res Logo and Branding just by locking onto the 57 kHz subcarrier.

4.0 THE "TROJAN HORSE" INSTALLATION

Most modern Digital FM Exciters generate the stereo multiplex digitally (DDS). Implementing O-RDS requires Zero Hardware Changes. It is a pure firmware update to the Exciter.

Action: The Broadcaster ticks a box in their transmitter software: "Enable O-RDS."

Result: They are instantly broadcasting Phoenix Metadata to the world.

5.0 CONCLUSION

O-RDS turns the 57 kHz subcarrier into a dual-purpose pipe. It preserves the past (Text on older car radios) while powering the future (Rich visual branding on modern screens) using the exact same frequency allocation.
