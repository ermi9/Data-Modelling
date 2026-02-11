"""
Runnable examples for Matplotlib exam methods.
Run: python matplotlib_examples.py

This script will open multiple plot windows (one per section).
Close a window to continue to the next.
"""

import numpy as np
import matplotlib.pyplot as plt

# 1) plt.figure(figsize=...)
plt.figure(figsize=(5, 3))
plt.plot([0, 1, 2], [0, 1, 4], label="line")
plt.title("plt.figure(figsize=(w,h))")
plt.legend()
plt.show()

# 2) plt.subplots(nrows, ncols)
x = np.linspace(0, 2*np.pi, 200)
fig, axes = plt.subplots(1, 2, figsize=(8, 3))
axes[0].plot(x, np.sin(x), label="sin")
axes[0].legend()
axes[0].set_title("Subplot 1")

axes[1].plot(x, np.cos(x), label="cos")
axes[1].legend()
axes[1].set_title("Subplot 2")

plt.tight_layout()
plt.show()

# 3) plt.scatter(x, y, s=...)
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 2, 5])
plt.figure(figsize=(4, 3))
plt.scatter(x, y, s=120, label="points")  # s, not size
plt.title("plt.scatter(..., s=...)")
plt.legend()
plt.show()

# 4) plt.errorbar(x, y, yerr=...)
x = np.array([1, 2, 3, 4])
y = np.array([2.0, 2.5, 3.2, 3.8])
err = np.array([0.2, 0.15, 0.25, 0.1])
plt.figure(figsize=(4, 3))
plt.errorbar(x, y, yerr=err, fmt="o", capsize=4, label="measurement")
plt.title("plt.errorbar(..., yerr=...)")
plt.legend()
plt.show()

# 5) ax.legend() vs plt.legend()
fig, ax = plt.subplots(figsize=(4, 3))
ax.plot([0, 1, 2], [0, 1, 4], label="line")
ax.scatter([0, 1, 2], [0, 1, 4], s=70, label="points")
ax.set_title("ax.legend()")
ax.legend()
plt.show()

# 6) ax.hist(data, bins='auto', density=True)
data = np.random.normal(0, 1, size=1000)
fig, ax = plt.subplots(figsize=(5, 3))
ax.hist(data, bins="auto", density=True, label="N(0,1)")
ax.set_title("ax.hist(..., density=True)")
ax.legend()
plt.show()

# 7) 3D plotting surface
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection="3d")

x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

ax.plot_surface(X, Y, Z)
ax.set_title("3D surface (projection='3d')")
plt.show()
