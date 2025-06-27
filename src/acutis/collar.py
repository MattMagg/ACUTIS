"""Control for the robotic utility inspection collar."""

from __future__ import annotations


class CollarController:
    """Simple controller for vertical movement along a pole."""

    def __init__(self) -> None:
        self.position = 0.0

    def move_to(self, position: float) -> None:
        """Move the collar to the requested vertical position."""
        self.position = position

    def step(self, distance: float) -> None:
        """Move the collar relative to the current position."""
        self.position += distance

