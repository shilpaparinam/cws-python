# Q1:
# n = int(input("enter a number: "))
# b = {}
# for i in range(1, n + 1):
#     if b.items() != None:
#         b[i] = i * i
#         b.update()
# print(b)


# a = {}
# if a.items() == None:
#     print("dict is empty")
# else:
#     print("it is not empty")

# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}
# d3 = {}
# d3.update(d2)
# d3.update(d1)
# for i in d1:
#     if i in d2.keys():
#         d3[i] = d1[i] + d2[i]
# print(d3)

# d1 = {1: 2, 3: 4, 5: 6}
# l = list(d1.keys())
# if len(l) == 0:
#     print("Size is 0")
# else:
#     print(d1.items())

d1 = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 7: 60, 8: 50}
for i in range(0, 9):
    if d1.get(i) != 1:
        d1.popitem()
print(d1)
