start = int(input("enter start num"))
end = int(input("enter end num"))
if start <= end:
    while start <= end:
        if start % 5 == 0 and start % 6 == 0:
            print(start, end=" ")
        start = start + 1
else:
    while start >= end:
        if start % 5 == 0 and start % 6 == 0:
            print(start, end=" ")
        start = start - 1
