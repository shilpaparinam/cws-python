a = [12, 43, 45, 33, 56, 78]

# for i in range(0, len(a)):
#     if a[i] % 2 == 0:
#         print(a[i])

for i in range(0, len(a)):
    if a[i] % 4 == 0 and a[i] % 3 == 0:
        print(a[i])
