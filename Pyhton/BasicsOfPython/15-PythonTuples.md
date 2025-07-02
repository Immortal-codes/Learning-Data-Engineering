

````markdown
# ✅ Python Tuples – FAANG-Level Notes

---

## 🔹 What is a Tuple?

A **tuple** is:
- **Immutable** (can’t change after creation)
- **Ordered** (preserves insertion order)
- **Indexed**
- Allows **duplicates**
- Can hold **mixed data types**

```python
t = (1, "hello", 3.14)
````

✅ Use when you need a **read-only collection** of items.

---

## 🔹 Why Tuple over List?

| Feature     | Tuple                        | List               |
| ----------- | ---------------------------- | ------------------ |
| Mutability  | ❌ Immutable                  | ✅ Mutable          |
| Performance | ✅ Faster (less memory)       | Slower             |
| Use Case    | Fixed data (coords, DB)      | Dynamic collection |
| Hashable    | ✅ Yes (if elements hashable) | ❌ No               |

---

## 🔹 Tuple Creation

```python
t1 = (1, 2, 3)           # Normal tuple
t2 = 1, 2, 3             # Without parentheses
t3 = (5,)                # Singleton tuple (important!)
t4 = tuple([1, 2, 3])    # From list
```

⚠️ `t = (5)` is **not** a tuple — it’s an integer.

---

## 🔹 Accessing Elements

```python
t = (10, 20, 30, 40)
print(t[0])     # 10
print(t[-1])    # 40
print(t[1:3])   # (20, 30)
```

✅ Supports indexing and slicing (just like lists).

---

## 🔹 Immutability in Action

```python
t = (1, 2, 3)
# t[0] = 10   ❌ TypeError: 'tuple' object does not support item assignment
```

---

## 🔹 Tuple Packing & Unpacking

```python
# Packing
t = 1, 2, 3

# Unpacking
a, b, c = t
print(a, b, c)  # 1 2 3
```

✅ Useful in **function return values**, **swapping**, etc.

---

## 🔹 Swapping Without Temp Var

```python
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10
```

FAANG-style tuple swap 💥

---

## 🔹 Tuple Methods

```python
t = (1, 2, 3, 2)

t.count(2)     # ➤ 2
t.index(3)     # ➤ 2
```

⚠️ Only two methods: `.count()` and `.index()`

---

## 🔹 Tuples Are Hashable

```python
t = (1, 2, 3)
s = set()
s.add(t)
print(s)  # {(1, 2, 3)}
```

✅ Can be used as **dictionary keys** or **set elements** (unlike lists).

---

## 🔹 Tuple in Dictionary Keys – Example

```python
location_data = {
    (28.61, 77.20): "Delhi",
    (19.07, 72.87): "Mumbai"
}
```

✅ Real-world FAANG use-case: key as coordinate.

---

## 🔹 Nested Tuples

```python
nested = ((1, 2), (3, 4))
print(nested[1][0])  # 3
```

---

## 🔹 Tuple vs NamedTuple (🔥 FAANG Bonus)

Use `collections.namedtuple` when:

* You want **read-only object**
* With **field names**

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")
p = Point(1, 2)
print(p.x, p.y)  # 1 2
```

✅ Readable, immutable, and memory-efficient.

---

## 📌 Summary – Tuple at a Glance

| Feature           | Description                          |
| ----------------- | ------------------------------------ |
| Immutable         | Yes                                  |
| Ordered           | Yes                                  |
| Allows Duplicates | Yes                                  |
| Indexing          | Yes                                  |
| Methods           | `count()`, `index()`                 |
| Used in           | DB rows, function returns, hash keys |
| Performance       | Faster than lists                    |

---

## 🔥 FAANG-Level Use Cases

* Coordinates: `(lat, lon)`
* RGB color: `(255, 255, 0)`
* DB row: `("Alice", "SDE", 120000)`
* Hashable key in set/dict
* Returning multiple values from a function
* Immutable configs

---

# 🔚 End of Tuple Notes

```

---


```
