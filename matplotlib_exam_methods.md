# Matplotlib — Exam Methods Cheat Sheet (import matplotlib.pyplot as plt)

This file gives **method signatures**, **syntax breakdown**, **concrete examples**, and **nuances/gotchas** for the Matplotlib methods you listed.

---

## 1) `plt.figure`

### What it does
Creates a **new figure** (a top-level container for one or more Axes/plots).

### Signature (common)
```py
plt.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, ...) -> matplotlib.figure.Figure
```

### Your exam syntax
```py
plt.figure(figsize=(width, height))
```

### Syntax breakdown
- `figsize=(width, height)` is a **tuple in inches** (not pixels).
- The returned object is a `Figure` (often stored as `fig`).

### Concrete example
```py
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
plt.plot([0, 1, 2], [0, 1, 4])
plt.title("Simple line")
plt.show()
```

### Nuances / gotchas
- Inches matter: if you want pixels, it’s roughly `pixels = inches * dpi`.
- Calling `plt.figure()` multiple times creates multiple figures.
- If you use `plt.figure()` without plotting, you get a blank figure.

---

## 2) `plt.subplots`

### What it does
Creates a `Figure` and a grid of `Axes` objects (subplots).

### Signature (common)
```py
plt.subplots(nrows=1, ncols=1, figsize=None, sharex=False, sharey=False, squeeze=True, ...) -> (Figure, Axes)
```

### Your exam syntax
```py
fig, axes = plt.subplots(nrows, ncols)
```

### Syntax breakdown
- Returns a tuple: `(fig, axes)`
- `axes` can be:
  - a single `Axes` object (if 1x1 and `squeeze=True`)
  - a 1D array of Axes (e.g., 1x3)
  - a 2D array of Axes (e.g., 2x2)

### Concrete example (2 rows x 1 col)
```py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 200)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axes = plt.subplots(2, 1, figsize=(6, 6))

axes[0].plot(x, y1, label="sin")
axes[0].legend()
axes[0].set_title("Sine")

axes[1].plot(x, y2, label="cos")
axes[1].legend()
axes[1].set_title("Cosine")

plt.tight_layout()
plt.show()
```

### Nuances / gotchas
- If `nrows=ncols=1`, `axes` is **not an array**; it’s a single Axes:
  ```py
  fig, ax = plt.subplots()
  ```
- If you want `axes` always as an array, set `squeeze=False`.

---

## 3) `plt.scatter`

### What it does
Creates a scatter plot: points at `(x, y)`.

### Signature (common)
```py
plt.scatter(x, y, s=None, c=None, marker=None, alpha=None, label=None, ...) -> PathCollection
```

### Your exam syntax
```py
plt.scatter(x, y, s=size)
```

### Key parameter note (exam point)
- The marker size parameter is **`s`**, **NOT** `size`.

### Concrete example
```py
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 2, 5])

plt.figure(figsize=(5, 4))
plt.scatter(x, y, s=80, label="points")
plt.legend()
plt.show()
```

### Nuances / gotchas
- `s` is area in points² (so doubling `s` does not double radius; it doubles area).
- If you want a legend, pass `label="..."` and call `plt.legend()` (or `ax.legend()`).

---

## 4) `plt.errorbar`

### What it does
Plots points/lines with error bars (uncertainty) in y and/or x.

### Signature (common)
```py
plt.errorbar(x, y, yerr=None, xerr=None, fmt='', ecolor=None, capsize=None, label=None, ...) -> ErrorbarContainer
```

### Your exam syntax
```py
plt.errorbar(x, y, yerr=error_values)
```

### Syntax breakdown
- `yerr=`: vertical error bars (can be scalar, 1D array, or shape (2, N) for asymmetric errors)
- `xerr=`: horizontal error bars

### Concrete example
```py
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([2.0, 2.5, 3.2, 3.8])
err = np.array([0.2, 0.15, 0.25, 0.1])

plt.figure(figsize=(5, 4))
plt.errorbar(x, y, yerr=err, fmt="o", capsize=4, label="measurement")
plt.legend()
plt.show()
```

### Nuances / gotchas
- Parameter names are `yerr` and `xerr` (common exam trap).
- `fmt="o"` makes markers. If `fmt=""`, you might not see points unless you specify marker/linestyle.
- Asymmetric errors use shape `(2, N)`:
  ```py
  yerr = np.vstack([lower_errors, upper_errors])
  ```

---

## 5) `plt.legend` vs `ax.legend`

### What it does
Adds a legend describing labeled plot elements.

### Signatures (common)
```py
plt.legend(*args, **kwargs) -> Legend
ax.legend(*args, **kwargs) -> Legend
```

### Your exam syntax
```py
plt.legend()
# or
ax.legend()
```

### Distinction (exam point)
- `ax.legend()` attaches the legend to a **specific Axes**.
- `plt.legend()` operates on the **current Axes** (whatever Matplotlib thinks is “active”).

### Concrete example (Axes-level recommended)
```py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 4))
ax.plot([0, 1, 2], [0, 1, 4], label="line")
ax.scatter([0, 1, 2], [0, 1, 4], s=60, label="points")
ax.legend()
plt.show()
```

### Nuances / gotchas
- In multi-subplot figures, prefer `ax.legend()` so you don’t put the legend on the wrong subplot.

---

## 6) `ax.hist`

### What it does
Plots a histogram of data (counts or density).

### Signature (common)
```py
ax.hist(x, bins=None, density=False, range=None, histtype='bar', alpha=None, label=None, ...) -> (n, bins, patches)
```

### Your exam syntax
```py
ax.hist(data, bins='auto', density=True)
```

### Syntax breakdown
- `bins`:
  - an int (e.g., 20), or
  - a sequence of bin edges, or
  - a strategy string like `'auto'`
- `density=True` normalizes so the **total area** under the histogram is 1

### Concrete example
```py
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=0, scale=1, size=1000)

fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(data, bins="auto", density=True, label="N(0,1)")
ax.legend()
plt.show()
```

### Nuances / gotchas
- With `density=True`, y-axis is **probability density**, not counts.
- Passing multiple datasets changes behavior:
  ```py
  ax.hist([data1, data2], bins=20)
  ```

---

## 7) 3D plotting (`projection='3d'` + `plot_surface`)

### What it does
Creates 3D axes and plots a 3D surface (or other 3D plots).

### Canonical exam syntax
```py
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(...)
```

### Concrete example (surface)
```py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection="3d")

x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

ax.plot_surface(X, Y, Z)
plt.show()
```

### Nuances / gotchas
- The key requirement is `projection='3d'`.
- You typically need `X, Y` from `np.meshgrid` for surfaces.
- `plot_surface` expects 2D arrays for X, Y, Z with matching shapes.

---

# Mini exam checklist
- Figure size in **inches**: `plt.figure(figsize=(w,h))`
- Subplots returns `(Figure, Axes)` and `axes` shape depends on `nrows/ncols`
- Scatter marker size parameter is **`s`**
- Error bars: `yerr` / `xerr`
- Prefer `ax.legend()` in multi-axes figures
- Histogram: `density=True` means **area = 1**
- 3D requires `projection='3d'`
