# Variables in Python are passed by reference.
my_var = 10

print(my_var)

# Printing the result of "id" function will return the memory location where variable "my_var" is stored.
print(id(my_var))

# Using the "hex" function on the output of the "id" function can return the hexadecimal value of the memory location where the variable is stored.
print(hex(id(my_var)))
