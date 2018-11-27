# "try" and "catch" statements are used regularly in Python.
a = 10
b = 1

try:
    a / b
except ZeroDivisionError:
    print("Division by 0.")
finally:
    print("This always executes.")

# "while" loop can be combined with "try" and "catch" blocks is possible.
a = 0
b = 2

while a < 4:
    print("----------")
    a += 1
    b -= 1

# "continue" will ensure that execution will go on even when exception is raised.
    try:
        a/b
    except ZeroDivisionError:
        print("{0}, {1} - division by 0.".format(a, b))
        continue
    finally:
        print("{0}, {1} - this always executes.".format(a, b))

    print("{0}, {1} - main loop.".format(a, b))

a = 0
b = 2

while a < 4:
    print("----------")
    a += 1
    b -= 1

# "break" will ensure that the execution is halted when exception is raised.
    try:
        a/b
    except ZeroDivisionError:
        print("{0}, {1} - division by 0.".format(a, b))
        continue
    finally:
        print("{0}, {1} - this always executes.".format(a, b))

    print("{0}, {1} - main loop.".format(a, b))
# "else" branch will be executed only if "break" was never encountered.
else:
    print("Code executed without a zero divison error.")
