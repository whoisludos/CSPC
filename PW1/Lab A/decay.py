import numpy as np


def simulate_loop(N0, lam, dt=0.05, steps=200, seed=0):
    """Radioactive decay, pure-Python loop version (slow)."""

    if lam < 0:
        raise ValueError("lam must be >= 0")

    rng = np.random.default_rng(seed)

    N = N0

    counts = [N0]

    for _ in range(steps):

        decayed = 0

        for _ in range(N):
            if rng.random() < lam * dt:
                decayed += 1

        N -= decayed

        counts.append(N)

    return np.array(counts)


def simulate(N0, lam, dt=0.05, steps=200, seed=0):
    """Radioactive decay, vectorised NumPy version (fast)."""

    if lam < 0:
        raise ValueError("lam must be >= 0")

    rng = np.random.default_rng(seed)

    N = N0

    counts = [N0]

    for _ in range(steps):

        decayed = rng.binomial(N, lam * dt)

        N -= decayed

        counts.append(N)

    return np.array(counts)
    