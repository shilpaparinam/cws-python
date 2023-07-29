a = {"name": "Shilpa", "age": 66, "gender": "F"}
# a["name"] = "ssjsjsjs"

a.update({"address": "hyd", "country": "india", "pincode": 333232})
# print(a)


# del a["pincode"]
# print(a)
# a.pop("country")
# print(a)

# print(a.get("address"))

"""
enter a key from user, delete that key
"""
# keyname = input("enter key you want to delete")
# if a.get(keyname) != None:
#     a.pop(keyname)
# else:
#     print("key doesnt exist")
# print(a)

for i in a:
    print(i)
