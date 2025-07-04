# 🔍 Python RegEx – FAANG-Level Notes

---

## 📌 What is RegEx?

- **RegEx (Regular Expression)** = Pattern to **search/match text**.
- Used for validation, extraction, or replacing strings.
- Python’s `re` module provides RegEx support.

```python
import re
```

---

## 🔧 Basic Pattern Match

```python
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)  # Starts with 'The' and ends with 'Spain'
```

---

## ⚙️ Core RegEx Functions

| Function     | Description                          |
|--------------|--------------------------------------|
| `findall()`  | Returns all matches as list          |
| `search()`   | Returns the **first match** object   |
| `split()`    | Splits string by pattern             |
| `sub()`      | Replace match with another string    |

---

## ✅ Common Examples

```python
# Find all occurrences
re.findall("ai", txt)

# Search first whitespace
re.search("\s", txt).start()

# Split on whitespace
re.split("\s", txt)

# Replace whitespace with '9'
re.sub("\s", "9", txt)
```

---

## 🧬 Metacharacters

| Pattern | Meaning                         |
|---------|----------------------------------|
| `[]`    | Set of characters `[a-z]`       |
| `.`     | Any character except newline     |
| `^`     | Starts with `^hello`            |
| `$`     | Ends with `planet$`             |
| `*`     | 0 or more occurrences            |
| `+`     | 1 or more                        |
| `?`     | 0 or 1                           |
| `{}`    | Exactly N `{2}`, or `{2,4}`     |
| `|`     | Either or `this|that`           |
| `()`    | Group                           |

---

## 🧩 Special Sequences

| Pattern | Meaning                                |
|---------|----------------------------------------|
| `\A`    | Start of string                        |
| `\Z`    | End of string                          |
| `\b`    | Word boundary                          |
| `\B`    | Not word boundary                      |
| `\d`    | Digit (0–9)                            |
| `\D`    | Not digit                              |
| `\s`    | Whitespace                             |
| `\S`    | Not whitespace                         |
| `\w`    | Word char (a-z, A-Z, 0-9, _)           |
| `\W`    | Not word char                          |

> ⚠ Always use raw string for patterns: `r"\bword\b"`

---

## 🏁 Flags

```python
re.IGNORECASE  # re.I → Case-insensitive
re.MULTILINE   # re.M → ^/$ match start/end of line
re.DOTALL      # re.S → '.' matches newline too
re.VERBOSE     # re.X → allow multiline regex with comments
```

---

## 🎯 Match Object Methods

```python
x = re.search(r"\bS\w+", "The rain in Spain")

print(x.span())   # ➜ (12, 17)
print(x.string)   # ➜ The rain in Spain
print(x.group())  # ➜ Spain
```

---

## 🧪 Sample Use-Cases

```python
# Validate Email
re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", "john@example.com")

# Extract numbers
re.findall(r"\d+", "Item 1 costs 100 and item 2 costs 250")

# Replace digits
re.sub(r"\d+", "#", "123 apples and 456 bananas")
```

---

## 🧾 Summary

| Use Case               | Function     |
|------------------------|--------------|
| Match start-to-end     | `^...$`       |
| Find all matches       | `findall()`   |
| First match object     | `search()`    |
| Replace pattern        | `sub()`       |
| Split by pattern       | `split()`     |
| Get match info         | `group(), span()` |

---

> 💡 Tip: Use [regex101.com](https://regex101.com) for live testing and explanation.

