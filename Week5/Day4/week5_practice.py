"""
Q1. Ask a sentence from the user. Count the number of words in a
sentence using split() method.
"""
# str1 = input("enter a string: ")
# w = str1.split()
# count = 0
# for i in w:
#     count = count + 1
# print(count)

"""
Ask a sentence from the user. Count the number of vowels in
that sentence.
"""
# str1 = input("enter a string: ")
# count = 0
# w = str1.split()
# for i in str1:
#     if i == "a" or i == "e" or i == "o" or i == "i" or i == "u":
#         count = count + 1
# print(f"Total vowel count is {count}")

"""
Write a program to find the longest word in a given string and
print the word.
"""
# str1 = input("enter a string: ")
# long_word = ""
# length = 0
# w = str1.split()
# for i in w:
#     if length < len(i):
#         length = len(i)
#         long_word = i
# print(f"Longest Word ={long_word}")

"""
Write a program to find the shortest word in a given string and
print the word. Make sure that all the words are of different length
in the string.
"""
str1 = "i am shilpa"  # i am shilpa
length = 0
w = str1.split()
short_word = ""
for i in w:
    if length < len(i):
        length = len(w)
        short_word = i
print(f"Shortest Word ={short_word}")
