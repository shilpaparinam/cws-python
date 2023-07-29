# a = []
# for i in range(0, 10):
#     n = int(input("Enter number: "))
#     a.append(n)
# print(a)
# odd = []
# for i in range(0, 10):
#     if a[i] % 2 != 0:
#         odd.append(a[i])
# print(odd)


# a = [12, 456, 789, 421, 4578]
# a.sort()
# print(f"second smallest number is {a[1]}")


# a = [12, 456, 789, 421, 4578]
# a.sort()
# print(a)
# print(f"second largest number is {a[-2]}")
# print unique values

# a = [45, 3, 65, 45, 123, 65, 3, 65, 45, 2, 3, 5, 65, 3, 7]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# # print(b)
# # print frequency of each value
# for i in b:
#     count = a.count(i)
#     if count > 3:
#         print(i)
# # print(f"{i} occurs {count} times")

# a = [1, 2, 3, 4, 5, 6]
# print(sum(a) / len(a))

# a = [23, 24, 45, 5, 66, 78]
# add = a[1] + a[-2]
# print(add)

# a = [45, 3, 65, 45, 123, 65, 3, 65, 45, 2]
# b = [2, 3, 4, 5, 5]
# b = a.extend(b)
# print(a)
# a.sort()
# a.reverse()
# print(a)

# a = []
# b = []
# for i in range(0, 10):
#     num = int(input("enter num"))
#     a.append(num)
# print(a)
# b = a.copy()
# b.reverse()
# print(b)

a = [1, 2, 3, 4, 6]
if len(a) == 0:
    print("List is empty")
else:
    print("List is not empty")

#https://www.codechef.com/problems/BIRYANI
