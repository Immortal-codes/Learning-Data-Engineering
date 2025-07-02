

### ✅ Python List - Cheat Sheet for Interviews (🔥 Crisp + Practical)

#### 🔹 1. **What is a List?**

* Dynamic array (can grow/shrink)
* Mutable ✅
* Indexed ✅
* Allows duplicates ✅
* Can hold different datatypes ✅

```python
lst = [1, "hello", 3.14, [5,6], True]
```

---

#### 🔹 2. **Accessing Elements**

```python
lst[0]         # First element
lst[-1]        # Last element
lst[1:4]       # Slicing
```

---

#### 🔹 3. **Basic Operations**

```python
len(lst)            # Length
lst + [7, 8]        # Concatenation
lst * 2             # Repetition
3 in lst            # Membership check
```

---

#### 🔹 4. **Modifying Lists**

```python
lst.append(99)           # Add at end
lst.insert(1, "new")     # Insert at index
lst.extend([100, 101])   # Add multiple

lst[0] = "changed"       # Direct update
```

---

#### 🔹 5. **Deleting Items**

```python
lst.remove(99)      # Remove by value (first occurrence)
lst.pop()           # Remove last element
lst.pop(1)          # Remove at index
del lst[2]          # Delete by index
lst.clear()         # Empty the list
```

---

#### 🔹 6. **Useful Methods**

```python
lst.index("hello")     # First index of item
lst.count(3.14)        # Count of item
lst.sort()             # In-place sort
lst.reverse()          # Reverse list
lst.copy()             # Shallow copy
```

---

#### 🔹 7. **Looping**

```python
for item in lst: print(item)
for i in range(len(lst)): print(lst[i])
```

---

#### 🔹 8. **List Comprehension (🔥 Must Know)**

```python
[x*x for x in range(5)]             # Squares
[x for x in range(10) if x%2 == 0]  # Evens
```

---

#### 🔹 9. **Nested Lists**

```python
matrix = [[1,2], [3,4]]
print(matrix[0][1])  # 2
```

---

#### 🔹 10. **Copying Lists**

```python
new = lst[:]         # Slice copy
new = lst.copy()     # copy()
```

❗ Don’t use `new = lst`, it creates a reference, not a copy.

---

### 🚫 Common Mistakes

| Mistake                          | Why it’s Wrong               |
| -------------------------------- | ---------------------------- |
| `lst1 = lst2`                    | Both point to same memory    |
| `lst.remove(x)` but x not in lst | Raises ValueError            |
| `lst.sort()` on mixed types      | Raises TypeError in Python 3 |

---

### 🎯 When to Use List vs Other Collections?

| Use Case                | Go With             |
| ----------------------- | ------------------- |
| Indexing / Ordered Data | `list`              |
| Unique items only       | `set`               |
| Key-value pairs         | `dict`              |
| FIFO Queue              | `collections.deque` |

---

If this format works for you, I’ll prepare **Set**, **Tuple**, **Dict**, etc. in this same crisp FAANG-style. 💪

Batao bhai, ab waale notes pasand aaye? Or chaahta hai `.md` file banake doon ready to download?


