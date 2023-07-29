set1 = {43, 42, 345, 33, 56}
set2 = {43, 22, 45, 56, 368}
# result = set1.union(set2)
# print(result)

# result = set2.intersection(set1)
# print(result)

# set1.add(1000)
# print(set1)
# set1.remove(56)
# print(set1)

a = {43, 42, 345, 33, 56}
b = {43, 22, 45, 56, 368}
result = list(set(a).intersection(set(b)))
print(result)
