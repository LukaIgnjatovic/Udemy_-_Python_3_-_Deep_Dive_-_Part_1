# Shared references are used for immutable objects.
a = "Hello..."
b = a

print(hex(id(a)))

print(hex(id(b)))

# Python (sometimes) does this automatically in the case when the values of variables are the same, but their assignment is explicit.
a = "World!"
b = "World!"

print(hex(id(a)))

print(hex(id(b)))

# Changing the value of a variable will change its memory location as well.
b = "Hello world."

print(hex(id(b)))

print(hex(id(a)))

# This is not quite the same for mutable objects...
a = [1, 2, 3]
b = a

print(hex(id(a)))

print(hex(id(b)))

# Appending a value to one of the lists will change contents of both lists, but their memory location will stay the same.
b.append(100)

print(hex(id(a)))

print(hex(id(b)))

print(a)

print(b)
