# Pandas — Exam Methods Cheat Sheet (import pandas as pd)

This file gives **method signatures**, **syntax breakdown**, **concrete examples**, and **nuances/gotchas** for the Pandas methods you listed.

---

## 1) `pd.read_csv`

### What it does
Reads a CSV (or delimited text) file into a `DataFrame`.

### Signature (common)
```py
pd.read_csv(
    filepath_or_buffer,
    sep=',',
    delimiter=None,
    index_col=None,
    parse_dates=None,
    dtype=None,
    na_values=None,
    ...
) -> pd.DataFrame
```

### Your exam syntax
```py
pd.read_csv('file.csv', sep=';', index_col='id', parse_dates=['date'])
```

### Syntax breakdown
- `sep=';'`: delimiter is semicolon (common in Europe)
- `index_col='id'`: use column `id` as the DataFrame index
- `parse_dates=['date']`: parse column(s) into datetime dtype

### Concrete example
```py
import pandas as pd

df = pd.read_csv("file.csv", sep=";", index_col="id", parse_dates=["date"])
print(df.head())
print(df.dtypes)
```

### Nuances / gotchas (exam traps)
- “Distractor” parameters:
  - `date_parser` is deprecated in many contexts (don’t use unless explicitly required).
  - There is no standard `id_column` parameter (the correct one is `index_col`).
- `sep` vs `delimiter`: both exist, but typically you use **one**. If both are set, it can confuse readers/exams.
- If the file uses comma as decimal separator:
  ```py
  pd.read_csv(..., decimal=",")
  ```

---

## 2) `df.groupby`

### What it does
Splits data into groups by key(s) and allows aggregation (mean, sum, count, etc.).

### Signature (common)
```py
df.groupby(by=None, axis=0, as_index=True, sort=True, dropna=True) -> DataFrameGroupBy
```

### Your exam syntax
```py
df.groupby('col').mean(numeric_only=True)
```

### Syntax breakdown
- `'col'`: the grouping key column
- `.mean(...)`: aggregation function
- `numeric_only=True`: tells Pandas to ignore non-numeric columns when computing mean

### Concrete example
```py
g = df.groupby("col").mean(numeric_only=True)
print(g)
```

### Nuances / gotchas
- Without `numeric_only=True`, you can get errors when string columns are present.
- Common variations:
  ```py
  df.groupby("col")["value"].mean()
  df.groupby(["col1", "col2"]).sum(numeric_only=True)
  df.groupby("col").agg({"value":"mean", "price":"max"})
  ```
- `as_index=False` keeps the group key as a normal column instead of index:
  ```py
  df.groupby("col", as_index=False).mean(numeric_only=True)
  ```

---

## 3) `df.corr`

### What it does
Computes pairwise correlation of columns.

### Signature (common)
```py
df.corr(method='pearson', numeric_only=False) -> pd.DataFrame
```

### Your exam syntax
```py
df.corr(method='pearson', numeric_only=True)
```

### Syntax breakdown
- `method='pearson'`: default, linear correlation
- `numeric_only=True`: ignore non-numeric columns

### Concrete example
```py
corr_pearson = df.corr(method="pearson", numeric_only=True)
corr_spearman = df.corr(method="spearman", numeric_only=True)
print(corr_pearson)
```

### Nuances / gotchas
- Methods you must know:
  - `'pearson'`: linear relationship
  - `'spearman'`: rank-based (monotonic), less sensitive to outliers / non-linear monotonic
  - `'kendall'`: rank-based, often for small samples
- Missing values are handled pairwise (rows with NaN in either column are excluded for that pair).

---

## 4) `df.describe`

### What it does
Generates descriptive statistics (for numeric: count, mean, std, min, quartiles, max; for categorical: count, unique, top, freq).

### Signature (common)
```py
df.describe(percentiles=None, include=None, exclude=None) -> pd.DataFrame
```

### Your exam syntax
```py
df.describe(include='all')
# or
df.describe(include=['number'])
```

### Concrete example
```py
print(df.describe(include="all"))
print(df.describe(include=["number"]))
```

### Nuances / gotchas
- `include="all"` forces categorical summary too (count/unique/top/freq).
- If you only want specific types, use `include=[...]` or `exclude=[...]`.

---

## 5) `df.info()`

### What it does
Prints a concise summary: column names, non-null counts, dtypes, memory usage.

### Signature (common)
```py
df.info(verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=True) -> None
```

### Your exam syntax
```py
df.info()
```

### Concrete example
```py
df.info()
```

### Nuances / gotchas
- It **prints** info; it doesn’t return a DataFrame.
- Super useful for quickly spotting missing values via `Non-Null Count`.

---

## 6) `df.dropna`

### What it does
Drops rows (or columns) containing missing values (`NaN`, `None`).

### Signature (common)
```py
df.dropna(axis=0, how='any', subset=None, inplace=False) -> pd.DataFrame | None
```

### Your exam syntax
```py
df.dropna(how='any')
```

### Syntax breakdown
- `how='any'`: drop row if **any** value is missing
- `how='all'`: drop row only if **all** values are missing

### Concrete example
```py
clean_any = df.dropna(how="any")
clean_all = df.dropna(how="all")
```

### Nuances / gotchas
- Use `subset=[...]` to consider missingness only in certain columns:
  ```py
  df.dropna(subset=["price", "value"])
  ```
- `inplace=True` mutates and returns `None` (common confusion):
  ```py
  df.dropna(inplace=True)  # df changes, return is None
  ```

---

## 7) `df.loc[...]`

### What it does
Label-based selection (rows/cols by labels), and boolean filtering.

### Pattern
```py
df.loc[row_label, col_label]
df.loc[boolean_mask, col_label_list]
```

### Your exam syntax
```py
df.loc[row_label, col_label]
# or
df.loc[boolean_mask]
```

### Key exam point
Label slicing is **inclusive** on the endpoint.

### Concrete example
```py
# single value by label
price = df.loc[3, "price"]

# boolean filtering + column selection
filtered = df.loc[df["price"] > 100, ["name", "price"]]
print(filtered)
```

### Nuances / gotchas
- `.loc` uses **index labels**, not integer positions (unless your index labels are integers).
- If your index is dates, this becomes very powerful:
  ```py
  df.loc["2026-02-01":"2026-02-10"]  # inclusive if those labels exist
  ```

---

## 8) `df.iloc[...]`

### What it does
Integer-position based selection (0-based), like Python slicing.

### Pattern
```py
df.iloc[row_idx, col_idx]
df.iloc[row_start:row_stop, col_start:col_stop]
```

### Key exam point
Slicing is **exclusive** of the endpoint.

### Concrete example
```py
# first two rows, first three columns (by position)
subset = df.iloc[0:2, 0:3]
print(subset)

# single cell by position
cell = df.iloc[1, 2]
print(cell)
```

### Nuances / gotchas
- `.iloc` ignores index labels entirely; it’s pure positional.
- Endpoint excluded:
  ```py
  df.iloc[0:3]  # rows 0,1,2
  ```

---

# Quick exam checklist
- `read_csv`: `sep`, `index_col`, `parse_dates`
- `groupby`: use `numeric_only=True` when mean/sum meets strings
- `corr`: methods = pearson/spearman/kendall, often `numeric_only=True`
- `describe`: `include='all'` summarizes categorical too
- `info()`: prints dtypes + non-null counts
- `dropna`: how='any' vs how='all'
- `.loc`: labels, inclusive slice
- `.iloc`: positions, exclusive slice
