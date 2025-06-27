# Internal Agent Plan

This plan guides the agent in gradually building the ACUTIS repository. It summarises the recommended stages of work derived from the proposal and patent.

## 1. Requirements & Research
- Thoroughly review the proposal and patent to capture functional goals and constraints.
- Identify key performance metrics for through-transmission scanning.

## 2. Architecture Design
- Outline hardware components: transducer pair, mechanical collar, acquisition electronics.
- Define software modules for sensor control, movement coordination, and data processing.

## 3. Prototype Development
- Produce an initial collar mechanism capable of vertical movement.
- Develop firmware to operate the collar and trigger ultrasonic pulses.

## 4. Signal Acquisition Module
- Capture through-transmission readings with precise timing.
- Synchronise transmitter and receiver for reliable measurements.

## 5. Processing & Analysis
- Detect anomalies such as rot or cracks in captured data.
- Store a continuous vertical profile for each pole inspected.

## 6. Control Software
- Drive collar motion and maintain transducer alignment.
- Provide safety checks and operator controls.

## 7. User Interface & Data Management
- Visualise scan data and log results for later review.
- Offer controls for starting, stopping, and reviewing scans.

## 8. Testing & Validation
- Unit test software modules and perform integration tests with hardware.
- Conduct field trials on sample poles to validate accuracy.

## 9. Iteration & Deployment
- Refine hardware and algorithms based on feedback.
- Package the system for operational use and document procedures.

This outline serves as a private roadmap for the agent. It will evolve as the project matures and new insights are gained from prototypes and tests.
