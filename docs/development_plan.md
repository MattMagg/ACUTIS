# ACUTIS Development Plan

This document outlines high-level stages for building ACUTIS. The timeline spans multiple months and focuses on incremental progress rather than rushing to a finished system.

## Stage 1: Requirements & Research
- Study the proposal and patent to confirm that ACUTIS relies on a Robotic Utility Pole Inspection Collar (RUPIC) performing through-transmission scans.
- Gather performance goals and constraints from these sources.
- Identify safety considerations for operating the collar on live utility poles.

## Stage 2: Simulation Foundation
- Maintain a lightweight environment to model components.
- Use simple scripts to explore collar motion and signal capture workflows.
- Introduce simulation and scanner concepts to exercise the planned workflow.

## Stage 3: Hardware Prototypes
- Build an initial RUPIC collar mechanism and design the air-coupled transducer pair for through-transmission operation.
- Evaluate basic data acquisition strategies and verify signal quality.

## Stage 4: Data Acquisition Pipeline
- Develop software to coordinate collar movement with pulse transmission and reception.
- Log raw readings for later processing.

## Stage 5: Signal Processing & Analysis
- Implement algorithms to detect anomalies in the captured data.
- Refine techniques through iterative testing on sample poles.
- Expand the scanner workflow to handle full pole scans automatically.

## Stage 6: Integrated System Trials
- Combine hardware and software for full scans.
- Conduct field tests and adjust the approach based on results.

This plan is intentionally broad. Details will evolve as prototypes are tested and feedback is gathered.
