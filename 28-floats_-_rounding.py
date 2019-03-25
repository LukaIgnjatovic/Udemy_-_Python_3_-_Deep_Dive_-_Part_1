# "round" function is already available in Python.
help(round)

# "round" functionality can be seen in the next example.
a = round(1.9)

# If argument "ndigits" is not specified, the "round" function will return an "int".
print(a, type(a))

a = round(1.9, 0)

# However, if the argument "ndigits" is specified, the number returned will have the same type as the "number" argument.
print(a, type(a))

# Using the "round" on consecutively on an example can showcase what it does more clearly.
print(round(1.8888, 3))

print(round(1.8888, 2))

print(round(1.8888, 1))

print(round(1.8888, 0))

# "ndigits" argument can be lower than zero.
print(round(888.88, 1))

print(round(888.88, 0))

print(round(888.88, -1))

print(round(888.88, -2))

print(round(888.88, -3))

print(round(888.88, -4))

# "0" is a multiple of "10.000" and that is the reason the last expression resulted in a zero ("888.88" is closer to "0" than to "10.000").
print(round(8888.88, -4))

# When there are ties, Python uses "Bankers' Rounding". It rounds numbers to the least significant digits.
print(round(1.25, 1))

print(round(1.35, 1))


# If the rounding "away from zero" is required, a new function has to be defined. It will be called "_round", so it does not overlap with the built-in "round" method.
def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))


# This new function can be compared with regular "round" method on positive and negative numbers.
print(round(1.5), _round(1.5))

print(round(2.5), _round(2.5))

print(round(-1.5), _round(-1.5))

print(round(-2.5), _round(-2.5))
