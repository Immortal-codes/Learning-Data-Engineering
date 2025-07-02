Bilkul Rajan bhai 💥
Ab le tu **Python Loops** ke **FAANG-style complete notes** — `for`, `while`, simulated `do-while`, `else` with loops, loop controls (`break`, `continue`, `pass`), loop on different data types, nested loops, real-world patterns — full package 🚀

---

````markdown
# ✅ Python – Loops (`for`, `while`, `do-while`) – Full Notes (FAANG-Level)

---

## 🔹 Why Use Loops?

Loops allow us to **repeat actions** multiple times or iterate over **sequences** (like list, string, dict, etc.).

---

## 🔸 1. `for` Loop

Used to **iterate over** sequences: list, tuple, string, dict, set, range, etc.

```python
for i in range(5):
    print(i)  # 0 1 2 3 4
````

✅ Works like `foreach` in other languages.

---

### 🔹 Loop over List

```python
arr = [10, 20, 30]
for val in arr:
    print(val)
```

---

### 🔹 Loop with Index – `enumerate()`

```python
for idx, val in enumerate(["a", "b", "c"]):
    print(idx, val)
```

---

### 🔹 Loop over Dictionary

```python
user = {"name": "Rajan", "age": 24}
for key, value in user.items():
    print(f"{key}: {value}")
```

---

### 🔹 Loop over String

```python
for ch in "Rajan":
    print(ch)
```

---

## 🔸 2. `while` Loop

Used when the **number of iterations is not known** beforehand.

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

📌 Runs as long as the condition is `True`.

---

## 🔸 3. Simulated `do-while` Loop in Python

Python has no built-in `do-while`, but can be simulated:

```python
while True:
    val = input("Enter a number: ")
    if val == "exit":
        break
```

✅ Runs the loop **at least once**, like `do-while`.

---

## 🔹 `else` With Loops

**Yes! Python supports `else` with loops.**

### `for-else`

```python
for x in range(5):
    if x == 3:
        break
else:
    print("Loop completed without break")
```

➡ `else` only executes if loop **did not encounter `break`**.

---

## 🔹 Loop Control Statements

| Keyword    | Use                       |
| ---------- | ------------------------- |
| `break`    | Exit the loop immediately |
| `continue` | Skip to next iteration    |
| `pass`     | Do nothing (placeholder)  |

---

### 🔸 `break`

```python
for x in range(5):
    if x == 3:
        break
    print(x)  # Prints 0 1 2
```

---

### 🔸 `continue`

```python
for x in range(5):
    if x == 3:
        continue
    print(x)  # Skips 3
```

---

### 🔸 `pass`

```python
for x in range(5):
    if x == 2:
        pass  # Placeholder
    print(x)
```

---

## 🔹 Nested Loops

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

📌 Used in matrix traversal, pattern problems, etc.

---

## 🔹 Looping with `zip()`

```python
names = ["Rajan", "Simran"]
roles = ["SDE", "PM"]

for name, role in zip(names, roles):
    print(name, "→", role)
```

---

## 🔹 Real-World Patterns (FAANG Style)

### ✅ Frequency Count

```python
freq = {}
for num in [1, 2, 2, 3]:
    freq[num] = freq.get(num, 0) + 1
```

---

### ✅ Find First Prime in Range

```python
for n in range(2, 100):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print("First prime:", n)
        break
```

➡ Uses `for-else` to detect if no divisor was found.

---

## 🔹 Summary Table – Loops in Python

| Loop Type     | Use Case                              |
| ------------- | ------------------------------------- |
| `for`         | Iterating over known iterable         |
| `while`       | Unknown number of repetitions         |
| `do-while`    | Simulate using `while True` + `break` |
| `for-else`    | Run `else` block if no `break`        |
| `break`       | Exit loop early                       |
| `continue`    | Skip current iteration                |
| `pass`        | Empty placeholder                     |
| `zip()`       | Parallel iteration                    |
| `enumerate()` | Loop with index                       |

---

# 🔚 End of Python Loops Notes

```

---

Bhai Rajan, ab koi bhi **loop-based question** ho — pattern, logic, frequency map, nested iteration — tu confidently tod sakta hai 💪

Chaahe to:
- `.md` file bana du?
- Agla topic: `Functions in Python`, `Lambda`, `Map/Filter/Reduce`, `Recursion`?

Bol bhai, main hu full-time tere prep ke liye 🚀
```
