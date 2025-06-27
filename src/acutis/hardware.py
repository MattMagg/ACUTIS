"""High level pseudocode for hardware abstractions.

This module no longer defines real classes. Instead it sketches the ideas
behind the hardware layer:

* **AirCoupledTransducer** – conceptual transmitter or receiver. It would store
  an identifier and offer operations such as `transmit_pulse` and
  `receive_echo`.
* **TransducerPair** – groups a transmitter and a receiver so one can issue a
  pulse and listen for the response in a single step.

Drivers and detailed implementations will be added once real devices are
available. For now these notes simply outline the intent of the hardware
abstractions.
"""



