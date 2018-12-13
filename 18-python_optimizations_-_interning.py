# The "interning" in Python means that some objects are reused on demand.
# At startup, Python (CPython), pre-loads (caches) a global list of integers in the range [-5, 256].
# Any time an integer is referenced in that range, Python will use the cached version of that object.
# These objects are called singletons and the optimization strategy is that small integers show up often.
# When "a = 10" is executed, Python just has to point to the existing reference for 10.
# However, when "a = 257" is executed, Python does not use that global list and a new object is created every time.
# It should be noted that instructor's code in tutorial and code in this script differ in behaviour when referencing numbers outside of singleton range.
# This is probably due to different versions of Python used in tutorial and here.

# Creating variables in singleton range will always point to the same memory location.
a = 10
b = 10

print(hex(id(a)))

print(hex(id(b)))

# The simplest way of comparing memory addresses is by using the "is" operator.
print(a is b)

# Creating variables outside of single range should always create a new object. However, this is where this Python script behaves differently than in instructor's tutorial.
a = 257
b = 257

# These addresses are not be the same in instructor's tutorial.
print(hex(id(a)))

print(hex(id(b)))

# This statement returns "False" in instructor's tutorial.
print(a is b)

# Still, different variables that have the same value should point to the same memory location.
a = 10
b = int(10)
c = int("10")
d = int("1010", base=2)

print(hex(id(a)))

print(hex(id(b)))

print(hex(id(c)))

print(hex(id(d)))
