# update element at a position

a = [54, 2, 3, 34, 5, 6]
# print(a)
# a[-1] = 100
# print(a)

for i in range(0, len(a)):
    #     if a[i]%2==0:
    #         a[i] = a[i] + 5
    #     else:
    #         a[i]=a[i]+3
    # print(a)

    if a[i] % 2 == 0:
        a[i] = 0

print(a)
