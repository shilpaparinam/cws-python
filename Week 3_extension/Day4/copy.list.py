a = [43, 32, 154, 654, 76, 78687, 32]
b = a.copy()
print(id(a))
print(id(b))
print(a)
print(b)
a[3] = 1000
a = [500]  # 500 address
b = a
# b=500

print(a)
print(b)

# a = [99, 33]  # 300
a[3] = 100
print(a)
print(b)
