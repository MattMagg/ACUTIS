# ACUTIS Development Roadmap

This document sketches the major milestones for expanding the project. It
summarizes priorities extracted from `acutis_research.md` and serves as a
high-level guide for future contributors.

## Phase 1 – Core Framework
- Establish the hardware abstraction layer with a pluggable transducer interface.
- Implement the basic signal processing pipeline for A‑scan measurements.
- Create a reproducible build and test environment using Python and CMake.

## Phase 2 – Real Hardware Integration
- Provide plugin implementations for common air‑coupled transducers and DAQ
  devices.
- Add deterministic scheduling and buffering required for sub‑100 µs latency.
- Begin capturing real data and verifying algorithms against reference samples.

## Phase 3 – Advanced Inspection Features
- Introduce B‑scan and C‑scan imaging modules with GPU acceleration options.
- Expand automatic defect detection and calibration utilities.
- Document performance characteristics and best practices for deploying
  inspection stations.

These phases are intentionally broad to allow flexibility. As the repository
matures, each milestone can be broken down into detailed tasks and linked issues.
