# Q1:
# numbers = [1, 2, 3, 4, 5, 6, 7]
# sq_list = []
# for i in range(0, len(numbers)):
#     sq = numbers[i] * numbers[i]
#     sq_list.append(sq)
# print(sq_list)

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse()
# for i in range(0, 4):
#     print(list1[i], list2[i])

# list1 = [70, 20, 15, 70, 25, 50, 20]
# for i in range(0, len(list1)):
#     if list1.count(70) > 0:
#         list1.remove(70)
# print(list1)

list1 = [2, -3, 4, 5, 6, -7, 8, 9]
sum = 0
prod = 1
for i in range(0, len(list1)):
    if list1[i] >= 0:
        sum = sum + list1[i]
    elif list1[i] < 0:
        prod = prod * list1[i]
print(f"Total={sum}")
print(f"Product={prod}")

# list1 = [1, 24, "CWS", 45, 678, "INDIA", 987, "XYS"]
# str_count = 0
# int_count = 0
# for i in range(0, len(list1)):
#     if type(list1[i]) == str:
#         str_count = str_count + 1
#     elif type(list1[i]) == int:
#         int_count = int_count + 1
# print(f"Str count={str_count}")
# print(f"Int count={int_count}")

# list1 = [1, 23, 19, 11, 29, 22, 47]
# count = 0
# for i in range(0, len(list1)):
#     for j in range(1, list1[i]):
#         if list1[i] % j == 0:
#             print(list1[i], end=" ")
#             count = count + 1
# print()
# if count == 2:
#     print(list1[i])

# list1 = [1, 29, 11, 47, 45, 78, 89]
# c = []
# for i in list1:
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             c.append(i)
# print(c)

# list1 = [43, 132, 5, 19, 7, 2, 3]
# for num in list1:
#     factors = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors += 1
#     if factors == 2:
#         print(num, end=" ")
