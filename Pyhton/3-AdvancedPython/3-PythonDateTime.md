# ⏰ Python `datetime` Module – Full Notes

---

## 📌 What is `datetime` in Python?

- Python does **not have a built-in `date` data type**
- Use the **`datetime` module** to work with **dates and times**
- Dates are represented using **`datetime` objects**

---

## 🔽 Import and Get Current Date & Time

```python
import datetime

x = datetime.datetime.now()
print(x)
```

> ✅ Output:
> `2025-07-03 19:12:00.512207`  
> (Includes year, month, day, hour, minute, second, microsecond)

---

## 🔍 Accessing Parts of a Date

```python
import datetime

x = datetime.datetime.now()

print(x.year)         # Year => 2025
print(x.strftime("%A"))  # Weekday name => Thursday
```

---

## 🏗️ Creating a Custom Date Object

```python
import datetime

x = datetime.datetime(2020, 5, 17)
print(x)
```

> You can also provide optional values like hour, minute, second, etc.

```python
datetime.datetime(2020, 5, 17, 10, 30)
```

---

## 🎨 Formatting Dates using `strftime()`

- `strftime()` = **String format time**
- Converts a datetime object to a **readable string**
- Accepts a format string to define the output

### Example: Display full month name

```python
import datetime

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))  # Output: June
```

---

## 🧾 Common Format Examples

| Code  | Meaning             |
|-------|----------------------|
| `%Y`  | Full year (e.g. 2025) |
| `%m`  | Month (01–12)        |
| `%d`  | Day (01–31)          |
| `%H`  | Hour (00–23)         |
| `%M`  | Minute (00–59)       |
| `%S`  | Second (00–59)       |
| `%A`  | Weekday name         |
| `%B`  | Month name           |

---

## 🧾 Summary

| Task                      | Code                                     |
|---------------------------|------------------------------------------|
| Import `datetime`         | `import datetime`                        |
| Current date & time       | `datetime.datetime.now()`                |
| Create custom date        | `datetime.datetime(2023, 12, 31)`        |
| Format date string        | `date.strftime("%A")`                    |

---

> 💡 Tip: Use `strftime()` when you want to **present** a date nicely to the user, and `datetime()` for **logic/comparisons**.

