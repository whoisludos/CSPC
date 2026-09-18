import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3    #decay constant, given

data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]    #quest 1

N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)    #quest 2

fig, axes = plt.subplots(1, 2, sharex=True, sharey=True)
axes[0].scatter(t, observed)
axes[0].set_title("Observed data")
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Count")    #quest 3
axes[1].plot(t, analytical)
axes[1].set_title("Analytical")
axes[1].set_xlabel("Time")
axes[1].set_ylabel("Count")

plt.savefig("figure.png")    #quest 4
