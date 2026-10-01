import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

def k_imbalance(x):
    return (2*x)**2 / ((a-x)*(b-x)) - K


x_newton = newton(k_imbalance, 0.5)


def objective(x):
    return k_imbalance(x[0])**2

res = minimize(objective, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]

print(f"Extent x from Newton: {x_newton:.4f}")
print(f"Extent x from SLSQP: {x_slsqp:.4f}")


H2_eq = a - x_newton
I2_eq = b - x_newton
HI_eq = 2 * x_newton

print(f"\nEquilibrium Amounts:")
print(f"H2: {H2_eq:.4f} mol")
print(f"I2: {I2_eq:.4f} mol")
print(f"HI: {HI_eq:.4f} mol")

x_vals = np.linspace(0, 0.99, 100)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, a - x_vals, 'b-', label='H2')
plt.plot(x_vals, b - x_vals, 'g-', label='I2')
plt.plot(x_vals, 2 * x_vals, 'r-', label='HI')
plt.axvline(x_newton, color='k', linestyle='--', label=f'Equilibrium x={x_newton:.2f}')
plt.xlabel('Extent of reaction (x)')
plt.ylabel('Amount (mol)')
plt.title('Chemical Equilibrium: H2 + I2 <=> 2 HI')
plt.legend()
plt.grid(True)
plt.savefig('equilibrium.png')
print("Saved plot as equilibrium.png")