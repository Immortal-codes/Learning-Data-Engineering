# 🔁 Python Iterators

---

## 📌 What is an Iterator?

- An **iterator** is an object that contains a **countable number of values**.
- It can be **iterated upon** — meaning you can **traverse through all the values** one by one.

> ✅ In Python, an **iterator** is an object that implements the **iterator protocol**.

---

## ⚙️ Iterator Protocol

To be an iterator, an object must implement:

- `__iter__()` → Returns the iterator object itself
- `__next__()` → Returns the **next value** from the iterator

---

## 🔄 Iterator vs Iterable

| Term       | Meaning |
|------------|---------|
| **Iterable** | Objects like list, tuple, dict, set, str that can return an iterator |
| **Iterator** | Object with `__iter__()` and `__next__()` methods |

---

## 🧪 Example: Tuple Iterator

```python
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))  # apple
print(next(myit))  # banana
print(next(myit))  # cherry
```

---

## 🧪 Example: String Iterator

Even **strings are iterable** — they return one character at a time:

```python
mystr = "banana"
myit = iter(mystr)

print(next(myit))  # b
print(next(myit))  # a
print(next(myit))  # n
print(next(myit))  # a
print(next(myit))  # n
print(next(myit))  # a
```

---

## 🔁 Looping Through an Iterator

You can use a `for` loop to iterate over any iterable:

### ✅ Tuple Example

```python
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)
```

### ✅ String Example

```python
mystr = "banana"

for x in mystr:
    print(x)
```

> 💡 Behind the scenes, the `for` loop:
> - Creates an **iterator object** using `iter()`
> - Then calls `next()` on it until it raises `StopIteration`

---

## 🧾 Summary

- All iterables can return an iterator using `iter()`
- Iterator objects give values one-by-one using `next()`
- `for` loop is a simplified way to use iterators
- Custom objects can be made iterable using `__iter__()` and `__next__()`

---

> 🔥 Next Up:  
> - Creating Custom Iterators  
> - Using `StopIteration`  
> - Difference between Generators vs Iterators


# 🔨 Create a Custom Iterator in Python

---

## 🧰 How to Create an Iterator?

To make your own iterator:

- Define a **class**
- Implement:
  - `__iter__()` → returns the iterator object itself
  - `__next__()` → returns the **next value** in the sequence

---

## 📌 Reminder

All classes have a constructor `__init__()` used for **initialization**.

- Similarly, `__iter__()` is used to **prepare the iterator**
- `__next__()` is used to **fetch the next value**

---

## 🧪 Example: Infinite Sequence Iterator

```python
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))  # 1
print(next(myiter))  # 2
print(next(myiter))  # 3
print(next(myiter))  # 4
print(next(myiter))  # 5
```

> ⚠️ This will continue **forever** unless we stop it manually using a condition.

---

## 🛑 StopIteration

- To **prevent infinite iteration**, raise `StopIteration` manually when done.

---

## ✅ Example: Stop after 20 Iterations

```python
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
```

🧾 Output:
```
1
2
3
...
20
```

---
## 🔁 Summary

| Method        | Purpose                                    |
|---------------|--------------------------------------------|
| `__iter__()`  | Returns the iterator object itself         |
| `__next__()`  | Returns the next item, or raises StopIteration |

> ✅ You can customize `__next__()` to return numbers, letters, or any sequence.

---



