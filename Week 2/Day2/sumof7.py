start = int(input("start num"))
end = int(input("end num"))
sum = 0

while start <= end:
    if start % 7 == 0:
        sum = sum + start
    start = start + 1
print(sum)
