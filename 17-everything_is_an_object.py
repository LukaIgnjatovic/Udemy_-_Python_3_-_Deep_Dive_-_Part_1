# Assigning an integer to a variable actually makes an instance of "int" class and assigns it to that variable.
a = 10

print(type(a))

# Using the "int" function does the same thing actually.
b = int(10)

print(type(b))

# Checking the documentation is possible using the "help" function.
help(int)

# If "x" is property is not given, "int" class assigns value "0" to its instance.
c = int()

print(c)

# "int" class has an additional property, "base". If "base" is used, "x" argument has to be a string.
c = int("101", base=2)

print(c)


# Function that returns the square value of an input is defined.
def square(a):
    return a ** 2


print(type(square))

# If is "square" is located somewhere in the memory, it is possible to assign it to another variable.
f = square

# Since this is true, their memory locations should match.
print(hex(id(square)))

print(hex(id(f)))

print(f is square)

print(square(2))

print(f(2))


# Function that returns the cube value of an input is defined.
def cube(a):
    return a ** 3


# Function that returns either "square" or "cube" function depending on an input is defined.
def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube


# Now "f" can be assigned to either "square" or "cube" function depending on the "select_function" input value.
f = select_function(1)

print(f is square)

# "f" can be invoked like any other function.
print(f(2))

f = select_function(2)

print(f is cube)

print(f(2))

# Assigning the result of "select_function" is not necessary.
print(select_function(2)(3))


# It is possible to create a function that calls other functions directly in a more expressive manner.
def exec_function(fn, n):
    return fn(n)


print(exec_function(cube, 3))

print(exec_function(square, 3))
