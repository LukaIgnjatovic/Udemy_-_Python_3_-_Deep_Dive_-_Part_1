# Lists are mutable objects.
my_list = [1, 3, 3]

print(type(my_list))

print(id(my_list))

# Adding a new element will not change the memory location of the original list.
my_list.append(4)

print(my_list)

print(id(my_list))

# A new list is created, but its memory location is not the same as for "my_list" variable.
my_new_list = [1, 2, 3]

print(id(my_new_list))

# "4" was added to "my_new_list" by concatenation and not using "append" method, so its memory location has changed.
my_new_list = my_new_list + [4]

print(id(my_new_list))
# Using "append" changes the internal state of the variable, which means that the same object is used throughout the script.

# Dictionaries are mutable as well.
my_dict = {'key1': 1, 'key2': 'a'}

print(id(my_dict))

my_dict['key3'] = 10.5

print(id(my_dict))

# However, tuples are immutable.
my_tuple = (1, 2, 3)

print(id(my_tuple))

print(id(my_tuple[0]))

# Mutability can be tricky - tuple whose elements are lists is created.
my_new_tuple = ([1, 2], [3, 4])

print(my_new_tuple)

print(my_new_tuple[0])

print(my_new_tuple[0].append(3))

# In this way, it is possible to change internal elements of an immutable object.
print(my_new_tuple)
