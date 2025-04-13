# if statement

age = 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")


# For loop

for i in range(5):
    print("Number:", i)

# While loop

count = 0
while count < 3:
    print("Counting:", count)
    count += 1


# Break and continue statement

for i in range(5):
    if i == 3:
        break  # stops the loop
    print(i)

for i in range(5):
    if i == 2:
        continue  # skips this iteration
    print(i)


# Lists, Tuples, and Dictionaries

# List
# A list is a collection of items that can be changed, ordered, and allows duplicates.

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits[1])  # banana

# tuple
# Tuples are immutable:

colors = ('red', 'green', 'blue')
print(colors[0])  # red

# colors[0] = 'yellow' → ❌ This will cause an error

# Dictionary
# A dictionary is a collection of key-value pairs.

person = {
    'name': 'Alice',
    'age': 25
}
print(person['name'])  # Alice
person['age'] = 26  # Update value

# set and frozenset
# A set is an unordered collection of unique items.
# A frozenset is an immutable version of a set.

# Set
numbers = {1, 2, 3, 3}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}

#set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)  # Intersection: {3}
print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a - b)  # Difference: {1, 2}

# frozenset
fs = frozenset([1, 2, 3])
print(fs)

# fs.add(4) → ❌ Error: frozenset is immutable

# control modules and functions
# A module is a file containing Python code. A function is a block of reusable code.
# You can create your own modules and functions.

# function definition and call

def greet(name):
    print("Hello,", name)

greet("Alice")

# importing modules

import math

print(math.sqrt(16))  # 4.0

# importing specific functions

from math import pi

print(pi)  # 3.141592653589793

# Exceptin handling
# Exceptions are errors that occur during the execution of a program.
# You can handle exceptions using try and except blocks.

# try-except block

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input. Please enter a number.")


# try-except-finally block

try:
    x = int("hello")
except ValueError:
    print("Conversion failed.")
finally:
    print("This block always runs.")


# file handling
# Python provides built-in functions to handle files.
# You can read from and write to files.

# writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
    

# appending to a file

with open("example.txt", "a") as file:
    file.write("\nAppending a new line.")

# using math module

import math

print(math.pow(2, 3))  # 8.0
print(math.factorial(5))  # 120

# using date time module

from datetime import datetime

now = datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)

# using calendar module

import calendar

# Print calendar for April 2025
print(calendar.month(2025, 4))

# Check if a year is leap year
print(calendar.isleap(2024))  # True
