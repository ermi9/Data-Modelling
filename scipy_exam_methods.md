# SciPy — Exam Methods Cheat Sheet (by submodule)

This file gives **method signatures**, **syntax breakdown**, **concrete examples**, and **nuances/gotchas** for the SciPy methods/properties you listed.

> Typical imports you’ll see in exams:
> ```py
> import numpy as np
> from scipy import signal, optimize, integrate, stats, interpolate, linalg, fft, constants
> ```

---

# `scipy.signal`

## 1) `signal.resample(x, num)`

### What it does
Resamples a signal `x` to exactly `num` points using a **Fourier method** (frequency-domain resampling).

### Signature (common)
```py
scipy.signal.resample(x, num, t=None, axis=0, window=None, domain='time') -> y  (and optionally new_t)
```

### Your exam syntax
```py
signal.resample(x, num)
```

### Concrete example
```py
import numpy as np
from scipy import signal

t = np.linspace(0, 1, 100, endpoint=False)
x = np.sin(2*np.pi*5*t)          # 5 Hz sine, 100 samples

y = signal.resample(x, 200)      # resample to 200 samples
print(x.shape, y.shape)          # (100,) (200,)
```

### Nuances / gotchas
- Because it’s FFT-based, it assumes periodicity and can introduce ringing if the signal has sharp edges.
- If you want resampling with **anti-aliasing FIR filtering**, `signal.resample_poly` is often better (different function).
- If `t` is provided, SciPy can return the new time base too.

---

## 2) `signal.find_peaks(x, prominence=1.0)`

### What it does
Finds indices of local maxima (“peaks”) in a 1D signal.

### Signature (common)
```py
scipy.signal.find_peaks(x, height=None, threshold=None, distance=None, prominence=None, width=None, ...) -> (peaks, properties)
```

### Your exam syntax
```py
signal.find_peaks(x, prominence=1.0)
```

### Parameter focus: `prominence`
Prominence measures how much a peak stands out compared to its surrounding “baseline” (vertical distance from the peak to its lowest contour line).

### Concrete example
```py
import numpy as np
from scipy import signal

x = np.array([0, 1, 0, 0.5, 0, 2, 0, 1.2, 0])
peaks, props = signal.find_peaks(x, prominence=0.8)
print(peaks)          # e.g., [5 7] depending on threshold
print(props["prominences"])
```

### Nuances / gotchas
- Returns **indices**, not x-values.
- You also get a `properties` dict (contains prominences, widths, etc., depending on options).
- Other exam-relevant constraints often used: `height=...`, `distance=...`.

---

## 3) `signal.butter(N, Wn, btype='low')`

### What it does
Designs a digital or analog **Butterworth** filter and returns filter coefficients.

### Signature (common)
```py
scipy.signal.butter(N, Wn, btype='low', analog=False, output='ba', fs=None) -> (b, a) or other outputs
```

### Your exam syntax
```py
signal.butter(N, Wn, btype='low')
```

### Parameters
- `N`: filter order
- `Wn`: critical frequency (meaning depends on whether `fs` is given)
- `btype`: `'low'`, `'high'`, `'bandpass'`, `'bandstop'`

### Concrete example (digital low-pass, with sampling rate)
```py
import numpy as np
from scipy import signal

fs = 1000  # Hz sampling rate
cutoff = 50  # Hz cutoff
b, a = signal.butter(N=4, Wn=cutoff, btype="low", fs=fs)

# Apply to data (common next step):
t = np.linspace(0, 1, fs, endpoint=False)
x = np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*200*t)  # low + high freq
y = signal.filtfilt(b, a, x)  # zero-phase filtering
```

### Nuances / gotchas (big exam traps)
- **Interpretation of `Wn`:**
  - If you pass `fs=...`, then `Wn` is in **Hz**.
  - If you don’t pass `fs`, `Wn` must be **normalized** to Nyquist (0..1).
    - Example: `Wn = cutoff / (fs/2)`
- `output='ba'` returns `(b, a)`; other outputs exist (e.g., `sos` for stability).

---

## 4) `signal.detrend(x, axis=0)`

### What it does
Removes a trend from a signal (by default, removes a best-fit **linear** trend).

