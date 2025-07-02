# ✅ Python – Functions (FAANG-Level Short Notes)

---

## 🔹 Function Basics

```python
def greet():
    print("Hello, Rajan!")

def add(a, b):
    return a + b
```

---

## 🔹 Default & Keyword Args

```python
def greet(name="Guest"):
    print("Hello", name)

def show(name, role):
    print(f"{name} is a {role}")

show(role="SDE", name="Rajan")
```

---

## 🔹 Variable-Length Args

```python
def total(*args): print(sum(args))           # Positional
def info(**kwargs): print(kwargs)            # Keyword
```

✅ `*args` = tuple, `**kwargs` = dict

---

## 🔹 Return Multiple Values

```python
def calc(a, b): return a+b, a*b
s, p = calc(2, 3)
```

---

## 🔹 Lambda Functions

```python
square = lambda x: x*x
print(square(4))
```

---

## 🔹 Scope – local, global, nonlocal

```python
x = 10
def change(): global x; x = 5
change(); print(x)
```

---

## 🔹 Recursion

```python
def fact(n):
    if n == 0: return 1
    return n * fact(n-1)
```

---

## 🔹 Docstrings

```python
def greet(name):
    """Greets the user"""
    print("Hello", name)

print(greet.__doc__)
```

---

## 🔹 Nested & First-Class Functions

```python
def outer():
    def inner():
        print("Inner")
    inner()

def shout(text): return text.upper()
def call(func): return func("hi")
```

---

## 🔹 Returning Functions (Closure)

```python
def outer(x):
    def inner(y): return x + y
    return inner

add5 = outer(5)
print(add5(2))  # 7
```

---

## 🔹 Decorators (Intro)

```python
def deco(func):
    def wrapper():
        print("Before"); func(); print("After")
    return wrapper

@deco
def hello(): print("Hello Rajan")
```

---

## 🔹 Real Use Case – Frequency Map

```python
from collections import defaultdict
def freq(s):
    d = defaultdict(int)
    for ch in s: d[ch] += 1
    return d
```

---

## 🔹 Summary Table

| Concept           | Syntax / Use              |
|-------------------|---------------------------|
| Function          | `def fn():`               |
| Default Arg       | `def fn(x=0):`            |
| `*args`           | Positional (tuple)        |
| `**kwargs`        | Keyword (dict)            |
| Lambda            | `lambda x: x*x`           |
| Return Multiple   | `return a, b`             |
| Recursion         | `fn(n-1)`                 |
| Nested Function   | `def inner()`             |
| Closure           | `return inner`            |
| Decorator         | `@deco`                   |

---

# 🔚 End of Python Functions Notes
