# In Python, an iterable is an object capable of returning values one at a time. "for" loops allow for iteration over these objects.
i = 0

for i in range(5):
    print(i)

# Iteration over list is possible.
for i in [1, 2, 3, 4]:
    print(i)

# Iteration over string is possible.
for c in "Hello":
    print(c)

# Iteration over tuple is possible.
for x in ("a", "b", "c", 4):
    print(x)

# Iteration over more "complex" objects is possible, as well. This is a list containing tuples.
for x in [(1, 2), (3, 4), (5, 6)]:
    print(x)

# Unpacking of tuples inside a list is enabled, too.
for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

# "continue" and "break" statements work just as intended.
for i in range(5):
    if i == 3:
        continue
    print(i)

for i in range(5):
    if i == 3:
        break
    print(i)

# "else" is can be used with "for" loop.
for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print("Multiple of 7 found.")
        break
else:
    print("No multiple of 7 in the range.")

for i in range(1, 10):
    print(i)
    if i % 7 == 0:
        print("Multiple of 7 found.")
        break
else:
    print("No multiple of 7 in the range.")

# "try" and "catch" work with "for" loops as well.
for i in range(5):
    print("----------")
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print("Division by 0.")
        continue
    finally:
        print("This always executes.")
    print(i)

# Strings and sets are iterable, but they are not indexed inside the "for" loop.
s = "Hello"

for c in s:
    print(c)

# However, this can be bypassed with two different approaches.
s = "Hello"
i = 0

for c in s:
    print(i, c)
    i += 1

for i in range(len(s)):
    print(i, s[i])

# "enumerate" function can do this, as well. It returns a tuple.
for i, c in enumerate(s):
    print(i, c)