### Signature (common)
```py
scipy.signal.detrend(data, axis=-1, type='linear', bp=0, overwrite_data=False) -> ndarray
```

### Your exam syntax
```py
signal.detrend(x, axis=0)
```

### Concrete example
```py
import numpy as np
from scipy import signal

t = np.linspace(0, 10, 200)
x = 0.5*t + np.sin(t)        # linear trend + oscillation
y = signal.detrend(x)        # removes the linear trend
```

### Nuances / gotchas
- `type='linear'` removes linear trend; `type='constant'` removes mean only.
- Works along a specified axis for 2D arrays.

---

# `scipy.optimize`

## 5) `optimize.curve_fit(f, xdata, ydata, p0=guess)`

### What it does
Fits a model function `f` to data using **non-linear least squares**.

### Signature (common)
```py
scipy.optimize.curve_fit(f, xdata, ydata, p0=None, sigma=None, absolute_sigma=False, bounds=(-inf, inf), ...) -> (popt, pcov)
```

### Your exam syntax
```py
optimize.curve_fit(f, xdata, ydata, p0=guess)
```

### Concrete example (fit a line)
```py
import numpy as np
from scipy import optimize

def model(x, m, b):
    return m*x + b

xdata = np.array([0, 1, 2, 3])
ydata = np.array([1.0, 2.1, 3.9, 6.2])

popt, pcov = optimize.curve_fit(model, xdata, ydata, p0=[1, 0])
m_hat, b_hat = popt
print(m_hat, b_hat)
```

### Nuances / gotchas
- Your model must be `f(x, *params)` (x first, then parameters).
- `p0` matters a lot for non-linear problems; bad initial guesses can fail or converge to wrong solutions.
- `bounds=(lower, upper)` constrains parameters.
- `pcov` is the estimated covariance matrix of parameters.

---

## 6) `optimize.fsolve(func, x0)`

### What it does
Finds roots of a function: solves `func(x) = 0`.

### Signature (common)
```py
scipy.optimize.fsolve(func, x0, args=(), fprime=None, full_output=False, ...) -> x
```

### Your exam syntax
```py
optimize.fsolve(func, x0)
```

### Concrete example
```py
import numpy as np
from scipy import optimize

def func(x):
    return x**2 - 2  # root at sqrt(2)

root = optimize.fsolve(func, x0=1.0)
print(root)  # ~ [1.41421356]
```

### Nuances / gotchas
- `x0` is an initial guess; different guesses can converge to different roots (or fail).
- Return type is often an array even for 1D problems.
- For scalar root-finding, `optimize.root_scalar` can be simpler (different function).

---

# `scipy.integrate`

## 7) `integrate.odeint(func, y0, t)`

### What it does
Integrates a system of ODEs: computes `y(t)` given derivative function `func`.

### Signature (common)
```py
scipy.integrate.odeint(func, y0, t, args=(), Dfun=None, ...) -> ndarray
```

### Your exam syntax
```py
integrate.odeint(func, y0, t)
```

### Concrete example (exponential decay dy/dt = -k y)
```py
import numpy as np
from scipy import integrate

k = 0.5

def dydt(y, t):
    return -k * y

t = np.linspace(0, 10, 100)
y0 = 2.0
y = integrate.odeint(dydt, y0, t)   # shape (len(t), 1)
```

### Nuances / gotchas
- `odeint` expects derivative signature **`func(y, t, ...)`** (note order).
- Returns an array with shape `(len(t), len(y0))`.
- In modern SciPy, `solve_ivp` is often preferred, but exams still use `odeint` a lot.

---

# `scipy.stats`

## 8) `stats.linregress(x, y)`

### What it does
Performs linear least-squares regression on two sets of measurements.

### Signature (common)
```py
scipy.stats.linregress(x, y) -> LinregressResult
```
Result fields commonly include: `slope`, `intercept`, `rvalue`, `pvalue`, `stderr` (and sometimes `intercept_stderr`).

### Your exam return list
- slope, intercept, r_value, p_value, std_err

### Concrete example
```py
import numpy as np
from scipy import stats

x = np.array([0, 1, 2, 3])
y = np.array([1.0, 2.0, 2.9, 4.1])

res = stats.linregress(x, y)
print(res.slope, res.intercept, res.rvalue, res.pvalue, res.stderr)
```

