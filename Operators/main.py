# Arrithmetic operators
# Arithmetic operators are used to perform basic mathematical operations.
a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a % b)  # Modulus (remainder): 1
print(a ** b) # Exponentiation: 1000
print(a // b) # Floor division: 3

# Assignment operators
# Assignment operators are used to assign values to variables.

x = 5

x += 2  # x = x + 2 → 7
x -= 1  # x = x - 1 → 6
x *= 3  # x = x * 3 → 18
x /= 2  # x = x / 2 → 9.0
x %= 5  # x = x % 5 → 4.0
x **= 2 # x = x ** 2 → 16.0
x //= 3 # x = x // 3 → 5.0

# Comparison operators
# Comparison operators are used to compare two values.

a = 5
b = 10

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= 5)  # True
print(b <= 10) # True


# Logical operators
# Logical operators are used to combine conditional statements.

x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
print(not y)    # True

# Identity operators
# Identity operators are used to compare the memory locations of two objects.

a = [1, 2]
b = a
c = [1, 2]

print(a is b)      # True (same object)
print(a is c)      # False (same value, different object)
print(a is not c)  # True
print(a is not b)  # False (same object)

# Membership operators
# Membership operators are used to test if a value is in a sequence (like a list, tuple, or string).

fruits = ['apple', 'banana', 'cherry']

print('banana' in fruits)     # True
print('mango' not in fruits)  # True
print('apple' in fruits)      # True
print('grape' not in fruits)  # True


# Bitwise operators
# Bitwise operators are used to perform bit-level operations on integers.

a = 5       # 0b0101
b = 3       # 0b0011

print(a & b)  # AND: 1
print(a | b)  # OR: 7
print(a ^ b)  # XOR: 6
print(~a)     # NOT: -6
print(a << 1) # Left shift: 10
print(a >> 1) # Right shift: 2
