# a = {
#     "sagar": [67, 74, 32, 12, 44],
#     "sanjay": [76, 32, 12, 34, 33],
#     "akul": [76, 88, 32, 4, 56],
# }

# for k, v in a.items():
#     print(k)
#     for i in v[::-1]:
#         print(i)


# for k, v in a.items():
# print(f"{k} scored {sum(v)} marks")


# for k,v in a.items():
#     max_marks=0
#     for m in v:
#         if m>max_marks:
#             max_marks=m
#             print(f"name -> {k} and max marks->{max_marks} ")


# print(list(a.values()))
# print(a)
# print(max(a.values()))


# print max marks in all the student marks
# result = []
# for k, v in a.items():
#     result.extend(v)
# print(max(result))

#print max marks and name
a = {
    "sagar": [67, 74, 35, 12, 94],
    "sanjay": [78, 32, 2, 34, 33],
    "akul": [76, 88, 31, 4, 56],
}
result = []
for k, v in a.items():
    result.extend(v)
max_marks = max(result)
for k, v in a.items():
    if max_marks in v:
        print(k, max_marks)
