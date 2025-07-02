# ✅ Python – Dictionary (Full FAANG-Level Notes)

---

## 🔹 What is a Dictionary?

A **dictionary** is a built-in data type that stores **key-value pairs**.

- **Unordered (until Python 3.6) → Ordered (from 3.7+)**
- **Mutable**
- Keys must be **unique** and **hashable**
- Values can be of any type

```python
user = {
    "name": "Rajan",
    "role": "SDE",
    "age": 24
}
```

---

## 🔹 Creating Dictionaries

```python
d1 = {"a": 1, "b": 2}
d2 = dict(a=1, b=2)
d3 = dict([("a", 1), ("b", 2)])
d4 = {}               # empty dict
```

---

## 🔹 Accessing Values

```python
print(user["name"])        # Rajan
print(user.get("age"))     # 24
print(user.get("city", "N/A"))  # N/A (default value)
```

📌 Use `.get()` to avoid KeyError

---

## 🔹 Modifying Dictionary

```python
user["age"] = 25
user["email"] = "rajan@example.com"
```

✅ Add/update using assignment.

---

## 🔹 Removing Items

```python
user.pop("age")                 # Removes 'age' and returns its value
user.popitem()                  # Removes last inserted pair
del user["role"]                # Deletes key 'role'
user.clear()                    # Removes everything
```

---

## 🔹 Dictionary Methods – Quick Table

| Method              | Description                           |
| ------------------- | ------------------------------------- |
| `get(key, default)` | Safe value access                     |
| `keys()`            | Returns all keys                      |
| `values()`          | Returns all values                    |
| `items()`           | Returns all key-value pairs as tuples |
| `update()`          | Adds/updates from another dict        |
| `pop(key)`          | Removes key and returns value         |
| `popitem()`         | Removes last inserted item            |
| `clear()`           | Empties the dictionary                |
| `setdefault(k, v)`  | Adds key if missing                   |
| `copy()`            | Returns shallow copy                  |

---

## 🔹 Looping Over Dictionary

```python
for key in user:
    print(key, user[key])

for k, v in user.items():
    print(f"{k} → {v}")
```

✅ `.items()` is the most common and cleanest for looping.

---

## 🔹 Dictionary Comprehension (🔥 Pythonic)

```python
squares = {x: x*x for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

✅ You can also use conditions:

```python
even_squares = {x: x*x for x in range(10) if x % 2 == 0}
```

---

## 🔹 Nesting Dictionaries

```python
employees = {
    "emp1": {"name": "Rajan", "role": "SDE"},
    "emp2": {"name": "Simran", "role": "PM"}
}
print(employees["emp1"]["name"])  # Rajan
```

📌 Useful in real-world APIs, JSON handling.

---

## 🔹 Check Key Existence

```python
if "email" in user:
    print("Email is present")
```

✅ Fast and clean key presence check

---

## 🔹 Merge Dictionaries (Python 3.9+)

```python
d1 = {"a": 1}
d2 = {"b": 2}

d3 = d1 | d2  # New merged dictionary
```

📌 Use `d1 |= d2` for in-place merge

---

## 🔹 Real-World Use Cases (🔥)

| Use Case                    | Example                            |
| --------------------------- | ---------------------------------- |
| JSON parsing                | `dict = json.loads(response.text)` |
| Frequency count             | `freq[x] = freq.get(x, 0) + 1`     |
| Lookup tables (fast access) | e.g., `{user_id: user_obj}`        |
| Grouping items              | `defaultdict(list)`                |
| Caching results             | memoization in recursion           |

---

## 🔹 Dictionary vs List – Comparison

| Feature     | Dictionary            | List                   |
| ----------- | --------------------- | ---------------------- |
| Access      | Key-based (fast)      | Index-based            |
| Order       | Ordered (from 3.7+)   | Ordered                |
| Use Case    | Lookups, mapping data | Sequential collections |
| Performance | O(1) for key access   | O(n) for search        |

---

## 🔹 Interview Trick: Frequency Count (Most Common Use)

```python
arr = [1, 2, 2, 3, 1, 1]

freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)  # {1: 3, 2: 2, 3: 1}
```

📌 Must-know pattern for FAANG string/array problems.

---

## 📌 Summary

| Property       | Dictionary                                              |
| -------------- | ------------------------------------------------------- |
| Type           | Mutable, unordered (3.6−), ordered (3.7+)               |
| Key Type       | Must be hashable                                        |
| Value Type     | Any                                                     |
| Common Methods | `get()`, `pop()`, `update()`, `items()`, `setdefault()` |
| Comprehension  | ✅ Yes                                                   |
| Nested         | ✅ Yes                                                   |

---

# 🔚 End of Python Dictionary Notes
