import time
import numpy as np
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4
dt = 0.05
steps = 200
seed = 0

# Time the pure python loop version :
start = time.perf_counter()
simulate_loop(N0, lam, dt, steps, seed)
loop_time = time.perf_counter() - start

# Time the NumPy version :
start = time.perf_counter()
simulate(N0, lam, dt, steps, seed)
numpy_time = time.perf_counter() - start

print(f"Loop time:  {loop_time:.6f} s")
print(f"NumPy time: {numpy_time:.6f} s")
print(f"Speed-up:   {loop_time / numpy_time:.2f}x faster")
