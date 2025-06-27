# Data Acquisition

The data acquisition process will coordinate collar movement with the ultrasonic transducers. A typical scan will involve stopping at predefined heights, sending a pulse, and recording the resulting echo. Important goals include:

- Simple routines for moving the collar to each height in a scan profile.
- Collection of raw amplitudes and timing information from the sensors.
- Storage of readings for later processing and analysis.
- Providing clean input for the scanner workflow described in `scanner.md`.

Implementation details will depend on the final hardware, so this note serves as a placeholder until prototypes are built.

## Pseudocode Example

```
for each height in scan_profile:
    collar.move_to(height)
    transmitter.emit_pulse()
    echo = receiver.capture()
    store(height, echo)
```

This snippet expresses the intended flow without tying it to any specific
programming language. The focus is on moving the collar, emitting a pulse,
capturing the echo, and storing the reading for later analysis.
