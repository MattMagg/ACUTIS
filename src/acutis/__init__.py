"""Package placeholder with pseudocode references."""

# The package exposes basic classes so that other modules or example scripts can
# import them. All implementations remain high level stubs.

from .hardware import AirCoupledTransducer, TransducerPair
from .collar import CollarController
from .data_acquisition import DataAcquisition
from .processing import process_signal
from .simulation import simulate_echo
from .scanner import Scanner

__all__ = [
    "AirCoupledTransducer",
    "TransducerPair",
    "CollarController",
    "DataAcquisition",
    "process_signal",
    "simulate_echo",
    "Scanner",
]

