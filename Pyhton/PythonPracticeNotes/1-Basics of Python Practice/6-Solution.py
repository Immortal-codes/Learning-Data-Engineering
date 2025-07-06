# ---------------------------------------------
# 📤 Python Output Variables – Practice Problems
# ---------------------------------------------

# ✅ Problem 1: Print a Single Variable
msg = "Python is powerful"
print("Problem 1 Output:", msg)


# ✅ Problem 2: Concatenate Three Strings
x = "Python "
y = "is "
z = "awesome"
print("Problem 2 Output:", x + y + z)


# ✅ Problem 3: Concatenate String and Integer (With Error Fix)
age = 24
# print("I am " + age + " years old")  # ❌ This will give TypeError

# ✅ Correct Way: Convert int to str
print("Problem 3 Output:", "I am " + str(age) + " years old")


# ✅ Problem 4: Print Name and Age in One Line
name = "Rajan"
age = 24

# Option 1: Using concatenation and str()
print("Problem 4 Output:", "My name is " + name + " and I am " + str(age) + " years old.")

# Option 2: Using f-string (cleaner)
print(f"Problem 4 Output (f-string): My name is {name} and I am {age} years old.")


# ✅ Problem 5: Combine Words and Numbers (Sum Example)
a = 5
b = 3
sum_result = a + b

# Option 1: Using str()
print("Problem 5 Output:", "The sum of " + str(a) + " and " + str(b) + " is " + str(sum_result) + ".")

# Option 2: Using f-string
print(f"Problem 5 Output (f-string): The sum of {a} and {b} is {sum_result}.")
