"""
ask a number from user, no divisible by 8, count those numbers
"""
# num = int(input("enter one num: "))
# for i in range(1, num + 1):
#     if i % 8 == 0:
#         print(i, end=" ")

num = int(input("enter one num: "))
total = 0
sum = 0
for i in range(1, num + 1):
    if i % 8 == 0:
        total = total + 1
        sum = sum + i
print(total)
print(sum)
