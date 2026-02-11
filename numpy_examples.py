"""
Runnable examples for NumPy exam methods.
Run: python numpy_examples.py

This script creates small sample files (CSV/NPZ) locally.
"""

import numpy as np

# 1) np.array + vector addition
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print("np.array a:", a)
print("vector add a+b:", a + b)

# 2) np.arange
x = np.arange(0, 10, 2)
print("np.arange(0,10,2):", x)

# 3) np.linspace
y = np.linspace(0, 1, 5)
print("np.linspace(0,1,5):", y)

# 4) np.random.choice
labels = np.array(["A", "B", "C"])
samples = np.random.choice(labels, size=10, replace=True, p=[0.5, 0.3, 0.2])
print("np.random.choice samples:", samples)

# 5) np.savez + load
arr1 = np.arange(5)
arr2 = np.linspace(0, 1, 3)
np.savez("data.npz", name1=arr1, name2=arr2)
loaded = np.load("data.npz")
print("np.savez files:", loaded.files)
print("loaded['name1']:", loaded["name1"])

# 6) np.loadtxt (create a CSV first)
csv_content = "x,y
1,10
2,20
3,30
"
with open("file.csv", "w", encoding="utf-8") as f:
    f.write(csv_content)

data = np.loadtxt("file.csv", delimiter=",", skiprows=1)
print("np.loadtxt data:
", data)

# 7) reshape
r = np.arange(12).reshape((3, 4))
print("reshape to (3,4):
", r)

# 8) transpose .T
print("transpose shape:", r.T.shape)

# 9) boolean indexing
z = np.array([1, 2, 3, 4, 5, 6])
evens = z[z % 2 == 0]
print("boolean indexing evens:", evens)
