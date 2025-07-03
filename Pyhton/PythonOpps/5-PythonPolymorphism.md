# 🔀 Python Polymorphism

---

## 📌 What is Polymorphism?

- **Polymorphism** means "**many forms**".
- In programming, it refers to **functions/methods/operators** with the **same name** behaving **differently** based on the object or class.

---

## 🔧 Function Polymorphism

Python built-in functions often show polymorphism.

### ✅ Example: `len()` function works on different datatypes

#### 🔹 String
```python
x = "Hello World!"
print(len(x))  # Output: 12
```

#### 🔹 Tuple
```python
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))  # Output: 3
```

#### 🔹 Dictionary
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))  # Output: 3
```

---

## 🧱 Class Polymorphism

- Different classes can have **methods with the same name**.
- This allows for a **common interface** across unrelated classes.

### ✅ Example:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

# Using polymorphism
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()
```

🧾 Output:
```
Drive!
Sail!
Fly!
```

---

## 👪 Inheritance + Polymorphism

Polymorphism also works with **inheritance** when child classes **override methods** from the parent class.

### ✅ Example:

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
```

🧾 Output:
```
Ford
Mustang
Move!
Ibiza
Touring 20
Sail!
Boeing
747
Fly!
```

---

## ✅ Summary

| Concept            | Meaning                                                                 |
|--------------------|-------------------------------------------------------------------------|
| Function Polymorphism | Same function (`len()`) works on different types                      |
| Class Polymorphism    | Different classes have methods with the same name                     |
| Inheritance-based     | Child classes override methods from parent class                      |

> 💡 Thanks to polymorphism, we can write cleaner and more extensible code — the same method name can be reused across classes!

---

> 🔥 Coming Up Next:  
> - Operator Overloading in Python  
> - Method Overloading (with default args)  
> - Practical OOP-based Project Use-Cases

