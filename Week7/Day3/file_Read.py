"""
3 Types of mode to open a file:
    1. Read
    2. Write
    3. Append
"""
f = open("abc.txt", "r")
d = f.read()
print(d)
f.close()
