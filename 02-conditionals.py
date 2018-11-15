# A conditional is a construct that allows you to branch your code based on conditions being met (or not).
a = 2

if a < 5:
    print("a < 5")
else:
    print("a >= 5")

# "if" statements can be nested.
a = 8

if a < 5:
    print("a < 5")
else:
    if a < 10:
        print("5 <= a < 10")
    else:
        print("a >= 10")

# "elif" statements provide far better readability.
a = 5

if a < 5:
    print("a < 5")
elif a < 10:
    print("5 <= a < 10")
elif a < 15:
    print("10 <= a < 15")
elif a < 20:
    print("15 <= a < 20")
else:
    print("a > 20")

# Python also provides a conditional expression (ternary operator) that works like this: "X if (condition) else Y".
a = 5

b = "a < 5" if a < 5 else "a >= 5"
print(b)


# X and Y can be any expression, not just literal values.
def say_hello():
    print("Hello!")


def say_goodbye():
    print("Goodbye!")


a = 5

say_hello() if a < 10 else say_goodbye()

a = 15

say_hello() if a < 10 else say_goodbye()
