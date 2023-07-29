"""
write a function which return addition of 2 values

check if sum is even or odd

"""


def addition(n1, n2):
    return n1 + n2


def check(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


x = addition(10, 25)
check(x)
