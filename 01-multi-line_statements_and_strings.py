# Lists are basic Python data structures.
a = [1, 2, 3]

# List can be created with new lines in it.
a = [1, 2,
     3, 4, 5]
print(a)

# Comments can be added when the list is created with new lines.
a = [1,  # item 1
     2]
print(a)

# The same goes for tuples...
a = (1,  # comment
     2,  # comment
     3)
print(a)

# Dictionaries as well...
a = {"key_1": 1,  # value for key_1
     "key_2": 2   # value for key_2
     }
print(a)


# Even for arguments inside a function.
def my_func(a,  # this is used to indicate "a"...
            b,  # this is used to indicate "b"...
            c):
    print(a, b, c)


# This work when the function is called upon, too.
my_func(10,  # comment
        20,  # comment
        30   # comment
        )

# For "if" statements, we have to "/" operator to denote that it is the continuation of the same condition.
a = 10
b = 20
c = 30
if a > 5 \
    and b > 10 \
        and c > 20:
    print("Yes.")

# Multi-line strings are defined with triple delimiters.
a = """This is a string."""
print(a)

a = """This 
is a string."""
print(a)

a = """This
    is a string
        that is created over multiple lines."""
print(a)

# If a comment looks good while we are writing it, it does not mean it will look good in console.
a = """Some items:
        1. Item 1
        2. Item 2"""
print(a)


# Indentation is needed in order for code to work properly.
def my_func():
    a = """A multi-line string
    that is indented in the second line."""
    return a


print(my_func())
