# 🗑️ Python File & Folder Deletion – `os` Module

---

## 📦 Step 1: Import OS Module

```python
import os
```

---

## ❌ Delete a File

```python
os.remove("demofile.txt")
```

> ⚠️ Will raise `FileNotFoundError` if file doesn't exist.

---

## ✅ Check Before Deleting File

```python
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
```

---

## 📁 Delete a Folder (Only If Empty)

```python
os.rmdir("myfolder")
```

> ⚠️ `os.rmdir()` only works for **empty folders**.

---

## 🔐 Want to delete **non-empty folders**?

Use:
```python
import shutil
shutil.rmtree("foldername")
```

> ⚠️ Be careful: this **permanently deletes** the entire folder with all files/subfolders.

---

## 🔄 Summary Table

| Operation        | Function             | Notes                     |
|------------------|----------------------|---------------------------|
| Delete File       | `os.remove()`        | File must exist           |
| Delete Empty Dir  | `os.rmdir()`         | Folder must be empty      |
| Delete Full Dir   | `shutil.rmtree()`    | Deletes everything inside |

---

Let me know if you want examples of creating, renaming, or reading directories next 📁👨🏻‍💻
