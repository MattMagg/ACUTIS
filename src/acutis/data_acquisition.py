"""Pseudocode for coordinating data acquisition."""

# This module illustrates how a collar and pair of transducers work together to
# gather signals at various heights. It intentionally avoids hardware specifics
# while outlining the expected flow of operations.

from .hardware import TransducerPair
from .collar import CollarController


class DataAcquisition:
    """Coordinates collar movement with pulse transmission."""

    def __init__(self, tx_id="TX1", rx_id="RX1"):
        # Create pseudocode hardware objects
        self.transducers = TransducerPair(tx_id, rx_id)
        self.collar = CollarController()

    def scan_step(self, position):
        """Capture a single reading at the specified height."""
        self.collar.move_to(position)
        amplitude = self.transducers.fire_and_listen()
        return amplitude

    def scan_profile(self, positions):
        """Collect readings for an entire vertical profile."""
        profile = []
        for pos in positions:
            reading = self.scan_step(pos)
            profile.append((pos, reading))
        return profile


