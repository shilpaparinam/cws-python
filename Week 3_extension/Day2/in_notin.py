a = [45, 3, 65, 45, 123, 65, 3, 65, 45, 2, 3, 5, 65, 3, 7]
num = int(input("enter number: "))
if a.count(num) > 3:
    print("yes")
else:
    print("no")

# if num in a:
#     print("YES")
# else:
#     print("NO")

if num not in a:
    print("it doesnt exist")
else:
    print("it exists")
