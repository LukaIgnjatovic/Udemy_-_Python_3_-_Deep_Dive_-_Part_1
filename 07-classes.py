# Classes are defined with "class" keyword.
# "self" keyword denotes an object that was just created.
# "width" and "height" are going to be properties of the class "Rectangle".


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


# Object can be initialized with its properties.
r1 = Rectangle(10, 20)

# Properties of an object can be called upon.
print(r1.width)

# Properties of an object can be changed, as well.
r1.width = 100

print(r1.width)


# Method can be implemented in a class.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.width)


# Methods of a class are easily called upon.
r1 = Rectangle(10, 20)

print(r1.area())

print(r1.perimeter())

# An object can be printed. "__main__" is the current module.
print(str(r1))


# Printed value is just Python's definition of that object. Printing of an object along with its properties can be done with new module ("to_string").
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.width)

    def to_string(self):
        return "Rectangle with width = {0} and height = {1}.".format(self.width, self.height)


r1 = Rectangle(10, 20)

print(r1.to_string())


# Behaviour of an already defined method can be changed through the use of "magic methods".
# "Magic methods" are special methods that are redefined to add "magic" to your classes.
# They're always surrounded by double underscores (e.g. __init__ or __lt__).
# The behaviour of "str" method is now going to be altered to print the "Rectangle" object alongside its properties.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.width)

    def __str__(self):
        return "Rectangle with width = {0} and height = {1}.".format(self.width, self.height)


r1 = Rectangle(10, 20)

print(str(r1))

# Still, printing an object.
print(repr(r1))


# This can be changed by altering the "repr" method.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.width)

    def __str__(self):
        return "Rectangle with width = {0} and height = {1}.".format(self.width, self.height)

    def __repr__(self):
        return "Rectangle({0}, {1}).".format(self.width, self.height)


r1 = Rectangle(10, 20)

print(repr(r1))
