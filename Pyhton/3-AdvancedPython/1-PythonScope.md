# 🧭 Python Scope – Full Notes

---

## 📌 What is Scope?

A variable is only available **inside the region** where it is created.  
This region is called the **scope**.

---

## 🧪 Local Scope

- A variable created **inside a function** is **local** to that function.
- It can **only be used inside** that function.

```python
def myfunc():
    x = 300
    print(x)

myfunc()
```

---

## 🔁 Function Inside Function (Nested)

- Local variables are also accessible to **inner functions**.

```python
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()
```

---

## 🌍 Global Scope

- A variable created **outside** any function is **global**.
- It can be accessed **inside any function**.

```python
x = 300

def myfunc():
    print(x)

myfunc()
print(x)
```

---

## ⚠️ Same Variable Name (Local vs Global)

If a variable with the **same name** exists **inside and outside** a function, Python treats them as **separate variables**.

```python
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()
print(x)
```

🧾 Output:
```
200
300
```

---

## 🔑 The `global` Keyword

Use the `global` keyword to:
- Create a **global variable** inside a function
- **Modify** a global variable from within a function

### ✅ Create a global variable from local scope:

```python
def myfunc():
    global x
    x = 300

myfunc()
print(x)  # Output: 300
```

### ✅ Modify global variable from inside function:

```python
x = 300

def myfunc():
    global x
    x = 200

myfunc()
print(x)  # Output: 200
```

---

## 🔁 The `nonlocal` Keyword

- Used inside **nested functions**
- Allows modification of variable from **outer (non-global) scope**

### ✅ Example:

```python
def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())  # Output: hello
```

---

## 🧾 Summary Table

| Keyword     | Scope        | Purpose                                       |
|-------------|--------------|-----------------------------------------------|
| `local`     | Inside func  | Default scope inside a function               |
| `global`    | Everywhere   | Create/modify global variable inside function |
| `nonlocal`  | Nested func  | Modify outer function variable                |

---

> 💡 Tip: Avoid using too many global variables in large codebases — use function parameters and return values for better control.

