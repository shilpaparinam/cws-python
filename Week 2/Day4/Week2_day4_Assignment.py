# # a
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()  # it will leave 1 line

# # b
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end=" ")
#     print()  # it will leave 1 line

# c
count = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(count, end=" ")
        count = count + 1
    print()  # it will leave 1 line
