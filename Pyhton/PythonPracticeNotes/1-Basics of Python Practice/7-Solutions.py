# ---------------------------------------------
# 🌍 Python Global Variables – Practice Problems
# ---------------------------------------------

# ✅ Problem 1: Print a Global Variable Inside Function
language = "Python"

def print_language():
    print("Problem 1 Output:", "I love " + language)

print_language()


# ✅ Problem 2: Modify a Global Variable Inside Function (Without `global`)
x = 5

def modify_without_global():
    x = 10  # This is a local variable
    print("Problem 2 Output (inside function):", x)

modify_without_global()
print("Problem 2 Output (outside function):", x)  # Still 5 — global not affected


# ✅ Problem 3: Local vs Global
name = "Rajan"  # Global

def print_names():
    name = "Sharma"  # Local
    print("Problem 3 Output (inside function):", name)

print_names()
print("Problem 3 Output (outside function):", name)


# ✅ Problem 4: Create a Global Variable from Inside a Function
def set_city():
    global city
    city = "Delhi"

set_city()
print("Problem 4 Output:", city)  # city becomes global after function call


# ✅ Problem 5: Modify Global Variable Using `global` Keyword
count = 0

def increment_count():
    global count
    count += 1

increment_count()
increment_count()
print("Problem 5 Output: count =", count)  # Should print 2
