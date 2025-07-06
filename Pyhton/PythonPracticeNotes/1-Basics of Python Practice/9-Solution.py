# ---------------------------------------------
# 🧠 Python Numbers – Practice Problem Solutions
# ---------------------------------------------

# ✅ Problem 1: Assign Different Number Types
a = 10           # int
b = 3.14         # float
c = 2 + 4j       # complex

print("Problem 1 Output:")
print("a =", a, "| type:", type(a))
print("b =", b, "| type:", type(b))
print("c =", c, "| type:", type(c))
print("-" * 40)


# ✅ Problem 2: Arithmetic with int and float
x = 7
y = 2.5

sum_result = x + y
diff_result = x - y
product_result = x * y

print("Problem 2 Output:")
print("Sum:", sum_result, "| type:", type(sum_result))
print("Difference:", diff_result, "| type:", type(diff_result))
print("Product:", product_result, "| type:", type(product_result))
print("-" * 40)


# ✅ Problem 3: Complex number operations
a = 3 + 2j
b = 1 - 4j

add_complex = a + b
sub_complex = a - b

print("Problem 3 Output:")
print("Addition:", add_complex, "| type:", type(add_complex))
print("Subtraction:", sub_complex, "| type:", type(sub_complex))
print("-" * 40)


# ✅ Problem 4: Type checking
x = 100
y = 45.67
z = 7j

print("Problem 4 Output:")
print("x =", x, "| type:", type(x))
print("y =", y, "| type:", type(y))
print("z =", z, "| type:", type(z))
print("-" * 40)


# ✅ Problem 5: Reassign number types
num = 5
print("Problem 5 Output:")
print("Initial:", num, "| type:", type(num))

num = 5.5
print("Reassigned to float:", num, "| type:", type(num))

num = 5 + 3j
print("Reassigned to complex:", num, "| type:", type(num))
print("-" * 40)
