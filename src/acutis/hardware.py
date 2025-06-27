"""High level pseudocode for hardware abstractions."""

# Pseudocode classes describing the low level hardware used by ACUTIS. The
# actual drivers will be implemented in future stages when real devices are
# available.


class AirCoupledTransducer:
    """Represents either a transmitter or a receiver unit."""

    def __init__(self, identifier):
        # Store identifier or hardware port for later use
        self.identifier = identifier

    def transmit_pulse(self):
        # Trigger an ultrasonic burst on the hardware
        pass

    def receive_echo(self):
        # Return a measured amplitude from the receiver
        amplitude = None
        return amplitude


class TransducerPair:
    """Convenience class bundling a transmitter and receiver."""

    def __init__(self, tx_id, rx_id):
        self.transmitter = AirCoupledTransducer(tx_id)
        self.receiver = AirCoupledTransducer(rx_id)

    def fire_and_listen(self):
        # Pseudocode to transmit and capture a reading
        self.transmitter.transmit_pulse()
        echo = self.receiver.receive_echo()
        return echo


