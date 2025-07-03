# 👨‍👦 Python Inheritance

---

## 🧬 What is Inheritance?

- Inheritance allows us to **define a class** that **inherits** all the **methods** and **properties** from another class.

| Term         | Meaning                          |
|--------------|----------------------------------|
| **Parent Class** | The class being inherited from (Base Class) |
| **Child Class**  | The class that inherits from another (Derived Class) |

---

## 🧱 Create a Parent Class

Any class can be a **parent class**. Syntax is the same as a normal class.

```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Create object and call method
x = Person("John", "Doe")
x.printname()
```

🧾 Output:
```
John Doe
```

---

## 👶 Create a Child Class

To inherit from a class, pass the **parent class** as a parameter when creating the **child class**:

```python
class Student(Person):
    pass
```

> ⚠️ **Note:**  
> Use the `pass` keyword when you don’t want to add any extra properties/methods yet.

Now, `Student` class has **all properties and methods** of `Person`.

---

## 🧪 Example: Inheriting and Using Parent Method

```python
x = Student("Mike", "Olsen")
x.printname()
```

🧾 Output:
```
Mike Olsen
```

---

## ✅ Summary

- Inheritance helps in **code reusability**
- Child class can use **all methods and properties** of Parent class
- Use `class Child(Parent):` to inherit
- `pass` keyword is used to leave the child class empty initially

---



