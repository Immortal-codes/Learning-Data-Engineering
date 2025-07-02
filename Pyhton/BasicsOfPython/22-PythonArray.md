

* Python built-in lists vs `array.array()`
* Array creation, operations, methods
* Access, slice, update, loop
* Time complexity and usage
* Real-world and interview-level notes

---

````markdown
# ✅ Python Arrays – Complete Notes (FAANG-Level)

---

## 🔹 What is an Array in Python?

➡ Python **doesn't have built-in arrays** like C/C++  
➡ Use either:

1. **`list`** – more flexible (heterogeneous, dynamic) ✅
2. **`array` module** – type-specific arrays (like C-style) 🔥

---

## 🔹 Difference: List vs Array

| Feature         | `list`                        | `array.array()`                |
|------------------|-------------------------------|-------------------------------|
| Type Restriction | Can store **mixed types**     | Only **one data type**        |
| Import Needed?   | ❌ No                         | ✅ Yes (`from array import array`) |
| Memory Efficient?| ❌ Less                      | ✅ More                        |
| Speed            | Slower for large data         | Faster for numeric data       |

---

## 🔹 Importing and Creating an Array

```python
from array import array

a = array('i', [1, 2, 3, 4])  # 'i' means integer
````

✅ Common type codes:

* `'i'` → int
* `'f'` → float
* `'u'` → unicode character

---

## 🔹 Accessing and Updating Elements

```python
print(a[0])      # 1
a[1] = 10
print(a)         # array('i', [1, 10, 3, 4])
```

✅ Similar to list indexing.

---

## 🔹 Slicing an Array

```python
print(a[1:3])    # array('i', [10, 3])
```

✅ Supports slicing like lists.

---

## 🔹 Looping Through an Array

```python
for x in a:
    print(x)
```

---

## 🔹 Useful Array Methods

| Method              | Use                                   |
| ------------------- | ------------------------------------- |
| `.append(x)`        | Add element at end                    |
| `.insert(i, x)`     | Insert at position `i`                |
| `.pop()`            | Remove last element                   |
| `.remove(x)`        | Remove first occurrence of `x`        |
| `.index(x)`         | Get index of value `x`                |
| `.reverse()`        | Reverse in-place                      |
| `.buffer_info()`    | Memory address and number of elements |
| `.typecode`         | Returns type code                     |
| `.extend(iterable)` | Add multiple items                    |

---

### 🔸 Example:

```python
a = array('i', [1, 2, 3])
a.append(4)
a.insert(1, 10)
a.remove(2)
a.reverse()
print(a)  # array('i', [4, 3, 10, 1])
```

---

## 🔹 Converting Array to List and Vice Versa

```python
a = array('i', [1, 2, 3])
lst = a.tolist()               # array → list

arr2 = array('i', lst)         # list → array
```

---

## 🔹 Time Complexity (Same as List)

| Operation | Time Complexity  |
| --------- | ---------------- |
| Access    | O(1)             |
| Insert    | O(n)             |
| Delete    | O(n)             |
| Append    | O(1) (Amortized) |

---

## 🔹 Use-Cases

✅ Use `array.array()` when:

* You want **numeric data only**
* You want to save memory (in comparison to list)
* You need to interface with **C/C++ extensions** or binary files

✅ Use `list` when:

* You need **heterogeneous** data
* You want more flexibility (strings, nested structures, etc.)

---

## 🔹 Example – Sum of All Elements

```python
from array import array
a = array('i', [1, 2, 3, 4])
total = sum(a)
print(total)  # 10
```

---

## 🔹 How to Search in Array?

```python
if 3 in a:
    print("Found at", a.index(3))
else:
    print("Not Found")
```

---

## 🔹 Limitations of `array.array`

* Only supports primitive types (int, float, char, etc.)
* For 2D arrays → use `list of lists` or NumPy
* Not widely used in practice unless you're doing **low-level optimizations**

---

## 🔹 Interview Tip

In most FAANG-level Python rounds:

* You will **use lists** instead of `array.array`
* But understanding `array` module is still useful for **low-level optimizations**

---

# 🔚 End of Python Array Notes

```

---


```
