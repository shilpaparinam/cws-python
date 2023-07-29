# # Open the file in read mode
# f = open("abc.txt", "r")
# # Read all the lines from the file
# lines = f.readlines()
# print(lines)


# # Ask the user to enter a word
# word = input("Enter a word: ")

# # Check if the word exists in the file
# exists = False
# for i in lines:
#     if word in i:
#         exists = True

# if exists:
#     print("Yes")
# else:
#     print("No")


# Open the file in read mode
f = open("abc.txt", "r")
sum = 0
# Read all the lines from the file
for i in f:
    lines = f.readline()
    sum = sum + int(i)
    print(lines)
    print(sum)

# print(lines)
