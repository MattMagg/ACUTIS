import unittest

from src.acutis.hardware import AirCoupledTransducer
from src.acutis.plugin import TransducerPlugin


class TestAirCoupledTransducer(unittest.TestCase):
    def test_inherits_plugin(self):
        tx = AirCoupledTransducer("demo")
        self.assertIsInstance(tx, TransducerPlugin)
        self.assertTrue(tx.initialize({"frequency": 400e3}))
        tx.set_frequency(450e3)
        amp = tx.receive_echo()
        self.assertTrue(0.0 <= amp <= 1.0)


if __name__ == "__main__":
    unittest.main()

