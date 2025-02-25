def my_function(name):
    return("Hello python from", {name})

print (my_function("Anas"))

# integer

x = 1
y = 3
print(type(x + y))

# # float

pi = 3.14
print(type(pi))

# # string

name = "Anas"
print(type(name))

# # boolean

is_busy = True
print(type(is_busy))

# # list or array

groceries = ["wheat", "rice", "sugar"]
print(type(groceries))

# # tuple or immutable list

tuple = ("wheat", 3.142, True, [1, 2, 3])
print(tuple)

# # # dictionary or object

person = {
    "name": "Anas",
    "age": 25,
    "is_busy": True
}
person["age"] = 20

print(person)

# # set or unique list

unique_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(type(unique_numbers))


# range or sequence of numbers

number = range(1, 10)
print(number)

# # None

value = None

print(value)


