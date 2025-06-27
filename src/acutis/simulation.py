"""Pseudocode for generating synthetic scan data.

During early development we may wish to model how echoes could look without any
hardware attached. Notes for a future simulation module:

* provide a `simulate_echo` helper that returns varying amplitudes
* optionally adjust the response when a `defect` flag is set
* introduce randomness so repeated runs do not yield identical values

The real implementation will evolve alongside the processing algorithms.
"""


