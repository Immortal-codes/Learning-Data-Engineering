# 🐍 Python Virtual Environment – Complete Notes

---

## ✅ What is a Virtual Environment?

A **virtual environment** is an **isolated Python environment** for a specific project.

### Why use it?

- Separate dependencies for each project
- Prevents version conflicts
- Keeps global Python installation clean
- Enables testing with different Python versions

Each virtual env has:
- Its **own Python interpreter**
- Its **own `pip` & site-packages**
- Full **isolation**

---

## 🔧 Create a Virtual Environment

> Python has a built-in module called `venv`.

### 📌 Syntax:

```bash
python -m venv myenv
```

### Example:

```bash
C:\Users\YourName> python -m venv myfirstproject
```

This creates:

```
myfirstproject/
│
├── Include/
├── Lib/
├── Scripts/ (Windows) or bin/ (macOS/Linux)
├── pyvenv.cfg
```

---

## ▶️ Activate the Virtual Environment

### ✅ Windows:

```bash
myfirstproject\Scripts\activate
```

### ✅ macOS/Linux:

```bash
source myfirstproject/bin/activate
```

> Terminal changes:  
`(myfirstproject) C:\Users\YourName>`

---

## 📦 Install Packages Inside Venv

```bash
pip install cowsay
```

Example Output:

```bash
Successfully installed cowsay-6.1
```

📌 Note: Installed only inside the virtual environment.

---

## 🧪 Test the Environment with a Python File

### Step 1: Create a file `test.py` outside the env folder:

```python
import cowsay
cowsay.cow("Good Mooooorning!")
```

### Step 2: Run inside the environment:

```bash
(myfirstproject) C:\Users\YourName> python test.py
```

🧾 Output:

```
  _________________
< Good Mooooorning! >
  =================
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
```

---

## 🚫 Deactivate the Virtual Environment

```bash
deactivate
```

Terminal reverts to normal:

```bash
C:\Users\YourName>
```

> 🛑 Now if you run `python test.py`, you'll get:

```text
ModuleNotFoundError: No module named 'cowsay'
```

Because `cowsay` was installed **only in the virtual environment**.

---

## 🧹 Delete a Virtual Environment

### ❌ To delete the virtual environment folder:

#### 🪟 Windows:

```bash
rmdir /s /q myfirstproject
```

#### 🍎 macOS/Linux:

```bash
rm -rf myfirstproject
```

---

## 🧠 Recap

| Task                  | Command                                |
|-----------------------|-----------------------------------------|
| Create Venv           | `python -m venv myenv`                 |
| Activate (Windows)    | `myenv\Scripts\activate`               |
| Activate (Linux/mac)  | `source myenv/bin/activate`            |
| Deactivate            | `deactivate`                           |
| Install Packages      | `pip install <package>`                |
| Delete Venv           | `rmdir /s /q myenv` (or `rm -rf myenv`) |

---

> ✅ Always create a virtual environment per project — clean, safe, reproducible setup.

