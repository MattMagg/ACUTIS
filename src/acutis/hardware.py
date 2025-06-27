"""Hardware abstractions for the ACUTIS system."""

from __future__ import annotations

import random


class AirCoupledTransducer:
    """Simulated air-coupled ultrasonic transducer."""

    def __init__(self, name: str) -> None:
        self.name = name

    def transmit_pulse(self) -> None:
        """Simulate transmitting an ultrasonic pulse."""
        # In a real system, this would interface with hardware drivers.
        pass

    def receive_echo(self) -> float:
        """Simulate receiving an echo with a random amplitude."""
        # This placeholder returns a pseudo-random amplitude.
        amplitude = random.uniform(0.0, 1.0)
        return amplitude

