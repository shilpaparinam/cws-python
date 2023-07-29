"""
divisible from 5 between 1 to 100
"""

start = int(input("enter start number"))
end = int(input("enter end number"))
i = start
while i <= end:
    if i % 5 == 0:
        print(i, end=" ")
    i += 1

