import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)

data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)

t = data[:, 0]
y = data[:, 1]


# TODO 2: compute velocity v = derivative of y w.r.t. t
#         and acceleration a = derivative of v w.r.t. t
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?

v = np.gradient(y, t)

a = np.gradient(v, t)

print("Mean acceleration:", np.mean(a))
print("Standard deviation of acceleration:", np.std(a))


# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)

v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]

y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

difference = np.abs(y_recovered - y)

print("Largest difference in position:", np.max(difference))


# TODO 4: make a figure with 3 stacked panels:
#         position, velocity, acceleration vs time.
#         Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png

fig, axes = plt.subplots(3, 1, sharex=True, figsize=(10, 8))

# Position
axes[0].plot(t, y)
axes[0].set_ylabel("Position (m)")
axes[0].set_title("Motion from Tracking Data")
axes[0].grid(True)

# Velocity
axes[1].plot(t, v)
axes[1].set_ylabel("Velocity (m/s)")
axes[1].grid(True)

# Acceleration
axes[2].plot(t, a)
axes[2].axhline(-9.81, linestyle="--", label="True acceleration = -9.81 m/s²")
axes[2].set_xlabel("Time (s)")
axes[2].set_ylabel("Acceleration (m/s²)")
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.savefig("motion.png")
plt.show()
