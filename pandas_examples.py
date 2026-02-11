"""
Runnable examples for Pandas exam methods.
Run: python pandas_examples.py

This script creates a small sample CSV file locally.
"""

import pandas as pd

# Create a semicolon-separated CSV with an id column and a date column
csv_text = (
    "id;date;col;value;price;name
"
    "1;2026-02-01;A;10;120;Alpha
"
    "2;2026-02-02;A;20;80;Beta
"
    "3;2026-02-03;B;30;;Gamma
"
    "4;2026-02-04;B;40;200;Delta
"
)
with open("file.csv", "w", encoding="utf-8") as f:
    f.write(csv_text)

# 1) read_csv with sep, index_col, parse_dates
df = pd.read_csv("file.csv", sep=";", index_col="id", parse_dates=["date"])
print("df head:
", df.head())
print("
dtypes:
", df.dtypes)

# 5) info()
print("
info():")
df.info()

# 6) dropna
clean_any = df.dropna(how="any")
clean_all = df.dropna(how="all")
print("
dropna how='any' rows:", len(clean_any), "from", len(df))
print("dropna how='all' rows:", len(clean_all), "from", len(df))

# 2) groupby mean (numeric_only=True avoids string issues)
gb = df.groupby("col").mean(numeric_only=True)
print("
groupby mean:
", gb)

# 3) corr
corr = df.corr(method="pearson", numeric_only=True)
print("
corr:
", corr)

# 4) describe
print("
describe(include='all'):
", df.describe(include="all"))

# 7) loc
expensive = df.loc[df["price"] > 100, ["name", "price"]]
print("
loc boolean filter (price>100):
", expensive)

# 8) iloc
subset = df.iloc[0:2, 0:3]
print("
iloc [0:2,0:3]:
", subset)
