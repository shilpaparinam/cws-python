# s1 = input("enter a string: ")
# if s1 == s1[::-1]:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")


# s1 = "heart"
# s2 = "earth"
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not an anagram")

s1 = "heart"
s2 = "earth"
k1 = list(s1)
k2 = list(s2)
if k1.sort() == k2.sort():
    print("Anagram")
else:
    print("not anagram")
