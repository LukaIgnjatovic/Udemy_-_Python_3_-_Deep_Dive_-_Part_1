# "ctypes" and "gc" modules are required for this lesson.
import ctypes
import gc


# "ref_count" function will return the reference counter.
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


# "object_by_id" function will compare objects in the garbage collector.
def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists."
    return "Object not found."


# Classes "A" and "B" are defined in order to create a circular reference.
class A:
    def __init__(self):
        self.b = B(self)
        print("A: self: {0}, b: {1}".format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        print("B: self: {0}, a: {1}".format(hex(id(self)), hex(id(self.a))))


# The garbage collector is disabled.
gc.disable()

my_var = A()

print(hex(id(my_var)))

print(hex(id(my_var.b)))

print(hex(id(my_var.b.a)))

# "a_id" and "b_id" variables are created to store the memory locations of "my_var" and "my_var.b".
a_id = id(my_var)

b_id = id(my_var.b)

print(hex(a_id))

print(hex(b_id))

# Number of pointers to "a_id"'s location.
print(ref_count(a_id))
# This number is "2" since "my_var" and "b" are pointing to "a_id".

# Number of pointers to "b_id"'s location.
print(ref_count(b_id))
# This number is "1" since "a" is pointing to "b_id".

# Check is perfored to see if "a_id_ and "b_id" are still there.
object_by_id(a_id)

object_by_id(b_id)

# "my_var" is going to be changed to "None", that reference is destroyed.
my_var = None

# Circular reference is created now - "a" is pointing to "b", and "b" is pointing to "a".
print(ref_count(a_id))

print(ref_count(b_id))

# Objects "a_id" and "b_id" still exist since the garbage collector is turned off.
object_by_id(a_id)

object_by_id(b_id)

# Garbage collector can be called upon manually.
gc.collect()

# Garbage collector has collected objects "a_id" and "b_id".
object_by_id(a_id)

object_by_id(b_id)

# However, reference counters have not been set to 0 - these memory addresses are now used for something else.
print(ref_count(a_id))

print(ref_count(b_id))
# This illustrates exactly why it is so tricky to work with memory addresses and why the garbage collector is essential.
