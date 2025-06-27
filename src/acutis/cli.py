"""Command line interface for running sample scans."""

from __future__ import annotations

import argparse
from typing import List

from .hardware import AirCoupledTransducer
from .collar import CollarController
from .data_acquisition import DataAcquisition
from .processing import process_signal


def run_scan(positions: List[float]) -> None:
    """Run a simulated scan across the provided positions."""
    tx = AirCoupledTransducer("TX")
    rx = AirCoupledTransducer("RX")
    collar = CollarController()
    daq = DataAcquisition(tx, rx, collar)

    readings = daq.scan_profile(positions)
    result = process_signal(readings)
    for pos, reading in zip(positions, readings):
        print(f"position {pos:.2f} -> amplitude {reading:.3f}")
    print(f"average amplitude: {result:.3f}")


def main(args: List[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run a simulated ACUTIS scan")
    parser.add_argument(
        "positions",
        metavar="P",
        type=float,
        nargs="+",
        help="positions along the pole to scan",
    )
    ns = parser.parse_args(args)
    run_scan(ns.positions)


if __name__ == "__main__":
    main()

