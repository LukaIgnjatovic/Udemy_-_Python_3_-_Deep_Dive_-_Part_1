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

# There is no limit on the number of different objects a class can initialize.
r2 = Rectangle(10, 20)

# Even though "r1" and "r2" have the same properties, they are not the same objects.
print(r1 is not r2)
# This has returned "True" since the memory locations of respective objects are different.

# However, checking for equality will return "False", as well.
print(r1 == r2)


# This can be changed by altering the "eq" method.
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

    def __eq__(self, other):
        # "other" needs to be an instance of "Rectangle", same as "self".
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        # Comparing something that is not "Rectangle" with "Rectangle" must return "False".
        else:
            return False


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)

print(r1 == r2)

print(r1 == 100)


# Changing the "lt" method allows for "less than" comparison between "Rectangle" objects.
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

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            # Return an error without raising an exception.
            return NotImplemented


r1 = Rectangle(10, 20)
r2 = Rectangle(100, 200)

print(r1 < r2)

# This works as well. Even though "gt" method was not implemented, Python tries to flip the values inside comparison and executes "r1 < r2" with "lt".
print(r2 > r1)
# However, calling r1 <= r2 will not work, since methods that perform "<=" or ">=" operations have not been changed.


# It is a good practice to define "getters" and "setters" that will not allow to change properties of "Rectangle" to negative values, for example.
class Rectangle:
    # Putting an "_" in front of a variable means that this variable should be treated as private.
    # "_width" and "_height" are pseudo-private properties.
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive.")
        else:
            self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height <= 0:
            raise ValueError("Height must be positive.")
        else:
            self._height = height

    def __str__(self):
        return "Rectangle with width = {0} and height = {1}.".format(self._width, self._height)

    def __repr__(self):
        return "Rectangle({0}, {1}).".format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        else:
            return False


r1 = Rectangle(10, 20)

# Typing "r1.width" will raise an error, since there is no property called "width". "r1._width" will work, but it should not be used.
# Instead, "getwidth" method should be called upon on "Rectangle" object.
print(r1.get_width())

print(r1._width)
# Typing "r1.width = -100" will still work, however. This is called monkey patching and it will be covered later in the course.

# "set_width" can be used to set the value of property. Using "set_width" method to set width value to -10 will throw an error.
r1.set_width(100)

print(r1)


# "Pythonic" way of writing "getters" and "setters" is done like this.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # By not putting "_" in front of "width" and "height", the class will raise an error when trying to instance "r1 = Rectangle(-100, 20)", as well.
    # This is due to the fact the "setter" function will be called upon instancing. Writing code in this way enables backward compatibility.

    # Function that comes after "@property" is a property.
    @property
    def width(self):
        return self._width

    # Different property is in front of the function, so it is possible for them to have the same name.
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive.")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Height must be positive.")
        else:
            self._height = height

    def __str__(self):
        return "Rectangle with width = {0} and height = {1}.".format(self.width, self.height)

    def __repr__(self):
        return "Rectangle({0}, {1}).".format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False


r1 = Rectangle(10, 20)

# This will work with properties defined in the last "Rectangle" class.
print(r1.width)

r1.height = 100
print(r1)
