"""
check whether number is prime number  or not.
"""
num = int(input("enter num: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
        count = count + 1
print()
if count == 2:
    print("It is a prime number")
else:
    print("It is a composite number")

# num = int(input("enter num: "))
# count = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         count = count + 1
# if count == 2:
#     print("It is a prime number")
# else:
#     print("It is a composite number")
