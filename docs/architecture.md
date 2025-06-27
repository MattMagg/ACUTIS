# ACUTIS Architecture Overview

This document outlines the initial architecture based on the high level plan. It provides high level pseudocode concepts for building an air-coupled ultrasonic inspection system.

## Components

- **Hardware Abstractions**: Classes representing transmitters, receivers, and mechanical movement.
- **Data Acquisition**: Coordinates hardware elements and collects readings for each collar position.
- **Processing**: Functions that analyze captured signals and extract useful metrics.
- **Command Line Interface**: Entry points for running simple simulated scans and demonstrating the workflow.
- **Simulation**: Provides fake signals so development can continue without hardware.
- **Scanner**: High level orchestrator that ties acquisition and processing together.

These components are currently described only in pseudocode. Future iterations
will expand them into full-featured modules that interact with real devices and
provide sophisticated analysis.
