user_string = input("Enter a sentence = ")
# user_string = "aerOPLAne is a good transport"

words = user_string.split()

for i in words:
    if len(i) == 1:
        print(i.upper(), end=" ")
    else:
        print(i[0].upper() + i[1 : len(i) - 1] + i[-1].upper(), end=" ")

"""
# user_string = input("Enter a sentence = ")
user_string = "aeroplane is a transport"
unique_strings = []

for i in user_string:
    if i not in unique_strings:
        unique_strings.append(i)

print(unique_strings)
for i in unique_strings:
    if user_string.count(i) % 2 != 0:
        print(i, end="")


a = "aeroplane_is_a_good_transport"
b = a.split("_")
print(b)

for i in b:
    print(i.capitalize(), end="")
# e = d.title()


a = "aeroplane is a better transport"
# a = input("Enter a string: ")

vowels = ["a", "e", "i", "o", "u"]
result = []
words = ""

for i in a:
    if i.lower() in vowels:
        if len(words)!=0:
            result.append(words)
            words = ""
    else:
        words = words + i

if len(words)!=0:
    result.append(words)

print("Split string on vowels:", result)

"""
