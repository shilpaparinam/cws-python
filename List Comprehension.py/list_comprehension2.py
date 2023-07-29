# a = [b for b in range(1, 101)]
# print(a)

# a = [i % 2 for i in range(1, 15)]
# print(a)

# a = ["even" if i % 2 == 0 else "odd" for i in range(1, 10)]
# print(a)

# a = [
#     "Hi" if i % 2 == 0 else "Bye"
#     for i in range(int(input("enter start number")), int(input("enter end number")) + 1)
# ]
# print(a)

# print(sum([i for i in range(1, 11)]))


a = [i + 10 for i in range(1, 11) if i % 2 == 0]
print(a)
