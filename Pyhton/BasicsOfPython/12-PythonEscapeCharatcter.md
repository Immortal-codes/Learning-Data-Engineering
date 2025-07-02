Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:


Example
The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."


Escape Character List

# 🔍 Python Escape Characters

Escape characters are used to insert characters that are illegal in a string. They are prefixed with a backslash `\`.

| Escape Character | Description                  | Example                            | Output                   |
|------------------|------------------------------|------------------------------------|--------------------------|
| `\\`             | Backslash                    | `print("C:\\\\User")`              | `C:\User`                |
| `\'`             | Single Quote                 | `print('It\\'s good')`             | `It's good`              |
| `\"`             | Double Quote                 | `print("He said \\\"Hi\\\"")`      | `He said "Hi"`           |
| `\n`             | New Line                     | `print("Hello\\nWorld")`           | `Hello` <br> `World`     |
| `\t`             | Tab                          | `print("Hello\\tWorld")`           | `Hello   World`          |
| `\r`             | Carriage Return              | `print("123\\rABC")`               | `ABC` (overwrites `123`) |
| `\b`             | Backspace                    | `print("Helloo\\b")`               | `Hello`                  |
| `\f`             | Form Feed                    | `print("Hello\\fWorld")`           | `Hello` (form feed) `World` |
| `\a`             | Bell (Alert)                 | `print("\\a")`                     | System beep (if enabled) |
| `\v`             | Vertical Tab                 | `print("Hello\\vWorld")`           | Vertical tabbed text     |
| `\ooo`           | Octal Value                  | `print("\\101")`                   | `A`                      |
| `\xhh`           | Hex Value                    | `print("\\x41")`                   | `A`                      |

---

## ✅ Example: Using Escape Characters
Escape characters are used to insert characters that are illegal in a string. They are prefixed with a backslash `\`.

| Escape Character | Description                  | Example                            | Output                   |
|------------------|------------------------------|------------------------------------|--------------------------|
| `\\`             | Backslash                    | `print("C:\\\\User")`              | `C:\User`                |
| `\'`             | Single Quote                 | `print('It\\'s good')`             | `It's good`              |
| `\"`             | Double Quote                 | `print("He said \\\"Hi\\\"")`      | `He said "Hi"`           |
| `\n`             | New Line                     | `print("Hello\\nWorld")`           | `Hello` <br> `World`     |
| `\t`             | Tab                          | `print("Hello\\tWorld")`           | `Hello   World`          |
| `\r`             | Carriage Return              | `print("123\\rABC")`               | `ABC` (overwrites `123`) |
| `\b`             | Backspace                    | `print("Helloo\\b")`               | `Hello`                  |
| `\f`             | Form Feed                    | `print("Hello\\fWorld")`           | `Hello` (form feed) `World` |
| `\a`             | Bell (Alert)                 | `print("\\a")`                     | System beep (if enabled) |
| `\v`             | Vertical Tab                 | `print("Hello\\vWorld")`           | Vertical tabbed text     |
| `\ooo`           | Octal Value                  | `print("\\101")`                   | `A`                      |
| `\xhh`           | Hex Value                    | `print("\\x41")`                   | `A`                      |

print("Name:\tAlice\nCity:\tDelhi")
