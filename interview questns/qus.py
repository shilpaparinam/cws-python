# mirafra 1st round
# sum of 2 numbers
# l1 = [3, 2, 1, 6]
# k = 5
# for i in range(0, len(l1) - 1):
#     if l1[i] + l1[i + 1] == k:
#         print(l1[i], l1[i + 1])

# mirafra 2nd round
# count the occurences of max used character
s1 = "helloworld"
count = 0
s2 = sorted(s1)
s3 = set(s1)
for i in s3:
    # if s2[i] == i:
    #     count = count + 1
    print(f"{i} count is {s2.count(i)}", end=" ")
    print()
    if s2.count(i) >= 0:
        count = count + 1
        print(f"max count is {i} = {count}")

# define inheritance, explain with example
# class parentName:
#     name = "xyz"
#     age = 45
#     gender = M


# class childName(parentName):
#     name = "abc"
#     age = 5
#     gender = F


# # how is split used, explain with example
# s1 = "hihellogoodmorning"
# s2 = s1.split("h")
# print(s2)

# # str="i am in hyderabad"
# # o/p: "hyderabad in am i"
