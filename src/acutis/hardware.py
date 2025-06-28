"""Hardware abstractions for the ACUTIS system."""

from __future__ import annotations

import random

from .plugin import TransducerPlugin


class AirCoupledTransducer(TransducerPlugin):
    """Simulated air-coupled ultrasonic transducer."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.frequency = 0.0

    def initialize(self, config: dict) -> bool:
        self.frequency = config.get("frequency", 0.0)
        return True

    def set_frequency(self, freq_hz: float) -> None:
        self.frequency = freq_hz

    def transmit_pulse(self, params: dict | None = None) -> None:
        """Simulate transmitting an ultrasonic pulse."""
        # In a real system, this would interface with hardware drivers.
        pass

    def receive_echo(self, timeout_ms: float | None = None) -> float:
        """Simulate receiving an echo with a random amplitude."""
        amplitude = random.uniform(0.0, 1.0)
        return amplitude

