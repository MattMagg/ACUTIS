import unittest

from src.acutis.collar import CollarController
from src.acutis.data_acquisition import DataAcquisition
from src.acutis.hardware import AirCoupledTransducer


class TestDataAcquisition(unittest.TestCase):
    def test_scan_profile_length(self):
        tx = AirCoupledTransducer("TX")
        rx = AirCoupledTransducer("RX")
        collar = CollarController()
        daq = DataAcquisition(tx, rx, collar)
        positions = [0, 1, 2, 3]
        readings = daq.scan_profile(positions)
        self.assertEqual(len(readings), len(positions))


if __name__ == "__main__":
    unittest.main()
