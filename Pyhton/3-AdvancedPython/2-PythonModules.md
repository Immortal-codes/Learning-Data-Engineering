# 📦 Python Modules – Complete Notes

---

## 🧠 What is a Module?

- A **module** is like a **code library**.
- It's a **`.py` file** that contains functions, variables, and classes you want to reuse in other programs.

---

## 🛠️ Create a Module

Create a file named **`mymodule.py`**:

```python
# mymodule.py
def greeting(name):
    print("Hello, " + name)
```

---

## 🔗 Use a Module

Import and use it in another Python file:

```python
import mymodule

mymodule.greeting("Jonathan")
```

> ✅ Syntax: `module_name.function_name()`

---

## 📦 Variables in Module

You can also define variables like dictionaries, lists, etc. in modules.

### Example (in `mymodule.py`):

```python
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
```

### Access from another file:

```python
import mymodule

print(mymodule.person1["age"])  # Output: 36
```

---

## 🏷️ Naming a Module

- You can name your module **anything**, but it **must end in `.py`**

---

## 🧾 Renaming a Module (Alias)

Use the `as` keyword to create an alias:

```python
import mymodule as mx

print(mx.person1["age"])  # Output: 36
```

---

## ⚙️ Built-in Modules

Python includes **built-in modules** that you can import anytime.

### Example:

```python
import platform

print(platform.system())  # Output: Windows/Linux/Mac
```

---

## 🔍 Using `dir()` Function

Use `dir()` to list all **functions/variables** in a module:

```python
import platform

print(dir(platform))
```

> ✅ Works on both built-in and user-defined modules

---

## 📥 Import Specific Items from Module

Use `from module import item` to import only what you need.

### Example:

```python
# mymodule.py
def greeting(name):
    print("Hello, " + name)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
```

```python
# main.py
from mymodule import person1

print(person1["age"])  # Output: 36
```

> ⚠️ Don’t use `module_name.` when you import using `from`.

---

## 🧾 Summary Table

| Task                      | Syntax Example                            |
|---------------------------|--------------------------------------------|
| Import module             | `import mymodule`                          |
| Use function              | `mymodule.function()`                      |
| Use alias                 | `import mymodule as mx`                    |
| Import specific item      | `from mymodule import person1`            |
| List module contents      | `dir(mymodule)`                            |
| Built-in module usage     | `import platform; platform.system()`       |

---

> 💡 Best Practice: Keep your helper functions, constants, and configs in separate modules for clean and maintainable code.

