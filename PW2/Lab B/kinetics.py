import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


data = np.loadtxt('kinetics.csv', delimiter=',', skiprows=1)
t = data[:, 0]
C = data[:, 1]
C0 = C[0]


def total_error(k):
    return np.sum((C - C0 * np.exp(-k[0] * t))**2)


res = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fit = res.x[0]
print(f"Fitted rate constant k: {k_fit:.4f}")


plt.figure(figsize=(8, 5))
plt.plot(t, C, 'bo', label='Measured Data')
plt.plot(t, C0 * np.exp(-k_fit * t), 'r-', label=f'Fitted Curve (k={k_fit:.4f})')
plt.xlabel('Time (s)')
plt.ylabel('Concentration')
plt.title('Kinetics: First-Order Reaction Fit')
plt.legend()
plt.grid(True)
plt.savefig('kinetics.png')
print("Saved plot as kinetics.png")