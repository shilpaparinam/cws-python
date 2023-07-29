# print unique values
a = [45, 3, 65, 45, 123, 65, 3, 65, 45, 2, 3, 5, 65, 3, 7]
b = []
for i in a:
    if i not in b:
        b.append(i)
# print(b)
# print frequency of each value
for i in b:
    count = a.count(i)
    if count > 3:
        print(i)
# print(f"{i} occurs {count} times")
