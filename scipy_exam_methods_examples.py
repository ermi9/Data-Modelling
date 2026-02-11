"""
Runnable examples for SciPy exam methods (by submodule).
Run: python scipy_exam_methods_examples.py

Notes:
- SciPy must be installed.
- Some functions (filters) are demonstrated on synthetic signals.
"""

import numpy as np
from scipy import signal, optimize, integrate, stats, interpolate, linalg, fft, constants

print("=== scipy.signal.resample ===")
t = np.linspace(0, 1, 100, endpoint=False)
x = np.sin(2*np.pi*5*t)
y = signal.resample(x, 200)
print("original len:", len(x), "resampled len:", len(y))

print("
=== scipy.signal.find_peaks ===")
sig = np.array([0, 1, 0, 0.5, 0, 2, 0, 1.2, 0])
peaks, props = signal.find_peaks(sig, prominence=0.8)
print("peaks idx:", peaks)
print("prominences:", props.get("prominences"))

print("
=== scipy.signal.butter ===")
fs = 1000
cutoff = 50
b, a = signal.butter(4, cutoff, btype="low", fs=fs)
print("butter b len:", len(b), "a len:", len(a))

print("
=== scipy.signal.detrend ===")
t = np.linspace(0, 10, 200)
x = 0.5*t + np.sin(t)
xd = signal.detrend(x)
print("mean before:", float(np.mean(x)), "after detrend mean:", float(np.mean(xd)))

print("
=== scipy.optimize.curve_fit ===")
def model(x, m, b):
    return m*x + b

xdata = np.array([0, 1, 2, 3], dtype=float)
ydata = np.array([1.0, 2.1, 3.9, 6.2], dtype=float)
popt, pcov = optimize.curve_fit(model, xdata, ydata, p0=[1, 0])
print("popt (m,b):", popt)

print("
=== scipy.optimize.fsolve ===")
def f(x):
    return x**2 - 2

root = optimize.fsolve(f, x0=1.0)
print("root:", root)

print("
=== scipy.integrate.odeint ===")
k = 0.5
def dydt(y, t):
    return -k * y

t = np.linspace(0, 10, 100)
y0 = 2.0
y = integrate.odeint(dydt, y0, t)
print("odeint output shape:", y.shape, "y(t_end):", y[-1,0])

print("
=== scipy.stats.linregress ===")
x = np.array([0, 1, 2, 3], dtype=float)
y = np.array([1.0, 2.0, 2.9, 4.1], dtype=float)
res = stats.linregress(x, y)
print("slope:", res.slope, "intercept:", res.intercept, "rvalue:", res.rvalue)

print("
=== scipy.interpolate.interp1d ===")
x = np.array([0, 1, 2, 3], dtype=float)
y = np.array([0, 1, 4, 9], dtype=float)
f = interpolate.interp1d(x, y, kind="linear", fill_value="extrapolate")
print("f(1.5):", float(f(1.5)), "f(5.0):", float(f(5.0)))

print("
=== scipy.linalg.det ===")
A = np.array([[1, 2], [3, 4]], dtype=float)
print("det(A):", float(linalg.det(A)))

print("
=== scipy.fft.fftfreq ===")
n = 8
dt = 0.1
freqs = fft.fftfreq(n, d=dt)
print("freqs:", freqs)

print("
=== scipy.constants ===")
print("c:", constants.c)
print("h:", constants.h)
