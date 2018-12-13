# Strings that look like identifiers are interned. Identifiers must start with "_" or a letter and can only contain "_", letters and numbers.
# Counting on interning can be a bad idea in Python.
# However, Python can be forced to intern a string using "sys.intern()" method.
# This enables much faster string comparison since "is" operator that compares memory addresses is much faster than "==" operator that compares string letter by letter.
# It should be noted that instructor's code in tutorial and code in this script differ in behaviour when strings are defined in a way that breaks the identifier rules.
# This is probably due to different versions of Python used in instructor's tutorial and here.

# "sys" library is loaded to enable calling of "sys.intern()" method. "time" library is loaded to enable timing of code execution.
import sys
import time

# "a" and "b" are variables that are defined to qualify as identifiers.
a = "Hello"
b = "Hello"

print(hex(id(a)))

print(hex(id(b)))

# If "a" and "b" variables are defined in a way that breaks the identifier rules, they should not point to the same location.
# However, this is where this Python script behaves differently than in instructor's tutorial.
a = "Hello world."
b = "Hello world."

# These addresses are not be the same in instructor's tutorial.
print(hex(id(a)))

print(hex(id(b)))

# This statement returns "False" in instructor's tutorial.
print(a is b)

# However, this statement should always return "True".
print(a == b)

# String length should not really matter when it comes to interning it, if the rules of identifiers still stand.
a = "_this_is_a_long_string_that_could_be_used_as_an_identifier"
b = "_this_is_a_long_string_that_could_be_used_as_an_identifier"

# This statement should return "True", since rules for identifiers are not broken.
print(a is b)

# Automatic string interning does not have to be relied upon. It is possible to force Python to intern strings when needed.
a = sys.intern("Hello world.")
b = sys.intern("Hello world.")
c = "Hello world."

# "a" and "b" should point to the same memory location when defined in this way and "c" should be pointing to a different memory location.
# However, this is where this Python script behaves differently than in instructor's tutorial.
print(hex(id(a)))

print(hex(id(b)))

print(hex(id(c)))

# Instead of comparing "a" and "b" using "==" operator that does letter by letter comparison, it is much faster to compare their memory locations using "is" operator.
print(a is b)


# String interning should be used only when there is a need to compare a lot of strings (emphasis on "a lot").
def compare_using_equals(n):
    a = "a long string that is not interned" * 200
    b = "a long string that is not interned" * 200
    for i in range(n):
        if a == b:
            pass


def compare_using_interning(n):
    a = sys.intern("a long string that is not interned" * 200)
    b = sys.intern("a long string that is not interned" * 200)
    for i in range(n):
        if a is b:
            pass


# "perf_counter()" method will count the number of milliseconds required for code to execute.
start = time.perf_counter()

# Running "compare_using_equals" function 10 million times should be long enough to notice the time difference in execution.
compare_using_equals(10000000)

end = time.perf_counter()

# The time required to execute the code is printed, so comparison is easier to perform.
print("Time needed to execute 10 million loops using \"==\" operator is", end - start, "seconds.")

start = time.perf_counter()

compare_using_interning(10000000)

end = time.perf_counter()

print("Time needed to execute 10 million loops using \"is\" operator is", end - start, "seconds.")
# Interning is much faster, as shown in this example.
