# ACUTIS Architecture Overview

This document outlines the initial architecture based on the high level plan. It provides high level pseudocode concepts for building an air-coupled ultrasonic inspection system.

## Components

- **Hardware Abstractions**: Classes representing transmitters, receivers, and mechanical movement.
- **Data Acquisition**: Coordinates hardware elements and collects readings for each collar position.
- **Processing**: Functions that analyze captured signals and extract useful metrics.
- **Command Line Interface**: Entry points for running simple simulated scans and demonstrating the workflow.

Future iterations will expand these components into full-featured modules that interact with real devices and provide sophisticated analysis.
