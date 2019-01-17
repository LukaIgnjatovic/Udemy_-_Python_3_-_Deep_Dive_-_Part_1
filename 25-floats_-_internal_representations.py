# "Fraction" class from "fractions" module and "math" module are going to be needed for some of the exercises in this example.
from fractions import Fraction
import math

# Documentation for "Float" class can be called upon like this.
help(float)

# Same as "int", "float" can take many data types as input.
print(float(10))

print(float(10.4))

print(float("12.5"))

# However, decimals are not supported. The next line is commented because it would throw an error otherwise.
# print(float("22/7"))

# To convert fraction object to a float object, object of "Fraction" class has to be created first.
a = Fraction("22/7")

print(float(a))

# Internal representation of floats is a bit tricky in Python.
print(0.1)

print(format(0.1, ".15f"))

print(format(0.1, ".25f"))

# This is due to Python's inability to store certain decimal numbers accurately.
a = 0.1 + 0.1 + 0.1
b = 0.3

print(a == b)

# When the precision of a decimal number reaches a certain point, it can be seen why "a" is not equal to "b".
print(format(a, ".25f"))

print(format(b, ".25f"))
