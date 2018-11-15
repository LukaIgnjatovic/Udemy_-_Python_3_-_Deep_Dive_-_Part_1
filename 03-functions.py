# Importing specific functions from a module is possible.
from math import sqrt

# Entire module can be imported as well.
import math

# Some functions are available by default.
a = [1, 2, 3]

len(a)

# "sqrt" function can be called upon specific to get its square root.
sqrt(4)

# Number "pi" can be accessed via "math" library.
print(math.pi)


# New functions can be defined as well.
def func_1():
    print("Running \"func_1\".")


func_1()
# Note that to "call" or "invoke" a function we need to use the "()". Calling the function without "()" will only give its memory location.


# Arguments can be passed to the function. Annotations can be used to tell the function what are the expected argument types.
def func_2(a: int, b: int):
    return a * b


print(func_2(2, 3))

# Still, any argument type can still be passed to the function.
print(func_2("a", 3))

# Even lists can be passed.
print(func_2([1, 2], 3))

# However, strings are not supported by the "*" operator.
print(func_2("a", "b"))
