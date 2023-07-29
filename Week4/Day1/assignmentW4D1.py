# Q1:
# a = (2, 3, 4, 5, 6)
# l1 = list(a)
# print(l1[-4])

# Q2:
# a = (2, 3, 3, 2, 4, 4, 4, 5, 6, 7, 8)
# b = []
# for i in range(0, len(a)):
#     if a.count(i) > 1:
#         b.append(a[i])
# print(set(b))

# Q3:
# a = (2, 3, 4, 5, 6)
# b = int(input("enter an element"))
# if b in a:
#     print("element exists")
# else:
#     print("Element doesnt exist")

# Q4:
# a = (2, 3, 4, 5, 6, 65, 76, 77)
# b = list(a)
# b.remove(65)
# print(tuple(b))

# # Q5:
# a = (2, 3, 4, 5, 6, 65, 76, 77, 44, 33)
# b = list(a)
# b.reverse()
# print(tuple(b))


a = {2, 3, 4, 5, 6, 7, 8655}
b = {2, 4, 55, 876, 8655, 432}
print(a.union(b))
print(a.intersection(b))
