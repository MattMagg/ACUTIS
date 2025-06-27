"""High level concept for coordinating data acquisition.

The data acquisition layer will eventually combine the collar controls with the
transducers. At present we only map out the anticipated responsibilities:

* create a **TransducerPair** to issue pulses and capture echoes
* create a **CollarController** to position the hardware along the pole
* define a routine that moves to each position, fires the transducers, and logs
  the reading

Actual implementation will come later when hardware prototypes exist. These
notes simply record the idea of a `scan_profile` that returns a series of
measurements for specified heights.
"""



