# a = {}
# for i in range(0, 5):
#     sub = input("enter subject")
#     marks = int(input("enter marks"))
#     a[sub] = marks
# print(a)

a = {}
a["name"] = input("enter name: ")
a["gender"] = input("enter gender: ")
a["age"] = int(input("enter age: "))
for i in range(0, 5):
    sub = input("enter subject")
    marks = int(input("enter marks"))
    a[sub] = marks
print(a)
