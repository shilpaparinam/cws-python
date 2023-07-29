"""
print all factors
"""

# n = int(input("enter a number"))
# a = [i for i in range(1, n + 1) if n % i == 0]
# print(a)

"""
print all the prime numbers

"""
n = int(input("enter a number"))
factors = [i for i in range(1, n + 1) if n % i == 0]
print("prime" if len(factors) == 2 else "composite")


a = "Anirudh Khurana"

x = [i for i in a if i in "aeiouAEIOU"]
print(x)
print(len(x))