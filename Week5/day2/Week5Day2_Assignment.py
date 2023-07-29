"""
Q1. Write a Python program to check if a string has at least one
letter and one number. If it has at least one letter and one number
then print YES else print NO.
"""

n = input("enter a string:  ")
count_char = 0
count_int = 0
for i in range(0, len(n)):
    if n[i].isalpha():
        count_char += 1
    elif n[i].isdigit():
        count_int += 1
if count_int > 0 and count_char > 0:
    print("Yes")
else:
    print("No")

# user_string = input("Enter a sentence = ")

# isLetter = False
# isNumber = False

# for i in user_string:
#     if i.isdigit():
#         isNumber = True
#     elif i.isalpha():
#         isLetter = True

# if isNumber == True and isLetter == True:
#     print("Both number and letter exists")
# else:
#     print("Both number and letter does exists")


# for i in n:
#     if n.isalpha() and n.isdigit():
#         print("yes")
#     else:
#         print("no")
# for i in n:
#     if 97 > ord(n[i]) > 122 and 48 > ord(n[i]) > 57:
#         print("yes")
#     else:
#         print("no")


# """
# Q2:Write a python program to ask a string from user. Then count
# the number of vowels and number of consonants in that string.
# (Make sure there are no spaces in string when you enter in
# terminal).
# """
# n = input("enter a string:  ")
# count_v = 0
# count_c = 0
# for i in range(0, len(n)):
#     if n[i] == "a" or n[i] == "e" or n[i] == "i" or n[i] == "o" or n[i] == "u":
#         count_v += 1
#     else:
#         count_c += 1
# print(f"total vowels are {count_v}")
# print(f"total consonants are {count_c}")


"""
Q3. Write a python program to remove all the duplicates from the
string entered by user.
"""
# n = input("enter a string:  ")
# y = set(n)
# b = "".join(i for i in y)
# print(b)

# """
# Q4. Ask a string from user. Print the string with first 2 letters and
# last 2 letters.
# """
# n = input("enter a string:  ")
# print(n[0:2] + n[7:9])

"""
Q5. Write a python program to only print second half of the string.
Ask string from user.
"""

# n = input("enter a string:  ")
# if len(n) % 2 == 0:
#     n2 = len(n) // 2
# elif len(n) % 2 != 0:
#     n2 = (len(n) // 2) + 1
# print(n[n2:])
