# NumPy — Exam Methods Cheat Sheet (import numpy as np)

This file gives **method signatures**, **syntax breakdown**, **concrete examples**, and **nuances/gotchas** for the NumPy methods you listed.

---

## 1) `np.array`

### What it does
Creates a NumPy `ndarray` from a Python sequence (list/tuple), nested sequences (for 2D+), or any array-like.

### Signature (common)
```py
np.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0) -> np.ndarray
```

### Your exam syntax
```py
np.array([1, 2, 3])
```

### Syntax breakdown
- `object`: list/tuple/nested lists, or another array-like
- `dtype`: force a data type (e.g., `dtype=float`)
- `copy`: whether to copy data (default True)
- `ndmin`: ensure at least N dimensions

### Concrete example (vector addition)
```py
import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)  # [11 22 33] element-wise
```

### Nuances / gotchas
- Element-wise arithmetic is default (`+`, `-`, `*`, `/`).
- Dot product is different:
  ```py
  a @ b        # dot product for 1D vectors
  # vs
  a * b        # element-wise product
  ```
- Mixed types get upcast:
  ```py
  np.array([1, 2.5, 3]).dtype  # float
  ```

---

## 2) `np.arange`

### What it does
Returns evenly spaced values over a half-open interval **[start, stop)** using a step.

### Signature (common)
```py
np.arange([start,] stop[, step], dtype=None) -> np.ndarray
```

### Your exam syntax
```py
np.arange(start, stop, step)
```

### Concrete example
```py
x = np.arange(0, 10, 2)
print(x)  # [0 2 4 6 8]
```

### Nuances / gotchas
- `stop` is **excluded**.
- With floats, `arange` may have rounding issues:
  ```py
  np.arange(0, 1, 0.1)  # not always exact endpoints
  ```
  For “N equally spaced points” prefer `np.linspace`.

---

## 3) `np.linspace`

### What it does
Returns `num` evenly spaced samples over **[start, stop]** (stop included by default).

### Signature (common)
```py
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0) -> np.ndarray
```

### Your exam syntax
```py
np.linspace(start, stop, num)
```

### Concrete example
```py
x = np.linspace(0, 1, 5)
print(x)  # [0.   0.25 0.5  0.75 1.  ]
```

### Nuances / gotchas
- If `endpoint=False`, stop is excluded:
  ```py
  np.linspace(0, 1, 5, endpoint=False)
  ```
- `retstep=True` returns the step size too:
  ```py
  x, step = np.linspace(0, 1, 5, retstep=True)
  ```

---

## 4) `np.random.choice`

### What it does
Randomly samples from a 1D array-like or from `np.arange(a)` if `a` is an int.

### Signature (common)
```py
np.random.choice(a, size=None, replace=True, p=None) -> np.ndarray | scalar
```

### Your exam syntax
```py
np.random.choice(a, size=100, replace=True, p=[0.5, 0.3, ...])
```

### Syntax breakdown
- `a`: int `n` (samples from `0..n-1`) **or** an array of labels
- `size`: number/shape of draws
- `replace=True`: sampling **with replacement**
- `p`: probabilities (same length as `a`, sums to 1)

### Concrete example (custom probabilities)
```py
labels = np.array(["A", "B", "C"])
samples = np.random.choice(labels, size=10, replace=True, p=[0.5, 0.3, 0.2])
print(samples)
```

### Nuances / gotchas
- `p` must match `len(a)` and sum to 1 (within tolerance), otherwise `ValueError`.
- If `replace=False`, you cannot sample more than `len(a)`.
- Reproducibility: use a generator
  ```py
  rng = np.random.default_rng(0)
  rng.choice(labels, size=5, replace=True, p=[0.5, 0.3, 0.2])
  ```

---

## 5) `np.savez`

### What it does
Saves multiple arrays into one uncompressed `.npz` archive.

### Signature (common)
```py
np.savez(file, *args, **kwds) -> None
```

