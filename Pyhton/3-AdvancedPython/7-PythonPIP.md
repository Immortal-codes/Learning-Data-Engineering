# 📦 Python PIP – FAANG-Ready Notes

---

## 🔹 What is PIP?

- **PIP** = Package Installer for Python
- Used to **install**, **upgrade**, and **manage** Python packages (libraries/modules).
- Comes pre-installed with **Python 3.4+**

---

## 📦 What is a Package?

- A **package** = Collection of Python modules with metadata.
- Found on **[PyPI](https://pypi.org)** – Python Package Index.

---

## ✅ Check if PIP is Installed

```bash
pip --version
# or
python -m pip --version
```

---

## ⬇️ Install a Package

```bash
pip install package-name

# Example
pip install camelcase
```

---

## 🧪 Use an Installed Package

```python
import camelcase

c = camelcase.CamelCase()
print(c.hump("hello world"))  # ➜ Hello World
```

---

## ❌ Uninstall a Package

```bash
pip uninstall package-name

# Example
pip uninstall camelcase
```

---

## 📋 List All Installed Packages

```bash
pip list
```

📘 Sample Output:

```
Package         Version
--------------- -------
camelcase       0.2
pip             24.0
setuptools      65.5.0
```

---

## 🔄 Upgrade a Package

```bash
pip install --upgrade package-name

# Example
pip install --upgrade camelcase
```

---

## 🔍 Search & Find Packages

Browse or search packages: [https://pypi.org](https://pypi.org)

---

## 🗑️ Remove Cached Files (Optional Clean-Up)

```bash
pip cache purge
```

---

## 💡 Tip for Virtual Environments (Recommended)

```bash
# Create a virtual env
python -m venv env

# Activate (Windows)
env\Scripts\activate

# Activate (macOS/Linux)
source env/bin/activate
```

---

## 📦 Export/Import Requirements (for sharing dependencies)

```bash
# Save installed packages to a file
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt
```

---

> ⚠️ Always use a virtual environment for each project to avoid dependency conflicts.
