# ACUTIS Architecture Overview

This document outlines the initial architecture based on the high level plan. It summarises how an air-coupled ultrasonic inspection system might be organised.

## Components

- **Hardware Abstractions**: notes on transmitters, receivers, and mechanical movement.
- **Data Acquisition**: ideas for coordinating hardware and logging readings for each collar position.
- **Processing**: outlines of how captured signals might be analysed.
- **Command Line Interface**: a proposed way to run simple simulated scans and demonstrate the workflow.
- **Simulation**: Provides fake signals so development can continue without hardware.
- **Scanner**: High level orchestrator that ties acquisition and processing together.

These components are currently described only at a conceptual level. Future
iterations will expand them into full-featured modules that interact with real
devices and provide sophisticated analysis.

Detailed descriptions of each component can be found in the `notes/` directory.