### Nuances / gotchas
- `rvalue` is correlation coefficient (often written as `r_value` in notes).
- This is **simple linear regression** (one x predictor).

---

# `scipy.interpolate`

## 9) `interpolate.interp1d(x, y, kind='linear', fill_value='extrapolate')`

### What it does
Builds a 1D interpolating function from discrete data points.

### Signature (common)
```py
scipy.interpolate.interp1d(x, y, kind='linear', axis=-1, fill_value=np.nan, bounds_error=True, assume_sorted=False) -> callable
```

### Your exam syntax
```py
interpolate.interp1d(x, y, kind='linear', fill_value='extrapolate')
```

### Concrete example
```py
import numpy as np
from scipy import interpolate

x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 4, 9])  # y = x^2 at these points

f = interpolate.interp1d(x, y, kind="linear", fill_value="extrapolate")
print(f(1.5))   # interpolated between 1 and 2
print(f(5.0))   # extrapolated beyond range
```

### Nuances / gotchas
- `fill_value="extrapolate"` allows evaluation outside original x-range.
- If `bounds_error=True` (default), evaluating outside range can raise an error unless `fill_value` handles it.
- If `x` is not sorted and `assume_sorted=False`, SciPy will sort internally.

---

# `scipy.linalg`

## 10) `linalg.det(A)`

### What it does
Computes determinant of a square matrix `A`.

### Signature (common)
```py
scipy.linalg.det(a, overwrite_a=False, check_finite=True) -> float
```

### Your exam syntax
```py
linalg.det(A)
```

### Concrete example
```py
import numpy as np
from scipy import linalg

A = np.array([[1, 2],
              [3, 4]])
print(linalg.det(A))  # -2.0
```

### Nuances / gotchas
- Determinant can be very sensitive numerically for large matrices.
- Input must be square; otherwise you’ll get an error.

---

# `scipy.fft`

## 11) `fft.fftfreq(n, d=timestep)`

### What it does
Returns the frequency bins for a DFT of length `n` with sample spacing `d` seconds.

### Signature (common)
```py
scipy.fft.fftfreq(n, d=1.0) -> ndarray
```

### Your exam syntax
```py
fft.fftfreq(n, d=timestep)
```

### Concrete example
```py
import numpy as np
from scipy import fft

n = 8
dt = 0.1
freqs = fft.fftfreq(n, d=dt)
print(freqs)  # [ 0.    1.25  2.5   3.75 -5.   -3.75 -2.5  -1.25 ]
```

### Nuances / gotchas
- Output ordering includes negative frequencies (standard FFT ordering).
- Frequency resolution is `1/(n*d)`.
- Common pair in signal analysis: `freqs = fftfreq(...); X = fft(x)`.

---

# `scipy.constants`

## 12) Physical constants: `constants.c`, `constants.h`

### What they are
- `constants.c`: speed of light in vacuum (m/s)
- `constants.h`: Planck constant (J·s)

### Usage example
```py
from scipy import constants

print(constants.c)
print(constants.h)
```

### Nuances / gotchas
- These are **numbers** (floats), not functions.
- SciPy provides many constants; exams often pick `c` and `h` because they’re common.

---

# Quick exam checklist
- `resample`: FFT-based, returns exactly `num` samples
- `find_peaks`: returns indices + properties dict; `prominence` is key parameter
- `butter`: watch `Wn` meaning (normalized vs `fs=` in Hz)
- `detrend`: removes linear trend (`type='linear'` default)
- `curve_fit`: returns `popt`, `pcov`; model signature `f(x, *params)`
- `fsolve`: root finding, depends on initial guess `x0`
- `odeint`: derivative signature `func(y, t)` and output shape `(len(t), len(y0))`
- `linregress`: returns slope/intercept/rvalue/pvalue/stderr
- `interp1d`: callable interpolator; `fill_value='extrapolate'` extrapolates
- `det`: determinant of square matrix
- `fftfreq`: frequency bins include negatives; resolution `1/(n*d)`
- constants `c`, `h`: numeric physical constants
