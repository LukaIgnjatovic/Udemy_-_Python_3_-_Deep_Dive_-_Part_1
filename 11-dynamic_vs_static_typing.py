# Python is dynamically typed language. This means that variable does not have any information about its type when it is defined - its type can change
# throughout code. When "type" function is called, it only returns the type of object that the variable is currently pointing at.
a = "Hello."

print(type(a))

a = 10

print(type(a))

a = lambda x: x ** 2

print(type(a))

a = 3 + 4j

print(type(a))
