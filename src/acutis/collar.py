"""Notes on collar movement control.

The real collar will eventually climb or descend a utility pole. At this stage
we only describe the concept at a high level:

* **CollarController** – imagined manager of the climbing mechanism. It tracks
  the current height and exposes commands such as `move_to` for absolute
  positioning and `step` for incremental movements.

Motor control and other low level details are intentionally omitted until the
mechanical design is finalized.
"""



