"""
Runnable examples for the exam methods.
Run: python_examples.py
"""

# 1) zip()
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
print("zip ->", list(zip(list1, list2)))

# 2) open() - create then read
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello file!\nSecond line.\n")

with open("example.txt", "r", encoding="utf-8") as f:
    print("open/read ->", f.read())

# 3) input() - commented out to keep file runnable without waiting for input
# x = float(input("Enter value: "))
# print("input ->", x)

# 4) concatenation
first, last = "Johnny", "Doe"
print("concat ->", first + " " + last)

# 5) print f-strings
value = 3.1415926
print(f"f-string -> Result is {value:.3f}")

# 6) del
L = [10, 20, 30, 40]
del L[1]
print("del ->", L)

# 7) remove
L = [1, 2, 2, 3]
L.remove(2)
print("remove ->", L)

# 8) pop
L = ["a", "b", "c"]
print("pop() returns ->", L.pop())
print("after pop ->", L)

# 9) list comprehension filtering
L = [1, 2, 2, 3, 2, 4]
value = 2
filtered = [x for x in L if x != value]
print("filter ->", filtered)
