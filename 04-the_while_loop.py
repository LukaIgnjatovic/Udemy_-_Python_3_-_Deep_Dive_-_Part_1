# "while" loop will do something while an expression evaluation equals to true.
i = 0

while i < 5:
    print(i)
    i += 1

# Behaviour of "do-while" concept can be emulated as well. This construct ensures that the code block inside "while" loop executes at least once.
i = 5

while True:
    print(i)
    if i >= 5:
        break
        print("Something.")

# "break" statement can break out of the "while" loop.
min_length = 2

while True:
    name = input("Please enter your name: ")
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break

print("Hello, {0}.".format(name))

# "continue" statement allows for "while" loop to continue executing even if the condition in "if" statement is not met.
a = 0

while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

# "else" can be used with "while" loop if the loop did not end with a "break".
# Classic approach.
l = [1, 2, 3]
val = 10

found = False
idx = 0

while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1

if not found:
    l.append(val)

print(l)

# "else" approach.
l = [1, 2, 3]
val = 10

idx = 0

while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)

print(l)
