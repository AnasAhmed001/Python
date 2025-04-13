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

