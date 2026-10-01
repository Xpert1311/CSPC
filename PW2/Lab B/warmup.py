import numpy as np
from scipy.optimize import newton, minimize

def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

print("--- Part 2A ---")

x_gd = 0.0
lr = 0.1
for _ in range(1000):
    step = lr * df(x_gd)
    x_gd -= step
    if abs(step) < 1e-6: break
print(f"Gradient Descent: x = {x_gd:.4f}")


x_newton = newton(df, 0, fprime=d2f)
print(f"Newton: x = {x_newton:.4f}")

res_slsqp = minimize(f, 0, method="SLSQP")
print(f"SLSQP: x = {res_slsqp.x[0]:.4f}")


def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

print("\n--- Part 2B ---")
for x0 in [0, 2]:
    print(f"\nStarting point x0 = {x0}")
    

    x_gd = x0
    lr = 0.01
    for _ in range(1000):
        step = lr * dg(x_gd)
        x_gd -= step
        if abs(step) < 1e-6: break
    print(f"Gradient Descent: x = {x_gd:.4f}")
    

    x_newt = newton(dg, x0, fprime=d2g)
    d2 = d2g(x_newt)
    point_type = "Minimum" if d2 > 0 else "Maximum"
    print(f"Newton: x = {x_newt:.4f} (d2g = {d2:.4f} -> {point_type})")
    

    res_sq = minimize(g, x0, method="SLSQP")
    print(f"SLSQP: x = {res_sq.x[0]:.4f}")