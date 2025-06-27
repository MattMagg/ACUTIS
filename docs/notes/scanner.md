# Scanner Workflow

A complete inspection will combine data acquisition with signal processing. The scanner concept ties these steps together. At a high level it should:

1. Move the collar to each height specified by an operator.
2. Capture signals at each stop.
3. Process the collected data and store the results for review.

These ideas are intentionally broad. They serve as an outline for future development once the hardware and processing algorithms mature.

## Pseudocode Outline

```
for height in scan_heights:
    collar.move_to(height)
    signal = acquisition.capture()
    result = processing.analyse(signal)
    log.store(height, result)
```

This sketch illustrates the flow rather than executable code. Each step depends on future modules that manage the collar, acquisition hardware, and analysis routines.
