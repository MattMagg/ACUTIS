"""Plugin abstractions for ACUTIS transducers.

These high-level interfaces lay the groundwork for a
pluggable hardware layer as outlined in ``acutis_research.md``.
"""

from __future__ import annotations

import random
from abc import ABC, abstractmethod


class TransducerPlugin(ABC):
    """Abstract base class for transducer plugins."""

    @abstractmethod
    def initialize(self, config: dict) -> bool:
        """Configure the plugin with the provided settings."""

    @abstractmethod
    def set_frequency(self, freq_hz: float) -> None:
        """Update the operating frequency."""

    @abstractmethod
    def transmit_pulse(self, params: dict | None = None) -> None:
        """Transmit an ultrasonic pulse."""

    @abstractmethod
    def receive_echo(self, timeout_ms: float | None = None) -> float:
        """Receive an echo and return its amplitude."""


class SimulatedTransducer(TransducerPlugin):
    """Basic in-memory implementation used for tests and demos."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.frequency = 0.0

    def initialize(self, config: dict) -> bool:
        self.frequency = config.get("frequency", 0.0)
        return True

    def set_frequency(self, freq_hz: float) -> None:
        self.frequency = freq_hz

    def transmit_pulse(self, params: dict | None = None) -> None:
        pass

    def receive_echo(self, timeout_ms: float | None = None) -> float:
        return random.uniform(0.0, 1.0)
