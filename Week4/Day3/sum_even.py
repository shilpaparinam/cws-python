"""
make a dict for 5 subjects
calculate the sum of even marks

"""
a = {"eng": 77, "hindi": 88, "sst": 99, "sci": 55, "comp": 66}
total = 0
for m in a.values():
    if m % 2 == 0:
        total = total + m
print(total)
