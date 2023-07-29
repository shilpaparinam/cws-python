a = {"physcis": 45, "chemistry": 66}
# # b = {"maths": 78, "science": 88}
# print(a)

# a["chemistry"] = 78  # if key is not present, it will add a new key and value,
# # if key is already present , it will update the value to the existing key
# a["maths"] = 99
# print(a)
# print(a.get("maths"))
# print(a.values())
# a[5] = 6
# print(a)
# a[6] = 6  # same values can be there for different keys
# # a[6] = 10
# a[6] = 100
# # but for same keys if different values are
# # taken then it will update the value of the key and take the last value updated for the key.
# print(a)

# del a["chemistry"] #key of chemistry inside dict will get deleted
# print(a)

del a  # entire variable a will get deleted
print(a)
