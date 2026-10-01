import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('titration.csv', delimiter=',', skiprows=1)
V = data[:, 0]
pH = data[:, 1]


slope = np.gradient(pH, V)
eq_idx = np.argmax(slope)
eq_vol = V[eq_idx]
print(f"Equivalence point volume: {eq_vol:.2f} mL")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(V, pH, 'b.-', label='pH curve')
ax1.axvline(eq_vol, color='r', linestyle='--', label=f'Eq Point ({eq_vol} mL)')
ax1.set_xlabel('Volume of base (mL)')
ax1.set_ylabel('pH')
ax1.set_title('Titration Curve')
ax1.legend()
ax1.grid(True)

ax2.plot(V, slope, 'g.-', label='Slope (dpH/dV)')
ax2.axvline(eq_vol, color='r', linestyle='--', label=f'Max Slope ({eq_vol} mL)')
ax2.set_xlabel('Volume of base (mL)')
ax2.set_ylabel('Slope')
ax2.set_title('Derivative of pH')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('titration.png')
print("Saved plot as titration.png")