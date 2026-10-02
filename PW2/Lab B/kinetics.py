import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Read the data from the csv file
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)

t = data[:, 0]
C = data[:, 1]

# The first concentration is C0
C0 = C[0]

# Calculate the total error for a given k
def total_error(k):
    k = k[0]
    predicted = C0 * np.exp(-k * t)
    error = np.sum((C - predicted)**2)
    return error

# Find the value of k that gives the smallest error
result = minimize(
    total_error,
    [0.5],
    method="SLSQP",
    bounds=[(0, 5)]
)

k = result.x[0]

print("Fitted k =", k)

# Calculate the fitted curve
fitted_C = C0 * np.exp(-k * t)

# Plot the measured data and fitted curve
plt.scatter(t, C, label="Measured data")
plt.plot(t, fitted_C, label="Fitted curve")

plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.tight_layout()

plt.savefig("kinetics.png")
plt.show()
