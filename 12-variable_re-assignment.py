# Every time a variable is re-assigned, its memory location changes.
a = 10

print(hex(id(a)))

a = 15

print(hex(id(a)))

a = a + 1

print(hex(id(a)))

# However, if two variables have the same value, they will point to the same location.
a = 10

b = 10

print(hex(id(a)))

print(hex(id(a)))

a = "Hello"

b = "Hello"

print(hex(id(a)))

print(hex(id(a)))