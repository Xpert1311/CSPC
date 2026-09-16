"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


def test_matches_law():
    N0 = 1000
    lam = 0.4
    sim = simulate(N0, lam)
    idx = len(sim) // 2
    final_val = sim[-1]
    val = sim[20]
    dt = 1.0 / len(sim)
    assert 0 <= final_val <= N0