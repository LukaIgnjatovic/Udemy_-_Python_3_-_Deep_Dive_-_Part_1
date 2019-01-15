# "fractions" module is going to be needed for some of the exercises in this example.
import fractions

# Documentation for "Integer" class can be called upon like this.
help(int)

# "int" method has a default value of 0.
a = int()

print(a)

# "int" can take floats as input.
print(int(10.99))

# Booleans as well.
print(int(True))
print(int(False))

# Fractions will be covered in detail later, but "int" method can work with them too.
a = fractions.Fraction(22, 7)

print(a)

print(int(a))

# "int" can work with strings, if they contain only numbers.
print(int("12345"))

# "base" argument in "int" method can take various integer values, from 2 to 36.
print(int("101", base=2))

# Strings in the first argument are not case-sensitive.
print(int("FF", base=16))
print(int("ff", base=16))

# Values can be "out of range" for a certain base. For base 11, values go from 0 up to A. The next line is commented because it would throw an error otherwise.
# print(int("B", base=11))

# "bin" method can change a number's representation from base 10 to base 2.
print(bin(10))

# "oct" method can change a number's representation from base 10 to base 8.
print(oct(10))

# "hex" method can change a number's representation from base 10 to base 16.
print(hex(255))

# Variables can be assigned in binary (octal, hexadecimal), as well.
a = int("101", base=2)
b = 0b101

print(a)
print(b)


# Function can be defined that changes number's representation from base 10 to an arbitrary base.
def from_base_10(n, b):
    # Base cannot be less than 2.
    if b < 2:
        raise ValueError("Base \"b\" must be >= 2")

    # This function will work only for positive numbers.
    if n < 0:
        raise ValueError("Number \"n\" must be >= 0")

    # 0 will stay 0, no matter the base.
    if n == 0:
        return [0]

    digits = []

    while n > 0:
        # Next two lines would be used to assign "mod" ("m") and "div" ("n") values in a classic approach. However, "divmod" method can return both values at once.
        # m = n % b
        # n = n // b
        n, m = divmod(n, b)
        digits.insert(0, m)

    return digits


# "from_base10" function will change the number's representation depending on the input values.
print(from_base_10(10, 2))

print(from_base_10(255, 16))
# Convention states that all numbers encoded to values larger than 9 should be "translated" to a letter. For example, 10 = "A", 11 = "B", etc.


# "encode" function is going to provide this functionality.
def encode(digits, digit_map):
    # The maximum digit from "digits" has to have a proper represent in "digit_map".
    if max(digits) >= len(digit_map):
        raise ValueError("\"digit_map\" is not long enough to encode \"digits\"")

    encoding = ""

    for d in digits:
        encoding += digit_map[d]

    return encoding


# "encode" function will encode input digits depending on the input digit map.
print(encode([15, 15], "0123456789ABCDEF"))


# "encode" function can be defined in a much simpler and efficient way with list comprehensions.
def encode(digits, digit_map):
    # The maximum digit from "digits" has to have a proper represent in "digit_map".
    if max(digits) >= len(digit_map):
        raise ValueError("\"digit_map\" is not long enough to encode \"digits\"")

    return "".join([digit_map[d] for d in digits])


print(encode([15, 15], "0123456789ABCDEF"))


# Now, a function can be defined, "rebase_from10", that will call both "from_base10" and "encode" functions to .
def rebase_from_base_10(number, base):
    # "digit_map" is going to contain all the possible numbers and letters.
    digit_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # "base" argument cannot be less than 2 and greater than 36.
    if base < 2 or base > 36:
        raise ValueError("Invalid base: 2 <= base >= 36.")

    # Negative numbers are going to be included in this function.
    sign = -1 if number < 0 else 1

    # By multiplying "number" with "sign", it is ensured that "number" from then on will be positive.
    number *= sign

    digits = from_base_10(number, base)

    encoding = encode(digits, digit_map)

    if sign == -1:
        encoding = "-" + encoding

    return encoding


# It is time to check if the function does what it is supposed to.
e = rebase_from_base_10(10, 2)

print(e)

print(int(e, base=2))

# Changing the base works flawlessly.
e = rebase_from_base_10(3451, 16)

print(e)

print(int(e, base=16))

# Last test is going to be a negative number.
e = rebase_from_base_10(-314, 2)

print(e)

print(int(e, base=2))
