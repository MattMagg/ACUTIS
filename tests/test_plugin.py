import unittest

from src.acutis.plugin import SimulatedTransducer


class TestSimulatedTransducer(unittest.TestCase):
    def test_initialize_and_receive(self):
        plugin = SimulatedTransducer("demo")
        self.assertTrue(plugin.initialize({"frequency": 400e3}))
        plugin.set_frequency(450e3)
        amp = plugin.receive_echo()
        self.assertTrue(0.0 <= amp <= 1.0)


if __name__ == "__main__":
    unittest.main()
