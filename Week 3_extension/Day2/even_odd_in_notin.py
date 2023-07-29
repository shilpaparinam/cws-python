a = [45, 3, 652, 434, 1236, 65, 3, 65, 45, 2, 3, 5, 65, 3, 7]
even = []
odd = []
for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
