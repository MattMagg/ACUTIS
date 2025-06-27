"""Data acquisition routines for ACUTIS."""

from __future__ import annotations

from .hardware import AirCoupledTransducer
from .collar import CollarController


class DataAcquisition:
    """Coordinate collar movement and signal capture."""

    def __init__(self, transmitter: AirCoupledTransducer, receiver: AirCoupledTransducer, collar: CollarController) -> None:
        self.transmitter = transmitter
        self.receiver = receiver
        self.collar = collar

    def scan_step(self, position: float) -> float:
        """Move to position, transmit, and receive a single reading."""
        self.collar.move_to(position)
        self.transmitter.transmit_pulse()
        amplitude = self.receiver.receive_echo()
        return amplitude

    def scan_profile(self, positions: list[float]) -> list[float]:
        """Scan a series of positions and return their amplitudes."""
        readings = []
        for pos in positions:
            reading = self.scan_step(pos)
            readings.append(reading)
        return readings

