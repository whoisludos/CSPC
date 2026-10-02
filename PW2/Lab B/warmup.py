import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------

def f(x):
    return (x - 3)**2 + 1

def df(x):
    return 2 * (x - 3)

def d2f(x):
    return 2.0

# Gradient descent
x = 0
lr = 0.1

for i in range(1000):
    new_x = x - lr * df(x)

    if abs(new_x - x) < 1e-8:
        break

    x = new_x

print("2A")
print("Gradient descent:", x)

# Newton
x_newton = newton(df, 0, fprime=d2f)
print("Newton:", x_newton)

# SLSQP
result = minimize(f, 0, method="SLSQP")
print("SLSQP:", result.x[0])

# ---------- 2B: harder landscape ----------

def g(x):
    return x**4 - 3*x**2 + x + 5

def dg(x):
    return 4*x**3 - 6*x + 1

def d2g(x):
    return 12*x**2 - 6

# Try both starting points
for x0 in [0, 2]:

    # Gradient descent
    x = x0
    lr = 0.05

    for i in range(1000):
        new_x = x - lr * dg(x)

        if abs(new_x - x) < 1e-8:
            break

        x = new_x

    print("\n2B, starting at", x0)
    print("Gradient descent:", x)

    # Newton
    x_newton = newton(dg, x0, fprime=d2g)
    print("Newton:", x_newton)
    print("Second derivative:", d2g(x_newton))

    # SLSQP
    result = minimize(g, x0, method="SLSQP")
    print("SLSQP:", result.x[0])
