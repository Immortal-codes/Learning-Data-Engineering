# 🧵 Python String Formatting – Complete Notes

---

## 📌 F-Strings (Python 3.6+)

F-Strings allow inline variable formatting.

```python
txt = f"The price is 49 dollars"
print(txt)
```

---

## 🔹 Placeholders and Modifiers

```python
price = 59
txt = f"The price is {price} dollars"
print(txt)
```

Use modifiers to format values:

```python
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
```

Format directly:

```python
txt = f"The price is {95:.2f} dollars"
print(txt)
```

---

## 🔸 Math in F-Strings

```python
txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)
```

---

## ❓ Conditional (if-else) in F-Strings

```python
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)
```

---

## 🔧 Functions in F-Strings

```python
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)
```

Custom functions:

```python
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)
```

---

## ⚙️ More Modifiers

```python
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)
```

### Formatting Types

| Symbol | Description                        |
|--------|------------------------------------|
| `:<`   | Left-align                         |
| `:>`   | Right-align                        |
| `:^`   | Center-align                       |
| `:=`   | Place sign to leftmost             |
| `:+`   | Add + sign for positive numbers    |
| `:-`   | Negative sign only                 |
| `: `   | Space before positive numbers      |
| `:,`   | Comma separator                    |
| `:_`   | Underscore separator               |
| `:b`   | Binary                             |
| `:c`   | Unicode character                  |
| `:d`   | Decimal                            |
| `:e`   | Scientific (lowercase e)           |
| `:E`   | Scientific (uppercase E)           |
| `:f`   | Fixed point                        |
| `:F`   | Fixed point (uppercase INF/NAN)    |
| `:g`   | General format                     |
| `:G`   | General with uppercase             |
| `:o`   | Octal                              |
| `:x`   | Hex (lowercase)                    |
| `:X`   | Hex (uppercase)                    |
| `:n`   | Number format                      |
| `:%`   | Percentage                         |

---

## 🔙 Old Method: format()

```python
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
```

### Decimal Formatting

```python
txt = "The price is {:.2f} dollars"
print(txt.format(49))
```

---

## 🔢 Multiple Values

```python
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
```

### Index Numbers

```python
myorder = "I want {0} pieces of item {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
```

Refer same value multiple times:

```python
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
```

---

## 🏷️ Named Indexes

```python
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
```

---

> ✅ **Tip:** Always prefer **f-strings** for new code. It's faster, cleaner, and more readable.

