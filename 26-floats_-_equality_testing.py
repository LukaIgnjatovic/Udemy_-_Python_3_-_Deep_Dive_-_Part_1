# "isclose" method from "math" module is going to be needed for some of the exercises in this example.
from math import isclose

# Quirkiness of storing decimal numbers in binary format was shown in the last exercise.
x = 0.1

# Even though "print(x)" would output "0.1", it can be seen that this is not really the case with the "format" method.
print(format(x, ".25f"))

# However, if the number can be represented with some combination of the power of 2 in the denominator, then the number is stored correctly.
y = 0.125

print(format(y, ".25f"))

# This can be further shown with the next example.
a = 0.125 + 0.125 + 0.125
b = 0.375

print(a == b)

# Numbers that cannot be represented with some combination of the power of 2 in the denominator are still prone to incorrect representation. This can be bypassed by using the "round" method.
print(round(a, 3) == round(b, 3))

# This approach does not take into account the magnitude of variables.
x1 = 123456789.01
y1 = 123456789.02

x2 = 0.01
y2 = 0.02

# Absolute tolerance (absolute difference) between "x1" and "y1" versus "x2" and "y2" is "0.01", but the relative "delta" is quite different.
print(y1 / x1)

print(y2 / x2)

# This can be seen by using the "round" method on these examples.
print(round(x1, 1) == round(y1, 1))

# However, with "x2" and "y2" this should not be true, since "y2" is two times greater than "x2".
print(round(x2, 1) == round(y2, 1))

# "isclose" method can be used to check if two values are close to each other in a more sophisticated manner, with both relative and absolute tolerance.
help(isclose)

# This method is going to be used on the example mentioned in the last exercise.
x = 0.1 + 0.1 + 0.1
y = 0.3

print(isclose(x, y))

print(x == y)

# "isclose" seems to work as expected with default values in most cases.
print(isclose(x1, y1))

print(isclose(x2, y2))

# However, as usual, there is a caveat. Some times default values of "rel_tol" and "abs_tol" of "isclose" method have to be changed.
x = 0.0000001
y = 0.0000002

print(isclose(x, y, rel_tol=0.01))
# This should not be considered "False" in most cases. The workaround is to use "abs_tol" as well.

print(isclose(x, y, rel_tol=0.01, abs_tol=0.0001))

# These values can be tested on another example.
x = 999999999.01
y = 999999999.02

print(isclose(x, y, rel_tol=0.01, abs_tol=0.0001))
