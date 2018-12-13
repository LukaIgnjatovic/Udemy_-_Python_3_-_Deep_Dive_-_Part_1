# Peephole optimizations occur at compile time.
# For example, constant expressions like numeric calculations that do not contain variables are pre-calculated and stored in memory.
# Also, short sequences with length less than 20 are treated the same.

# "string" and "time" libraries are required for final examples in this script.
import string
import time


# "my_func" is going to check for peephole optimizations at compile time for different variables.
def my_func():
    # "a" is treated as a constant.
    a = 24 * 60
    # "b" is considered a short sequence.
    b = (1, 2) * 6
    # "c" is considered a short sequence.
    c = "abc" * 3
    # "d"'s length exceeds 20.
    d = "ab" * 11
    # "e"'s length exceeds 20.
    e = "the quick brown fox" * 5
    # "f" is a list and its type is mutable, so it cannot be pre-calculated and stored in memory.
    f = ["a", "b"] * 3


# Values of "a", "b" and "c" are pre-calculated and stored in memory since they meet aforementioned requirements.
my_func.__code__.co_consts

# Another type of peephole optimizations are membership tests.
# This means that mutable structures are replaced by their immutable counterparts.
# List is converted to tuple and set is converted to frozenset.
# On a side note, set membership is much faster than list or tuple membership (sets are basically like dictionaries).


# "my_func" is going to show how a list is being converted to a tuple.
def my_func_list_to_tuple(e):
    if e in [1, 2, 3]:
        pass


print(my_func_list_to_tuple.__code__.co_consts)


# "my_func" is going to show how a set is being converted to a frozenset.
def my_func_set_to_frozenset(e):
    if e in {1, 2, 3}:
        pass


print(my_func_list_to_tuple.__code__.co_consts)

# "ascii_letters" from "string" library contains all the upper and lowercase characters of ASCII encoding.
print(string.ascii_letters)

# "char_list" variable is going to contain all ASCII characters in a list.
char_list = list(string.ascii_letters)

# "char_tuple" variable is going to contain all ASCII characters in a tuple.
char_tuple = tuple(string.ascii_letters)

# "char_set" variable is going to contain all ASCII characters in a set.
char_set = set(string.ascii_letters)

# "char_list" and "char_tuple" are ordered in the same way as "print(string.ascii_letters)" statement has executed.
print(char_list)

print(char_tuple)

# However, "char_set" do not have a particular order.
print(char_set)


# Now it is time to check the time of execution needed for each of these data types.
def membership_test(n, container):
    for i in range(n):
        if "z" in container:
            pass


# "start" is going to store the time when execution has started using "perf_counter()" method from "time" library.
start = time.perf_counter()

# Function "membership_test" is going to be executed 10 million times on "char_list" list.
membership_test(10000000, char_list)

# "end" is going to store the time when execution has ended.
end = time.perf_counter()

# Printing the difference between "start" and "end" is going to show how much time was needed to execute "membership_test".
print("Time needed to execute 10 million loops using list is", end - start, "seconds.")

start = time.perf_counter()

membership_test(10000000, char_tuple)

end = time.perf_counter()

print("Time needed to execute 10 million loops using tuple is", end - start, "seconds.")

start = time.perf_counter()

membership_test(10000000, char_set)

end = time.perf_counter()

print("Time needed to execute 10 million loops using set is", end - start, "seconds.")
# As expected, checking for set membership is much faster.
