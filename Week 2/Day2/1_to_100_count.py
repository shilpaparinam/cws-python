# i = 1
# total = 0
# while i <= 100:
#     if i % 11 == 0:
#         total = total + 1
#     i = i + 1
# print(total)

"""
Ask a number from user = 

54653
Count the number of digits = 5

122111
Count the number of digits = 6

//
"""

num = int(input("enter the number"))
count = 1
while num // 10 != 0:
    count = count + 1
    num = num / 10
print(count)
