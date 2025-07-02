

````markdown
# 🐍 Python Setup on macOS with VS Code

This guide walks you through setting up Python and VS Code on a Mac.

---

## ✅ Step 1: Install Python on macOS

### 🔸 Check if Python is pre-installed
Open Terminal and run:
```bash
python3 --version
````

> If installed, it will show the version like `Python 3.11.x`.

---

### 🔸 Install Python via Homebrew (Recommended)

1. Install [Homebrew](https://brew.sh/) (if not already installed):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install Python:

```bash
brew install python
```

3. Verify installation:

```bash
python3 --version
pip3 --version
```

---

## ✅ Step 2: Install VS Code

1. Download from: [https://code.visualstudio.com/](https://code.visualstudio.com/)

2. Install and launch the app.

---

## ✅ Step 3: Install Python Extension for VS Code

1. Open VS Code
2. Go to Extensions (`⇧ + ⌘ + X`)
3. Search: `Python`
4. Click **Install** on the one from Microsoft

---

## ✅ Step 4: Set Python Interpreter in VS Code

1. Press `⌘ + ⇧ + P` to open Command Palette
2. Search: `Python: Select Interpreter`
3. Choose the version you installed (`Python 3.x` from `/usr/local/bin` or similar)

---

## ✅ Step 5: Run Python Code in VS Code

1. Create a new file with `.py` extension
2. Write some code:

```python
print("Hello, Python on Mac!")
```

3. Click the green play button `▶️` at the top-right
   OR press `⌃ + ⌥ + N` (after installing **Code Runner extension**)

---

## ✅ Optional: Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

> This helps manage dependencies for each project separately.

---

## ✅ Optional: Install Useful Python Tools

```bash
pip install black pylint autopep8
```

You can configure these in VS Code for formatting and linting.

---

## 🧠 Tips

* Use `⌘ + ~` to open Terminal inside VS Code
* Add `"python.pythonPath"` in `.vscode/settings.json` to fix interpreter issues
* Restart VS Code if any changes don’t reflect

---

Happy Coding 🧑‍💻

```

```
