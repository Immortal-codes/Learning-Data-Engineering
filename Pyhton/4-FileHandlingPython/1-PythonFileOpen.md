# 📁 Python File Handling – `open()` & File Modes

---

## 📌 `open()` Function

Used to **open a file** in a specific **mode**.

### 📚 Syntax:

```python
f = open("filename", "mode")
```

---

## 📂 File Modes in Python

| Mode | Description |
|------|-------------|
| `"r"` | Read (default). File must exist |
| `"a"` | Append. Creates file if not exists |
| `"w"` | Write. Overwrites or creates file |
| `"x"` | Create. Fails if file exists |
| `"t"` | Text mode (default) |
| `"b"` | Binary mode (for images, videos, etc.) |

---

## 🧪 Examples

### ✅ Open a file for reading (default):

```python
f = open("demofile.txt")
# same as: f = open("demofile.txt", "rt")
```

> ⚠️ Throws error if file does **not** exist.

---

## ✍️ Writing Modes Summary

| Mode | Behavior |
|------|----------|
| `"w"` | Overwrites content (creates if missing) |
| `"a"` | Appends to file (creates if missing) |
| `"x"` | Creates new file, errors if file exists |

---

## 🔁 Text vs Binary

| Mode | Used For |
|------|----------|
| `"t"` | Plain text (default) |
| `"b"` | Binary files like images/videos |

---

## ⚠️ Important

- Always **close the file** using `f.close()` or use `with` block.
- If file doesn't exist in `"r"` or `"x"` mode → **Error**.
- Use `"b"` mode when dealing with **non-text data** (like `image.jpg`, `video.mp4`).

---

## ✅ Example with `with` block (Auto close):

```python
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
```

---

Want to go ahead with **read, write, append, delete, file pointer operations, readlines, writelines, etc.** in the next part?

