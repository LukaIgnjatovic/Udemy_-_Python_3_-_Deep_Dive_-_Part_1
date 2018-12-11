# "modify_string" function is going to show how strings are immutable by printing the memory address before and after string concatenation.
def modify_string(s):
    print("Initial \"s\" memory address is {0}.".format(hex(id(s))))
    s = s + " world."
    print("Final \"s\" memory address is {0}.".format(hex(id(s))))


my_string = "Hello"

print("\"my_string\" memory address is {0}.".format(hex(id(my_string))))

modify_string(my_string)
# By calling "modify_string" on "my_string" shows that "my_string" and initial "s" have the same address.
# However, final "s" points to another memory location.

# "my_string"'s memory address and value stay the same after calling the "modify_string" function.
print(hex(id(my_string)))

print(my_string)


# "modify_list" function is going to show how lists are mutable by printing the memory address before and after appending elements to a list.
def modify_list(lst):
    print("Initial \"lst\" memory address is {0}.".format(hex(id(lst))))
    lst.append(100)
    print("Final \"lst\" memory address is {0}.".format(hex(id(lst))))


my_list = [1, 2, 3]

print(hex(id(my_list)))

modify_list(my_list)
# By calling "modify_list" on "my_list" shows that "my_list", initial "lst" and final "lst" have the same address.

# "my_list"'s memory address stays the same after calling the "modify_string" function, but its value has changed.
print(hex(id(my_list)))

print(my_list)


# Immutable objects are generally safer when operating with them. However, this is not always true.
def modify_tuple(t):
    print("Initial \"t\" memory address is {0}.".format(hex(id(t))))
    t[0].append(100)
    print("Final \"t\" memory address is {0}.".format(hex(id(t))))


my_tuple = ([1, 2], "a")

print(hex(id(my_tuple)))

modify_tuple(my_tuple)
# By calling "modify_tuple" on "my_tuple" shows that "my_tuple", initial "t" and final "t" have the same address.

# "my_tuple"'s memory address stays the same after calling the "modify_tuple" function, tuple's values have not changed.
# However, the values inside tuple have changed.
print(hex(id(my_tuple)))

print(my_tuple)
