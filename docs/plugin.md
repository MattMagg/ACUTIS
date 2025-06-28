# Transducer Plugin Architecture

ACUTIS uses a modular plugin model for air-coupled transducers. Plugins share a
common interface so that different hardware can be swapped without changing the
rest of the system. The interface is defined in `src/acutis/plugin.py` and is
inspired by the recommendations in `acutis_research.md`.

Each plugin must implement methods to initialize itself, set the operating
frequency, transmit ultrasonic pulses, and receive echoes. The repository
includes a `SimulatedTransducer` used for tests and early development.

