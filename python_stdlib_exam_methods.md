# Python (Native & Standard Library) — Exam Methods Cheat Sheet

This file gives **method signatures**, **syntax breakdown**, **concrete examples**, and **nuances/gotchas** for the methods you listed.

---

## 1) `zip()`

### What it does
Combines elements from multiple iterables **index-by-index** into tuples.

### Signature
```py
zip(*iterables) -> iterator[tuple]
```
- Takes any number of iterables.
- Returns a **zip object** (an iterator) producing tuples.

### Your exam syntax
```py
list(zip(list1, list2))
```

### Syntax breakdown
- `zip(list1, list2)` creates an **iterator** of pairs: `(list1[i], list2[i])`
- `list(...)` materializes it into a list of tuples

### Concrete example
```py
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
pairs = list(zip(list1, list2))
print(pairs)  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

### Nuances / gotchas
- **Stops at the shortest iterable**:
  ```py
  list(zip([1,2,3], ["a","b"]))  # [(1,'a'), (2,'b')]
  ```
- The result is an **iterator**: once you consume it, it’s “used up”.
- To “unzip”:
  ```py
  pairs = [(1,'a'), (2,'b')]
  nums, letters = zip(*pairs)
  # nums -> (1,2), letters -> ('a','b')
  ```

---

## 2) `open()`

### What it does
Opens a file and returns a file object (a stream) for reading/writing bytes or text.

### Signature (simplified)
```py
open(file, mode="r", encoding=None, newline=None, ...) -> TextIO | BufferedIO
```

### Your exam syntax
```py
open("filename.txt", "r")
```

### Syntax breakdown
- `"filename.txt"`: path (relative or absolute)
- `"r"`: **mode** (read text)
- In text modes, encoding matters; in binary modes, you read/write `bytes`.

### Concrete example (recommended: context manager)
```py
# Read text
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)
```

### Common modes (exam-relevant)
- `"r"`: read text (file **must exist**)
- `"w"`: write text (creates file or **truncates** existing file)
- `"a"`: append text (creates file if missing; writes at end)
- `"rb"`: read **binary** (returns bytes, good for images, audio, etc.)

### Quick demo of `w` vs `a`
```py
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("First line\n")   # overwrites file each run

with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Another line\n") # adds to the end
```

### Nuances / gotchas
- Prefer `with open(...) as f:` so the file always closes.
- `"w"` is destructive (it truncates).
- `"rb"`/`"wb"` deals with bytes; don’t pass `encoding=` in binary mode.

---

## 3) `input()`

### What it does
Reads a line from standard input and returns it as a **string**.

### Signature
```py
input(prompt: str = "") -> str
```

### Your exam syntax
```py
float(input("Enter value: "))
```

### Syntax breakdown
- `input("Enter value: ")` prints a prompt and returns user text like `"3.14"`
- `float(...)` converts that string to a float **before math**

### Concrete example
```py
x = float(input("Enter value: "))
y = float(input("Enter another: "))
print(x + y)
```

### Nuances / gotchas
- `input()` always returns `str`. For math you must cast:
  - `int(input(...))` for integers
  - `float(input(...))` for decimals
- Invalid input raises `ValueError`:
  ```py
  float("abc")  # ValueError
  ```

---

## 4) String concatenation (`+`)

### What it does
Joins strings to make a new string.

### “Signature” / operator behavior
```py
str + str -> str
```
(Concatenating with non-strings raises `TypeError` unless you convert.)

### Your exam syntax
```py
"Hello" + " " + "World"
# or
var1 + var2
```

### Concrete example
```py
first = "Johnny"
last = "Doe"
full = first + " " + last
print(full)  # Johnny Doe
```

### Nuances / gotchas
- Can’t do `"Age: " + 20` (TypeError). Fix:
  ```py
  "Age: " + str(20)
  ```
- For many parts, f-strings are usually cleaner:
  ```py
  age = 20
  s = f"Age: {age}"
  ```

---

## 5) `print()` with f-strings

### What it does
Prints text to standard output; f-strings format values inline.

### Signature (print)
```py
print(*objects, sep=" ", end="\n") -> None
```

### Your exam syntax
```py
print(f"Result is {value:.3f}")
```

### Syntax breakdown
- `f"..."` means “format string”
- `{value:.3f}` means:
  - `value` is inserted
  - `:.3f` formats as a float with **3 digits after the decimal**

### Concrete example
```py
value = 3.1415926
print(f"Result is {value:.3f}")  # Result is 3.142
```

### Nuances / gotchas
- Rounds (does not truncate): `3.141 -> 3.141`, `3.14159 -> 3.142`
- Works for padding/alignment too:
  ```py
  n = 7
  print(f"{n:03d}")  # 007
  ```

---

## 6) List removal — `del`

### What it does
Deletes an item (or slice) by **index/position**.

### “Signature” (statement)
```py
del L[index]
del L[start:stop:step]
```

### Your exam syntax
```py
del L[index]
```

### Concrete example
```py
L = [10, 20, 30, 40]
del L[1]
print(L)  # [10, 30, 40]
```

### Nuances / gotchas
- `del` is a statement, so it **returns nothing**.
- If index is out of range -> `IndexError`.
- You can delete slices:
  ```py
  L = [1,2,3,4,5]
  del L[1:4]   # removes 2,3,4
  # L -> [1,5]
  ```

---

## 7) List removal — `remove()`

### What it does
Removes the **first occurrence** of a value.

### Signature
```py
list.remove(value) -> None
```

### Your exam syntax
```py
L.remove(value)
```

### Concrete example
```py
L = [1, 2, 2, 3]
L.remove(2)
print(L)  # [1, 2, 3]
```

### Nuances / gotchas
- If value not found -> `ValueError`
- Does **not** return the removed item.
- Only removes the **first** match (not all).

---

## 8) List removal — `pop()`

### What it does
Removes and **returns** an item at an index (default: last).

### Signature
```py
list.pop(index: int = -1) -> Any
```

### Your exam syntax
```py
L.pop(index)   # default index is -1
```

### Concrete example
```py
L = ["a", "b", "c"]
last = L.pop()
print(last)  # c
print(L)     # ['a', 'b']

first = L.pop(0)
print(first) # a
print(L)     # ['b']
```

### Nuances / gotchas
- Out of range index -> `IndexError`
- Great when you need the removed value (unlike `del`/`remove`).

---

## 9) List comprehension (filtering)

### What it does
Creates a **new list** by filtering and/or transforming items.

### Pattern / “signature”
```py
[new_item for item in iterable if condition]
```

### Your exam syntax (remove all occurrences)
```py
[x for x in L if x != value]
```

### Concrete example (remove all 2s)
```py
L = [1, 2, 2, 3, 2, 4]
value = 2
filtered = [x for x in L if x != value]
print(filtered)  # [1, 3, 4]
```

### Nuances / gotchas
- This does **not mutate** the original list unless you reassign:
  ```py
  L = [x for x in L if x != value]
  ```
- Best for “remove all matches” safely and clearly.

---

# Mini practice: pick the right tool
- Remove by **position**: `del L[i]` or `L.pop(i)` (use `pop` if you need the value)
- Remove by **value once**: `L.remove(v)`
- Remove **all** occurrences: `[x for x in L if x != v]`
- Pair lists index-by-index: `list(zip(a, b))`
- Read numeric input: `float(input(...))` / `int(input(...))`
- Print formatted decimals: `print(f"{x:.3f}")`
