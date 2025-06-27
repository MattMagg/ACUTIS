# ACUTIS Architecture Overview

This document outlines the evolving architecture based on the high level plan. It summarises how an air-coupled ultrasonic inspection system might be organised.

## Components

- **Transducer Pair**: the main transmitter and receiver used for through-transmission measurements. See `notes/transducer.md` for design considerations.
- **Hardware Abstractions**: notes on drivers and mechanical movement of the collar.
- **Data Acquisition**: ideas for coordinating hardware and logging readings for each collar position.
- **Processing**: outlines of how captured signals might be analysed.
- **Command Line Interface**: a proposed way to run simple simulated scans and demonstrate the workflow.
- **Simulation**: Provides fake signals so development can continue without hardware.
- **Scanner**: High level orchestrator that ties acquisition and processing together.

These components remain conceptual and will be refined as prototypes are built and tested. Detailed descriptions of each area are kept in the `notes/` directory.
