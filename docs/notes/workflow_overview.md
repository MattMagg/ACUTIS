# Overall Workflow

This note summarises how the main parts of ACUTIS might interact during a scan. Each stage is intentionally high level to avoid locking into specific implementations.

1. **Initial Setup**
   - The collar attaches around the pole and pairs of air-coupled transducers are aligned on opposite sides.
   - Operators define the range of heights to inspect and any spacing between scan points.

2. **Movement & Acquisition**
   - The collar climbs to each specified height in sequence.
   - At each stop, the transmitter emits a short pulse and the receiver captures the transmitted waveform.
   - Raw readings are timestamped and stored for later processing.

3. **Processing & Analysis**
   - Collected signals are examined to identify unusual attenuation or delayed arrivals that may indicate internal damage.
   - Results are logged with references to their respective heights.

4. **Review**
   - Operators review the processed data, comparing it with previous scans or baseline measurements.
   - Any detected anomalies can be flagged for further inspection or maintenance.

This workflow captures the broad sequence of actions without delving into code details. Each step will be refined as hardware prototypes and algorithms mature.
