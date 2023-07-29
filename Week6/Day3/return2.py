def sumlist(o):
    t = sum(o)
    return t


def check(t):
    if t % 2 == 0:
        print("Even")
    else:
        print("Odd")


p = [10, 20, 30, 40]
r = sumlist(p)
print(r)
check(r)
