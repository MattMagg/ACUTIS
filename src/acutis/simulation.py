"""Pseudocode for generating synthetic scan data."""

# This module allows development without real hardware by providing
# simple functions that mimic transducer responses.

import random


def simulate_echo(defect=False):
    """Return a fake amplitude value."""
    base = 1.0
    if defect:
        base *= 0.5  # strong attenuation example
    # Include random variation
    return base + random.uniform(-0.1, 0.1)

