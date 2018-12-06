# "sys" and "ctypes" modules are required for this lesson.
import sys
import ctypes

# A list is created to serve as the example of a variable.
a = [1, 2, 3]

print(id(a))

# "getrefcount" function returns the number of pointer that reference a specific memory address.
print(sys.getrefcount(a))
# Number "2" is printed since this function increases the reference counter by 1 by default.


# "ref_count" function will return this reference counter without increasing it by 1.
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


print(ref_count(id(a)))

# Assigning a new variable to the same memory reference as "a" will increase the reference counter as expected.
b = a

print(ref_count(id(a)))

# Assigning "b" to "None" will decrease the reference counter to address where "a" is stored.
b = None

print(ref_count(id(a)))

# "b" will have a new location now ("None" does not delete it from the memory completely, it just changes its address).
print(id(b))
