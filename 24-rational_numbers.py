# "Fraction" class from "fractions" module and "math" module are going to be needed for some of the exercises in this example.
from fractions import Fraction
import math

# Documentation for "Fraction" class can be called upon like this.
help(Fraction)

# "Fraction" instances have 2 input values: numerator (default value - 0) and denominator (default value - 1).
print(Fraction(1))

print(Fraction(numerator=2, denominator=1))

print(Fraction(3, 4))

# This method can take various types of inputs, same as "int" method.
print(Fraction(0.125))

print(Fraction("0.125"))

print(Fraction("22/7"))

# Working with variables of class "Fraction" is possible, as well.
x = Fraction(2, 3)
y = Fraction(3, 4)

print(x + y)

print(x * y)

print(x / y)

# "Fraction" automatically reduces the number given to its least common denominator.
print(Fraction(8, 16))

# Negative sign is always assigned to the numerator.
print(Fraction(1, -4))

# Properties of the "Fraction" object can be easily accessed.
a = Fraction(1, -4)

print(a.numerator)

print(a.denominator)

# Irrational numbers are a bit quirky, since there is a memory limit on how much digits can be stored in their representation.
x = Fraction(math.pi)

print(x)

# "pi" can be represented as a rational number using "float" method, but this representation is only an approximation, due to memory limitations.
print(float(x))

# Square root of 2 will follow along the same lines.
y = Fraction(math.sqrt(2))

print(y)

print(float(y))

# Python "hides" certain stuff under the hood when it comes to storing rational numbers.
a = 0.125

print(a)

b = 0.3

print(b)

# Everything looks fine, so far. However, when it comes to representing these numbers as fractions, certain things "under the hood" come up.
print(Fraction(a))

print(Fraction(b))

# This can be demystified. "0.3" is not actually stored as "0.3", but as its approximation.
print(format(b, "0.5f"))

print(format(b, "0.15f"))

print(format(b, "0.25f"))

# This is why the resulting numbers of "Fraction" class differ from "3" and "10" for value "0.3".
x = Fraction(0.3)

print(x)

# It is possible to use the "limit_denominator" property to change the output values.
print(x.limit_denominator(10))

# This works with any number.
y = Fraction(math.pi)

print(y)

# It is possible to represent the closest value of pi whose denominator cannot be greater than "10".
print(y.limit_denominator(10))

print(22 / 7)
# As it can be seen, this value is a close approximation of pi.
