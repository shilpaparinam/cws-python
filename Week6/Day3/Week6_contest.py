"""
Q1. Write a function called list_average(lst) that takes a list of
numbers lst as a parameter and returns the average of the
numbers in the list.
"""

# def list_average(lst):
#     numbers = sum(lst) / 6
#     return numbers

# average = list_average([10, 20, 30, 40, 50, 60])
# print(average)


# """
# Write a function called dictionary_value_sum(d) that takes a
# dictionary d as a parameter, where the values are numbers, and
# returns the sum of all the values in the dictionary.

# """


def dictionary_value_sum(d):
    dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    items = list(dict.values())
    d = sum(items)
    return d


sum_items = dictionary_value_sum({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
print(sum_items)


# """
# Q3. Write a function called filter_even_numbers(lst) that takes a
# list of integers lst as a parameter and returns a new list containing
# only the even integers from the input list.

# """
# def filter_even_numbers(lst):
#     l1 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#     l2 = []
#     for i in range(0, len(l1)):
#         if l1[i] % 2 == 0:
#             l2.append(l1[i])
#     return l2


# even_num = filter_even_numbers([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
# print(even_num)


# """
# Q4. Write a function called union_of_sets(set_a, set_b) that
# takes two sets set_a and set_b as parameters and returns a new
# set containing the union of the two input sets.
# """
# def union_of_sets(set_a, set_b):
#     set_a = {1, 2, 3}
#     set_b = {3, 4, 5}
#     union_set = set_a.union(set_b)
#     return union_set

# x = union_of_sets({1, 2, 3}, {3, 4, 5})
# print(x)


"""
Q5. Write a function called is_palindrome(s) that takes a string s
as a parameter and returns True if the string is a palindrome
(reads the same forward and backward), otherwise False.

"""


# def is_palindrome(s):
#     str = input("Enter a str: ")
#     if str == str[::-1]:
#         return True
#     else:
#         return False


# palin = is_palindrome("")
# print(palin)


"""
Q6. Write a function called get_factors(n) that takes an integer n
as a parameter and returns a list of its factors, excluding 1 and the
number itself.
"""


# def get_factors(n):
#     n1 = int(input("Enter a no:   "))
#     l1 = []
#     for i in range(2, n1 - 1):
#         if n1 % i == 0:
#             l1.append(n1 // i)
#             i += 1
#     return l1


# x = get_factors(6)
# print(x)
