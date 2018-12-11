# Immutable objects have an easily explainable behaviour when it come to variable equality.
a = 10
b = 10

print(hex(id(a)))

print(hex(id(b)))

# Keyword "is" can be used to check if two variables point to the same memory location. This is called "identity check".
print("a is b <->", a is b)

# "==" sign can be used to check if two variables store the same values. This is called "equality check".
print("a == b <->", a == b)

# Memory locations differ for mutable objects, but equality between them still stands.
a = [1, 2, 3]
b = [1, 2, 3]

print(hex(id(a)))

print(hex(id(b)))

print("a is b <->", a is b)

print("a == b <->", a == b)

# "Equality check" between different variable types will still stand, if they are logically the same.
a = 10
b = 10.0

print(type(a))

print(type(b))

print(hex(id(a)))

print(hex(id(b)))

print("a is b <->", a is b)

print("a == b <->", a == b)

a = 10 + 0j
b = 10.0

print(type(a))

print(type(b))

print(hex(id(a)))

print(hex(id(b)))

print("a is b <->", a is b)

print("a == b <->", a == b)

# "None" object has its own memory location and type.
print(hex(id(None)))

print(type(None))

# All "None" objects point to the same memory location.
a = None
b = None
c = None

print(a is None)

print(b is None)

print(c is None)

print(a is b)

print(a is c)

print(b is c)
