# ---------------------------------------------
# 🔠 Python Built-in Data Types – Practice Problems
# ---------------------------------------------

# ✅ Problem 1: Text Type - Full name
full_name = "Rajan Sharma"
print("Problem 1:", full_name, "| Type:", type(full_name))


# ✅ Problem 2: String concatenation
first = "Rajan"
last = "Sharma"
full = first + " " + last
print("Problem 2:", full)


# ✅ Problem 3: int, float, complex types
age = 24               # int
height = 5.9           # float
z = 2 + 3j             # complex
print("Problem 3:", age, type(age), "|", height, type(height), "|", z, type(z))


# ✅ Problem 4: Arithmetic and type check
a = 10
b = 3.5
result = a + b
print("Problem 4: Result =", result, "| Type:", type(result))


# ✅ Problem 5: List of fruits
fruits = ["apple", "banana", "mango"]
print("Problem 5:", fruits[0], "| Type:", type(fruits))


# ✅ Problem 6: Tuple and length
numbers = (1, 2, 3)
print("Problem 6: Tuple =", numbers, "| Length:", len(numbers))


# ✅ Problem 7: Range and list conversion
r = range(1, 11)
r_list = list(r)
print("Problem 7:", r_list)


# ✅ Problem 8: Dictionary
person = {"name": "Rajan", "age": 24, "language": "Python"}
print("Problem 8: Language =", person["language"], "| Type:", type(person))


# ✅ Problem 9: Set of cities
cities = {"Delhi", "Mumbai", "Bangalore"}
print("Problem 9:", cities, "| Type:", type(cities))


# ✅ Problem 10: Convert list to frozenset
nums = [1, 2, 3, 4]
frozen_nums = frozenset(nums)
print("Problem 10:", frozen_nums, "| Type:", type(frozen_nums))


# ✅ Problem 11: Boolean condition
age = 24
is_adult = age > 18
print("Problem 11: Is Adult?", is_adult, "| Type:", type(is_adult))


# ✅ Problem 12: Bytes object
x = b"Python"
print("Problem 12:", x, "| Type:", type(x))


# ✅ Problem 13: Bytearray
ba = bytearray(5)
print("Problem 13:", ba, "| Type:", type(ba))


# ✅ Problem 14: Memoryview
mem = memoryview(bytes(5))
print("Problem 14:", mem, "| Type:", type(mem))


# ✅ Problem 15: NoneType
x = None
print("Problem 15:", x, "| Type:", type(x))
