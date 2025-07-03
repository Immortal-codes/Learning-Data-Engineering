# 🧠 Python Classes and Objects

---

## 🧰 Python is an Object-Oriented Programming Language

- Almost **everything in Python is an object**, with **properties** and **methods**.
- A **Class** is like an **object constructor** or a **"blueprint"** for creating objects.

---

## 🧱 Create a Class

Use the keyword `class` to create a class.

```python
class MyClass:
    x = 5
```

---

## 🧪 Create an Object

Now we can use the class `MyClass` to create an object:

```python
p1 = MyClass()
print(p1.x)
```

🧾 Output:
```
5
```

---

## ⚙️ The `__init__()` Function

- All classes have a function called `__init__()`.
- It is **automatically executed** when the class is being **initiated** (i.e., when creating an object).
- It is used to **assign values to object properties** or perform **any setup steps**.

---

### 🧑‍💻 Example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)  # John
print(p1.age)   # 36
```

📝 **Note:**  
The `__init__()` function runs **automatically** every time the class is used to create a new object.

---

## ✅ Summary

- `class` → used to define a blueprint
- `object` → instance created from the blueprint
- `__init__()` → special method that runs during object creation
- `self` → refers to the current object instance

---

