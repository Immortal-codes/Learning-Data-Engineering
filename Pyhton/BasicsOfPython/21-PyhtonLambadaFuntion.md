# ✅ Python – Lambda Functions (Short FAANG Notes)

---

## 🔹 Lambda Syntax

```python
lambda args: expression
```

```python
square = lambda x: x * x
print(square(5))  # 25
```

---

## 🔹 When to Use?

| Use Case               | Reason                            |
|------------------------|-----------------------------------|
| One-liner functions    | Less boilerplate                  |
| With `map()`, `filter()` | Transform/filter collections     |
| With `reduce()`        | Aggregate values                  |
| With `sorted()`        | Custom sort logic                 |

---

## 🔹 Basic Examples

```python
add = lambda a, b: a + b
is_even = lambda x: x % 2 == 0
```

---

## 🔹 With `map()`

```python
nums = [1, 2, 3]
squares = list(map(lambda x: x*x, nums))  # [1, 4, 9]
```

---

## 🔹 With `filter()`

```python
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2]
```

---

## 🔹 With `reduce()`

```python
from functools import reduce
product = reduce(lambda x, y: x*y, [1, 2, 3])  # 6
```

---

## 🔹 With `sorted()`

```python
students = [("Raj", 24), ("Sim", 20)]
sorted(students, key=lambda x: x[1])
```

---

## 🔹 Return Lambda (Closure)

```python
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
print(double(5))  # 10
```

---

## 🔹 Nested Lambda (Rare)

```python
print((lambda x: (lambda y: x + y))(2)(3))  # 5
```

---

## 🔹 Lambda vs def

| Feature    | `lambda`           | `def`            |
|------------|--------------------|------------------|
| Named      | No                 | Yes              |
| Multi-line | ❌ No              | ✅ Yes            |
| Return     | Implicit           | Explicit          |
| Use        | Simple 1-liners    | Full logic        |

---

## 🔹 Avoid Lambda When:

- Logic needs multiple lines  
- Code readability is important  
- You want meaningful function names  

---

# 🔚 End of Lambda Notes
