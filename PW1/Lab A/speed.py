import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4

start_loop = time.perf_counter()
simulate_loop(N0, lam)
time_loop = time.perf_counter() - start_loop

start_numpy = time.perf_counter()
simulate(N0, lam)
time_numpy = time.perf_counter() - start_numpy

speedup = time_loop / time_numpy if time_numpy > 0 else 0

print(f"Loop time: {time_loop:.6f} s")
print(f"NumPy time: {time_numpy:.6f} s")
print(f"NumPy is {speedup:.2f}x faster")