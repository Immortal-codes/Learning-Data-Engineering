# 🔄 Python JSON – Complete Notes

---

## 📌 What is JSON?

- **JSON (JavaScript Object Notation)** is a text format for **storing and exchanging data**.
- Python has a built-in module called `json` for working with JSON.

---

## 🔁 Convert JSON ➡️ Python

```python
import json

# JSON string
x = '{ "name":"John", "age":30, "city":"New York"}'

# Parse JSON ➜ Python dict
y = json.loads(x)
print(y["age"])  # ➜ 30
```

---

## 🔁 Convert Python ➡️ JSON

```python
import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y)  # ➜ '{"name": "John", "age": 30, "city": "New York"}'
```

---

## ✅ Supported Python ➡️ JSON Types

| Python         | JSON         |
|----------------|--------------|
| `dict`         | object       |
| `list`, `tuple`| array        |
| `str`          | string       |
| `int`, `float` | number       |
| `True`         | true         |
| `False`        | false        |
| `None`         | null         |

---

## 🔁 Example: All Types

```python
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
```

---

## 🎨 Formatting JSON Output

### 🧱 Indentation

```python
json.dumps(x, indent=4)
```

### ✂️ Custom Separators

```python
json.dumps(x, indent=4, separators=(". ", " = "))
```

### 🔤 Sorted Keys

```python
json.dumps(x, indent=4, sort_keys=True)
```

---

## 📥 JSON Encoding Examples

```python
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
```

---

## 🧾 Summary Table

| Operation                  | Method         |
|---------------------------|----------------|
| JSON ➜ Python             | `json.loads()` |
| Python ➜ JSON             | `json.dumps()` |
| Pretty Print JSON         | `indent=4`     |
| Custom separators         | `separators=()`|
| Sorted keys in JSON       | `sort_keys=True`|

---

> 💡 Tip: Always validate external JSON before parsing. Wrap `json.loads()` in `try/except` for production-grade code.

