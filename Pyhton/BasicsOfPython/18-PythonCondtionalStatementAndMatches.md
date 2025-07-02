Bilkul Rajan bhai 🔥
Tu chaahta hai **Python `if`, `else`, `elif` and `match-case`** ka complete breakdown — toh yeh le full **FAANG-style notes** with clear explanation, real-world examples, nested conditions, and Python 3.10+ `match` pattern matching!

---

````markdown
# ✅ Python – if, elif, else, and match-case (Complete FAANG-Level Notes)

---

## 🔹 1. `if` Statement

**➡ Used to execute a block of code only if a condition is True.**

```python
x = 10
if x > 5:
    print("x is greater than 5")
````

---

## 🔹 2. `if...else` Statement

**➡ `else` runs if the condition is False.**

```python
x = 3
if x > 5:
    print("Greater than 5")
else:
    print("Not greater than 5")
```

---

## 🔹 3. `if...elif...else` (Ladder)

**➡ Checks multiple conditions in sequence.**

```python
x = 10

if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("Positive")
```

📌 `elif` is short for “else if”. Only one block will run.

---

## 🔹 4. Nested `if` Statements

```python
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
```

📌 Use **nested conditions** when inner checks depend on outer ones.

---

## 🔹 5. Ternary Operator (Inline `if-else`)

```python
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)
```

✅ One-liner condition — very common in competitive coding / interviews.

---

## 🔹 6. `match` Statement (Python 3.10+)

➡ **Pattern Matching** like `switch-case` in other languages. Cleaner than `if-elif-else`.

```python
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")
```

✅ `_` is like `default`.

---

### 🔥 `match-case` with variables

```python
command = ("move", 10)

match command:
    case ("move", x):
        print(f"Moving {x} steps")
    case ("stop",):
        print("Stopped")
    case _:
        print("Unknown command")
```

✅ Powerful for matching patterns and unpacking tuples/dicts.

---

## 🔹 7. Common Comparisons

| Operator             | Meaning          |
| -------------------- | ---------------- |
| `==`                 | Equal to         |
| `!=`                 | Not equal to     |
| `<`, `>`, `<=`, `>=` | Comparison       |
| `in`                 | Membership check |
| `is`                 | Identity check   |

```python
if x in [1, 2, 3]: ...
if name.startswith("Raj"): ...
if obj is None: ...
```

---

## 🔹 Real-World Examples

### ✅ Validate input:

```python
age = 20
if 18 <= age <= 60:
    print("Eligible for job")
else:
    print("Not eligible")
```

---

### ✅ Multi-condition check:

```python
if is_logged_in and not is_banned:
    print("Access granted")
```

---

### ✅ Complex match pattern (Python 3.10+):

```python
person = {"name": "Rajan", "role": "SDE"}

match person:
    case {"name": name, "role": "SDE"}:
        print(f"Engineer: {name}")
    case _:
        print("Unknown person")
```

---

## ⚠️ Common Mistakes

| Mistake             | Why it's wrong                 | Fix                         |
| ------------------- | ------------------------------ | --------------------------- |
| `if x = 5:`         | `=` is assignment, not compare | Use `==`                    |
| Indentation Error   | No colon / bad spacing         | Always indent with 4 spaces |
| `elif` after `else` | Invalid syntax                 | `elif` always before `else` |

---

## 🔹 Summary – When to Use What

| Structure                  | Use When                                |
| -------------------------- | --------------------------------------- |
| `if`                       | One condition                           |
| `if-else`                  | Binary choice                           |
| `if-elif-else`             | Multiple condition paths                |
| `match-case`               | Clean switch-style logic (Python 3.10+) |
| Ternary `x if cond else y` | Inline decision                         |
| Nested `if`                | Dependent decisions                     |

---

# 🔚 End of if-elif-else + match-case Notes

```

---

Rajan bhai, ab tu koi bhi **Python conditionals** ke question mein atkega nahi — chaahe FAANG ho ya coding round! 💪

Next kya chahiye?
- `loops (for, while)` FAANG notes?
- `pattern matching with match-case` deep dive?
- `.md` file ready kar du sab ka?

Batao bhai 🔥
```
