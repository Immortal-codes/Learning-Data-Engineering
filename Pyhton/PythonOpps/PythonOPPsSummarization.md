# 🧠 Python OOPs – Complete Notes (FAANG-Level)

---

## 📌 What is OOP?

- OOP = **Object-Oriented Programming**
- A way to structure code using **classes** and **objects**
- Helps in **code reusability**, **modularity**, **readability**, and **scalability**

---

## ✅ Advantages of OOP

- Provides a **clear structure** to programs
- Keeps code **DRY** (Don't Repeat Yourself)
- Makes code easy to **debug**, **maintain**, and **extend**
- Promotes **real-world modeling** (e.g., Student, BankAccount, Employee)

---

## 🧱 OOP Core Concepts (4 Pillars)

| Pillar          | Meaning                                                                 |
|------------------|-------------------------------------------------------------------------|
| **Encapsulation** | Bind data and methods inside a class                                   |
| **Abstraction**   | Hide complex logic and expose only essentials                          |
| **Inheritance**   | Reuse properties/methods of another class                              |
| **Polymorphism**  | Same method behaves differently across classes                         |

---

## 🧰 Class & Object in Python

```python
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)  # Output: 5
```

---

## ⚙️ `__init__()` Constructor

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
```

> Called automatically when object is created

---

## 🧑‍🔧 Object Methods

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

p = Person("Rajan")
p.greet()
```

---

## 🔒 Encapsulation

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0   # Private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(1000)
print(acc.get_balance())  # 1000
```

---

## 🧰 Abstraction with ABC

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()
```

---

## 👨‍👧 Inheritance

```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

s = Student("Mike", "Olsen")
s.printname()
```

---

## 🧠 Method Overriding + super()

```python
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Person:", self.name)

class Student(Person):
    def show(self):
        print("Student:", self.name)

s = Student("Rajan")
s.show()  # Student: Rajan
```

---

## 🔁 Polymorphism

### 1. Function Polymorphism

```python
print(len("Rajan"))  # String
print(len([1, 2, 3]))  # List
```

### 2. Class Polymorphism

```python
class Car:
    def move(self):
        print("Drive")

class Boat:
    def move(self):
        print("Sail")

for vehicle in (Car(), Boat()):
    vehicle.move()
```

---

### 3. Inheritance Polymorphism

```python
class Vehicle:
    def move(self):
        print("Move")

class Plane(Vehicle):
    def move(self):
        print("Fly")

v = Vehicle()
p = Plane()

for obj in (v, p):
    obj.move()
```

---

## 🔄 Custom Iterator using `__iter__()` & `__next__()`

```python
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

obj = MyNumbers()
it = iter(obj)

for num in it:
    print(num)
```

---

## 🧨 Destructor – `__del__()`

```python
class Demo:
    def __del__(self):
        print("Object destroyed")

d = Demo()
del d
```

---

## 📚 Summary Table

| Concept          | Keyword/Usage       | Purpose                          |
|------------------|---------------------|----------------------------------|
| Class            | `class`             | Blueprint for object             |
| Object           | `obj = Class()`     | Instance of a class              |
| Constructor      | `__init__()`        | Initialization                   |
| Destructor       | `__del__()`         | Clean-up                         |
| Encapsulation    | Private var/methods | Data protection                  |
| Inheritance      | `class A(B)`        | Reuse from base class            |
| Polymorphism     | `method overriding` | Method behaves differently       |
| Abstraction      | `ABC` module        | Hide unnecessary implementation  |
| Iterator         | `__iter__`, `__next__` | Custom iteration logic        |

---

> 🔥 Pro Tip:
> Real-world projects often use OOP heavily for modeling users, products, services, permissions, and more.

---

## 🧪 OOP Practice Ideas

- Model a **Library System** (Books, Members, Borrow)
- Build **Student Management** with Inheritance
- Create a **Banking App** with encapsulation and abstraction
- Design an **Inventory System** using polymorphism