### Your exam syntax
```py
np.savez('file.npz', name1=array1, name2=array2)
```

### Concrete example
```py
a = np.arange(5)
b = np.linspace(0, 1, 3)

np.savez("data.npz", name1=a, name2=b)

loaded = np.load("data.npz")
print(loaded.files)     # ['name1', 'name2']
print(loaded["name1"])  # [0 1 2 3 4]
```

### Nuances / gotchas
- Keyword args set internal names (`name1=a`).
- Positional args become `arr_0`, `arr_1`, ...
- For compressed version: `np.savez_compressed(...)` (different function).

---

## 6) `np.loadtxt`

### What it does
Loads numerical data from a text file (e.g., CSV) into a NumPy array.

### Signature (common)
```py
np.loadtxt(fname, dtype=float, delimiter=None, skiprows=0, usecols=None, ...) -> np.ndarray
```

### Your exam syntax
```py
np.loadtxt('file.csv', delimiter=',', skiprows=1)
```

### Concrete example
```py
# file.csv:
# x,y
# 1,10
# 2,20
# 3,30

data = np.loadtxt("file.csv", delimiter=",", skiprows=1)
print(data)
# [[ 1. 10.]
#  [ 2. 20.]
#  [ 3. 30.]]
```

### Nuances / gotchas
- `skiprows=1` skips header row.
- `loadtxt` expects numeric content; for missing values or mixed types use `np.genfromtxt`.
- Wrong delimiter is the #1 reason it “doesn’t work”.

---

## 7) `np.reshape` / `.reshape()`

### What it does
Gives a new shape to an array without changing its data.

### Signature (method form)
```py
a.reshape(newshape, order='C') -> np.ndarray
```

### Your exam syntax
```py
a.reshape(new_shape)
```

### Concrete example
```py
a = np.arange(12)
b = a.reshape((3, 4))
print(b.shape)  # (3, 4)
```

### Nuances / gotchas
- Often returns a **view** if possible (no copy):
  ```py
  a = np.arange(6)
  b = a.reshape((2,3))
  b[0,0] = 999
  print(a[0])  # 999
  ```
- One dimension can be inferred with `-1`:
  ```py
  a.reshape((3, -1))
  ```
- Total elements must match the new shape or `ValueError`.

---

## 8) `.T` (transpose)

### What it does
Returns the transpose: swaps axes.

### Signature (property)
```py
array.T -> np.ndarray
```

### Your exam syntax
```py
array.T
```

### Concrete example
```py
A = np.array([[1,2,3],
              [4,5,6]])  # shape (2,3)
print(A.T.shape)         # (3,2)
```

### Nuances / gotchas
- For 1D arrays, transpose does nothing:
  ```py
  v = np.array([1,2,3])
  v.T.shape  # (3,)
  ```
  To force a column vector: `v.reshape(-1, 1)`.

---

## 9) Boolean indexing (filtering)

### What it does
Selects elements where a condition is True.

### Pattern
```py
x[mask]
```

### Your exam syntax
```py
x[x % 2 == 0]
```

### Concrete example
```py
x = np.array([1,2,3,4,5,6])
evens = x[x % 2 == 0]
print(evens)  # [2 4 6]
```

### Nuances / gotchas
- Boolean indexing creates a **copy**, not a view:
  ```py
  y = x[x % 2 == 0]
  y[0] = 999
  print(x)  # unchanged
  ```
- To modify in place, index on the left:
  ```py
  x[x % 2 == 0] = 0
  ```

---

# Quick exam checklist
- Element-wise addition: `a + b`
- `arange`: step-based, stop excluded
- `linspace`: N points, stop included by default
- `choice`: `p=` probabilities, `replace=True` for replacement
- `savez`: keyword names inside `.npz`
- `loadtxt`: delimiter + skiprows for headers
- `reshape`: often view; `-1` to infer
- `.T`: swaps axes, no effect for 1D
- Boolean indexing: returns copy
