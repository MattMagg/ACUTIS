# NOTE: These tests are placeholders and are intentionally skipped until real
# implementations exist.
import unittest

from src.acutis.processing import process_signal


class TestProcessing(unittest.TestCase):
    def test_process_signal_average(self):
        readings = [0.1, 0.2, 0.3]
        self.assertAlmostEqual(process_signal(readings), 0.2)

    def test_process_signal_empty(self):
        with self.assertRaises(ValueError):
            process_signal([])


if __name__ == "__main__":
    unittest.main()
