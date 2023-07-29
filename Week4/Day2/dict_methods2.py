# a = {"name": "Shilpa", "age": 66, "gender": "F"}
# r = a.keys()
# for i in r:
#     # for i in a.keys():
#     # print(a[i])
#     # print(i)
#     print(i, a[i])

# print(a.values())

a = {"physics": 45, "chemistry": 66, "maths": 44}
total = 0
# b = a.values()
for i in a.values():
    total = total + i
print(total)

a = {"physics": 44, "chemistry": 66, "maths": 88}
# for k, v in a.items():
#     print(f"Marks in {k} is {v}")

# for k in a.keys():
#     print(f"marks in {k} is {a[k]}")

# total = 0
# for v in a.values():
#     total = total + v
# print(total)
