# a = {"physics": 45, "chemistry": 66, "maths": 44}
# b = {}
# for k, v in a.items():
#     b[k] = v + 5
# print(b)

a = {"physics": 45, "chemistry": 18, "maths": 44, "history": 22}
b = {}
for k, v in a.items():
    if a.get(k) > 33:  # if v>33:
        b[k] = "Pass"
    else:
        b[k] = "Fail"
print(b)
