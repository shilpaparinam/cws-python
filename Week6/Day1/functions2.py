"""
printnumbers()
start number
end number
sum of start to end
"""


def number():
    start_num = int(input("enter start num: "))
    end_num = int(input("enter end number: "))
    sum = 0
    for i in range(start_num, end_num + 1):
        sum = sum + i
    print(f"{sum}")


number()
