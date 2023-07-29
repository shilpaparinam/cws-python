# a = {"a": 1, "b": 2, "c": 3}

# a.keys() == list(a.values())
# a.values() == list(a.keys())
# print(a)

#Q2:
a = {"a": 5, "e": 2, "c": 10, "d": 1, "b": 2}
b = {}
c = sorted(list(a.values()))
print(c)
for i in c:
    for k, v in a.items():
        if v == i:
            b.update({k: v})
print(b)
