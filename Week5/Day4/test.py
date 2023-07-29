# user_string = "aeroplane is a good mode of transport good bye ok done"
# words = user_string.split()
# print(words)

# # for i in range(0, len(words), 2):
# #     print(words[i], end=" ")

# for i in words[::2]:
#     print(i, end=" ")

user_string = "aeroplane is a good mode of transport good bye ok done"
words = user_string.split()[::-1]
print(words)
for i in words:
    j = print(i[::-1], end=" ")
