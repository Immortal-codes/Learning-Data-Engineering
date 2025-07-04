# ⚠️ Python Exception Handling – FAANG-Ready Notes

---

## 🔹 Purpose of Try-Except

- Used to **handle runtime errors** gracefully.
- Prevents the program from crashing when unexpected conditions occur.

---

## ✅ Syntax

```python
try:
    # code that may raise error
except ExceptionType:
    # code to handle the error
else:
    # code that runs if no error occurs
finally:
    # always runs (optional cleanup)
```

---

## 🔸 Basic Try-Except

```python
try:
    print(x)
except:
    print("An exception occurred")
```

---

## 🔸 Without Try Block → Error

```python
print(x)  # ❌ Raises NameError, crashes
```

---

## 🔸 Handling Specific Exceptions

```python
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Some other error occurred")
```

---

## 🔸 Else Block (Runs Only If No Error)

```python
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("No errors found ✅")
```

---

## 🔸 Finally Block (Always Runs)

```python
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("This will run no matter what.")
```

📦 Use case: cleanup, closing file/db connections

---

## 🔸 Nested Try-Except-Finally

```python
try:
    f = open("file.txt")
    try:
        f.write("Hello World")
    except:
        print("Error while writing")
    finally:
        f.close()
except:
    print("Error while opening the file")
```

---

## 🔸 Raising Exceptions

Use `raise` to manually throw an error:

```python
x = -1
if x < 0:
    raise Exception("❌ No numbers below 0 allowed")
```

---

## 🔸 Raise with Specific Exception Type

```python
x = "hello"
if not isinstance(x, int):
    raise TypeError("Only integers are allowed")
```

---

## 🚨 Common Built-in Exceptions (for interviews)

| Exception       | Description                        |
|----------------|------------------------------------|
| `NameError`     | Variable not defined               |
| `TypeError`     | Wrong data type                    |
| `ValueError`    | Invalid value                      |
| `ZeroDivisionError` | Divide by zero                 |
| `IndexError`    | List index out of range            |
| `KeyError`      | Dict key not found                 |
| `FileNotFoundError` | File does not exist           |
| `ImportError`   | Module not found                   |

---

> 🧠 Pro Tip: Always catch **specific exceptions** instead of a generic `except:` block. It helps in debugging and writing safer code.
