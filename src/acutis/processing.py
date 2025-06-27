"""Signal processing utilities for ACUTIS."""

from __future__ import annotations

from statistics import mean


def process_signal(readings: list[float]) -> float:
    """Very basic signal processing placeholder.

    Calculates the mean amplitude of provided readings.
    """
    if not readings:
        raise ValueError("No readings provided")
    return mean(readings)

