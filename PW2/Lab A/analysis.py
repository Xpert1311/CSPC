import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: Read freefall.csv into arrays t and y
data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: Compute velocity and acceleration using np.gradient
v = np.gradient(y, t)
a = np.gradient(v, t)

mean_acc = np.mean(a)
std_acc = np.std(a)

print(f"Mean acceleration: {mean_acc:.2f} m/s^2")
print(f"Standard deviation of acceleration: {std_acc:.2f} m/s^2")

# TODO 3: Integrate acceleration back up to recover velocity and position
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

max_diff = np.max(np.abs(y - y_rec))
print(f"Max difference between original and recovered position: {max_diff:.4f} m")

# TODO 4: Make a figure with 3 stacked panels and save as motion.png
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Position panel
ax1.plot(t, y, 'b-', label='Original Position')
ax1.plot(t, y_rec, 'r--', label='Recovered Position')
ax1.set_ylabel('Position (m)')
ax1.set_title('Motion Analysis from Free-Fall Tracking Data')
ax1.legend()
ax1.grid(True)

# Velocity panel
ax1_v = ax2.plot(t, v, 'g-', label='Velocity (gradient)')
ax2.set_ylabel('Velocity (m/s)')
ax2.legend()
ax2.grid(True)

# Acceleration panel
ax3.plot(t, a, 'm-', label='Acceleration (2x gradient)')
ax3.axhline(-9.81, color='k', linestyle='--', label='True g (-9.81 m/s²)')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Acceleration (m/s²)')
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.savefig('motion.png')
print("Figure saved as motion.png")