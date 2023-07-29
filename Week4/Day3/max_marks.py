# method1
# l = []
# for i in a.values():
#     l.append(i)
# print(l)
# print(max(l))


# method2
# print(max(a.values()))

a = {"eng": 77, "hindi": 100, "sst": 99, "sci": 55, "comp": 66}
# method3
max_marks = 0
max_marks_subjectname = ""
for k, v in a.items():
    if v > max_marks:
        max_marks = v
        max_marks_subjectname = k

print(f"max marks is {max_marks} of {max_marks_subjectname}")
