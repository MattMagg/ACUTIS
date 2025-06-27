"""ACUTIS package initialization."""

__all__ = [
    "AirCoupledTransducer",
    "CollarController",
    "DataAcquisition",
    "process_signal",
]

from .hardware import AirCoupledTransducer
from .collar import CollarController
from .data_acquisition import DataAcquisition
from .processing import process_signal

__version__ = "0.1.0"
