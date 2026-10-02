import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# Calculate how far we are from the equilibrium condition
def k_imbalance(x):
    return (2 * x)**2 / ((a - x) * (b - x)) - K

# Method 1: Newton root finding
x_newton = newton(k_imbalance, 0.5)

print("Newton result:", x_newton)


# Method 2: SLSQP minimisation
def squared_imbalance(x):
    return k_imbalance(x[0])**2

result = minimize(
    squared_imbalance,
    [0.5],
    method="SLSQP",
    bounds=[(0, 0.999)]
)

x_minimize = result.x[0]

print("SLSQP result:", x_minimize)

# Equilibrium amounts
H2_eq = a - x_newton
I2_eq = b - x_newton
HI_eq = 2 * x_newton

print("\nEquilibrium amounts:")
print("H2 =", H2_eq, "mol")
print("I2 =", I2_eq, "mol")
print("HI =", HI_eq, "mol")

# Values for the plot
x_values = np.linspace(0, 0.999, 200)

H2_values = a - x_values
I2_values = b - x_values
HI_values = 2 * x_values

# Plot the amounts as the reaction proceeds
plt.plot(x_values, H2_values, label="H2")
plt.plot(x_values, I2_values, label="I2")
plt.plot(x_values, HI_values, label="HI")

# Mark the equilibrium point
plt.axvline(x_newton, linestyle="--", label="Equilibrium")

plt.xlabel("Extent of reaction, x")
plt.ylabel("Amount (mol)")
plt.legend()
plt.tight_layout()

plt.savefig("equilibrium.png")
plt.show()
