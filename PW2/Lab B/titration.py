import numpy as np
import matplotlib.pyplot as plt

# TODO 1: Read titration.csv
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)

V = data[:, 0]
pH = data[:, 1]

# TODO 2: Compute the slope and find the equivalence point
slope = np.gradient(pH, V)

equivalence_index = np.argmax(slope)
equivalence_volume = V[equivalence_index]

print("Equivalence point volume:", equivalence_volume)
print("Maximum slope:", slope[equivalence_index])

# TODO 3: Make two plots side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: pH vs volume
axes[0].plot(V, pH)
axes[0].axvline(equivalence_volume, linestyle="--")
axes[0].set_xlabel("Volume of base added")
axes[0].set_ylabel("pH")
axes[0].set_title("Titration Curve")

# Right: slope vs volume
axes[1].plot(V, slope)
axes[1].axvline(equivalence_volume, linestyle="--")
axes[1].set_xlabel("Volume of base added")
axes[1].set_ylabel("dpH/dV")
axes[1].set_title("Slope of Titration Curve")

plt.tight_layout()
plt.savefig("titration.png")
plt.show()
