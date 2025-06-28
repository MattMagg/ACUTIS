"""ACUTIS package initialization."""

__all__ = [
    "AirCoupledTransducer",
    "CollarController",
    "DataAcquisition",
    "process_signal",
    "TransducerPlugin",
    "SimulatedTransducer",
]

from .hardware import AirCoupledTransducer
from .collar import CollarController
from .data_acquisition import DataAcquisition
from .processing import process_signal
from .plugin import TransducerPlugin, SimulatedTransducer

__version__ = "0.1.0"
