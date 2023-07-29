# start_num = int(input("enter start number: "))
# end_num = int(input("enter end number: "))
# i = start_num
# while i <= end_num:
#     print(i, end=" ")
#     i = i + 1

# start_num = int(input("enter start number: "))
# end_num = int(input("enter end number: "))
# i = start_num
# while i <= end_num:
#     if i % 5 == 0 or i % 7 == 0:
#         print(i, end=" ")
#     i = i + 1

# start_num = int(input("enter start number: "))
# end_num = int(input("enter end number: "))
# total = 0
# i = start_num
# while i <= end_num:
#     if i % 4 == 0:
#         total = total + i
#     i = i + 1
# print(f"total sum: {total}")

# num = int(input("Enter any num: "))
# total = num
# i = 1
# while i <= 10:
#     total = num * i
#     print(f"{num} X {i}= {total}")
#     i = i + 1


# i = 20
# count = 0
# while i <= 70:
#     if i % 4 == 0:
#         count = count + 1
#     i = i + 1
# print(f"Count= {count}")

num = int(input("Enter one num: "))
fact = 1
while num > 1:
    fact = fact * num
    num = num - 1
print(fact)
