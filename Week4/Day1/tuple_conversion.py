a = (12, 321, 34, 56, 66)
print(a, type(a))
b = list(a)
print(b, type(b))
b.append(233)
a = tuple(b)
print(a, type(a))