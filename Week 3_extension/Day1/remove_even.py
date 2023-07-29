a = [41, 2, 3, 443, 21, 24, 656]
even = []
odd = []
for i in range(0, len(a)):
    if a[i] % 2 != 0:
        odd.append(a[i])
    else:
        even.append(a[i])
print(even)
print(odd)
