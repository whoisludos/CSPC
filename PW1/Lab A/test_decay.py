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
    dt = 0.05
    steps = 200

    results = []

    for seed in range(100):
        results.append(simulate(N0, lam, dt, steps, seed)[-1])

    average = np.mean(results)

    t = steps * dt
    expected = N0 * np.exp(-lam * t)

    assert average == pytest.approx(expected, rel=0.05)
    