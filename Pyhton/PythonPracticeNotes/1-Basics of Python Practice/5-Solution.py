# ---------------------------------------------
# 🔹 Part 1: What are Variables?
# ---------------------------------------------

# ✅ Problem 1: Assign and print name
name = "Rajan Sharma"
print("Problem 1:", name)

# ✅ Problem 2: Sum of two variables
a = 10
b = 5
print("Problem 2: Sum =", a + b)

# ✅ Problem 3: Float value
pi = 3.14159
print("Problem 3: Value of pi =", pi)

# ✅ Problem 4: City and country in one line
city = "Moradabad"
country = "India"
print("Problem 4:", city + ", " + country)

# ✅ Problem 5: Print age message
age = 24
print("Problem 5: I am", age, "years old.")

# ---------------------------------------------
# 🔹 Part 2: Variable Names & Rules
# ---------------------------------------------

# ✅ Problem 1: Different valid variable styles
x = 5
age = 24
_balance = 1000
print("Problem 6:", x, age, _balance)

# ✅ Problem 2: Case-sensitivity
name = "Rajan"
Name = "Sharma"
print("Problem 7:", name)   # Output: Rajan
print("Problem 7:", Name)   # Output: Sharma

# ✅ Problem 3: Invalid variable (commented to avoid error)
# 2name = "invalid"  # ❌ SyntaxError: invalid syntax
name2 = "valid"      # ✅ Valid alternative
print("Problem 8:", name2)

# ✅ Problem 4: Invalid variable names
# List of invalid names with reason
# 1. 2var = 10          → Starts with number ❌
# 2. for = "loop"       → Python keyword ❌
# 3. my-name = "Rajan"  → Hyphen not allowed ❌
# 4. class = 5          → Python keyword ❌
# 5. @data = 100        → Special characters ❌

# ✅ Problem 5: Testing Python keywords as variable names
# The following will throw errors if uncommented:
# is = 1
# for = 2
# True = 3
# while = 4
# Use valid alternative:
is_valid = True
loop_count = 3
print("Problem 10:", is_valid, loop_count)

# ---------------------------------------------
# 🔹 Part 3: Multi-Word Variable Names
# ---------------------------------------------

# ✅ Problem 1: Camel case
studentAge = 21
print("Problem 11:", studentAge)

# ✅ Problem 2: Pascal case
StudentName = "Rajan Sharma"
print("Problem 12:", StudentName)

# ✅ Problem 3: Snake case
student_grade = "A"
print("Problem 13:", student_grade)

# ✅ Problem 4: All three styles in one
camelCaseVar = "Camel"
PascalCaseVar = "Pascal"
snake_case_var = "Snake"
print("Problem 14:", camelCaseVar, PascalCaseVar, snake_case_var)

# ✅ Problem 5: Refactor snake_case to camelCase
# Original:
student_marks = 95
student_subject = "Math"

# Refactored:
studentMarks = 95
studentSubject = "Math"
print("Problem 15:", studentMarks, studentSubject)
