# "math" module is going to be needed for some of the exercises in this example.
import math

# Addition, subtraction and multiplication between integers always results in an integer. Also, calculating exponent of two integers is an integer.
print(type(1 + 1))

print(type(4 - 10))

print(type(2 * 3))

print(type(3 ** 6))

# Division does not follow this rule, however.
print(type(2 / 3))

print(type(10 / 2))

# "floor" method returns the largest integer value less than or equal to x.
print(math.floor(3.15))

print(math.floor(4.9999))

print(math.floor(5.00))

print(math.floor(-6.7))

# Floats have limited precision in Python which leads to some weird cases.
print(math.floor(-3.0000000000001))

print(math.floor(-3.0000000000000001))
# "1" at the end was dropped, because of this restriction.

# "floor" and "trunc" modules differ from each other.
a = 33
b = 16

print(a / b)
print(a // b)
print(math.floor(a / b))
print(math.trunc(a / b))

a = -33
b = 16

print(a / b)
print(a // b)
print(math.floor(a / b))
print(math.trunc(a / b))

# "Mod" operator ("%") returns the remainder after division.
a = 13
b = 4

print("{0} / {1} = {2}".format(a, b, a / b))
print("{0} // {1} = {2}".format(a, b, a // b))
print("{0} % {1} = {2}".format(a, b, a % b))

# Formula that satisfies "mod" and "floor" divisions is defined like this.
print(a == b * (a // b) + (a % b))
