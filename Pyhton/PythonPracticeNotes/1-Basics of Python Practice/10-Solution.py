# 🧪 Python Type Casting – Practice Solutions

# ------------ 📌 int() – Practice Problems ------------

# 1. Convert user input (string) to integer and add 5 to it.
num = input("Enter a number: ")
num_int = int(num)
print("After adding 5:", num_int + 5)

# 2. Add two string numbers
a = "15"
b = "25"
sum_ab = int(a) + int(b)
print("Sum of strings:", sum_ab)

# 3. Convert float to int and show before and after
f = 9.99
print("Original float:", f)
print("After int():", int(f))

# 4. Parse string "007" to int and print types
code = "007"
print("Before:", code, type(code))
code_int = int(code)
print("After:", code_int, type(code_int))

# 5. Convert invalid string to int with error handling
try:
    val = int("hello")
except ValueError:
    print("Cannot convert 'hello' to int!")

# ------------ 📌 float() – Practice Problems ------------

# 1. Average of two string inputs
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Average:", (x + y) / 2)

# 2. Convert and multiply int and str to float
a = 3
b = "4.5"
result = float(a) * float(b)
print("Multiplication:", result)

# 3. Read string "5.0", convert, add 2.5
val = "5.0"
val_f = float(val)
print("Result:", val_f + 2.5)

# 4. Handle error for converting invalid string to float
try:
    float("abc")
except ValueError:
    print("Cannot convert 'abc' to float!")

# 5. Function that returns float result
def always_float(n):
    return float(n)

print("Float from int 10:", always_float(10))
print("Float from float 3.3:", always_float(3.3))

# ------------ 📌 str() – Practice Problems ------------

# 1. Integer to string in message
age = 22
print("You are " + str(age) + " years old.")

# 2. Boolean to string
print("String True:", str(True))
print("String False:", str(False))

# 3. Concatenate string and number
score = 99
print("Score: " + str(score))

# 4. Greeting using str()
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + str(age) + " years old.")

# 5. Convert float to string and find length
pi = 3.14159
pi_str = str(pi)
print("Length of string:", len(pi_str))
