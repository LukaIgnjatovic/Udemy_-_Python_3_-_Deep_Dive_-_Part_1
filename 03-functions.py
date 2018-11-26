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

# However, strings are not supported by the "*" operator. The next line is commented because it would throw an error otherwise.
# print(func_2("a", "b"))

# Calling the function without the arguments will just print its definition and memory location.
print(func_2)


# Functions can call other functions in their execution.
def func_3():
    return func_4()


def func_4():
    return print("Running func_4")


func_3()


# Still, the proper order of execution is essential. The next lines are commented because they would throw an error otherwise.
# def func_5():
#     return func_6()


# func_5()


# def func_6():
#     return print("Running func_5")

# Lambda functions are also present in Python.
fn1 = lambda x: x**2

print(fn1(2))
