"""
Print total of all the numbers divisible by 5
from 1 to 100 using list comprehension

Count the numbers divisible by 5
"""
a = [i for i in range(1, 101) if i % 5 == 0]
print(sum(a))
print(len(a))

