# lambda functions
# return addition of 2 numbers
# return addition of 5 numbers
# return sum of a list

x = lambda n1, n2: n1 + n2
print(x(10, 20))  # or y=x(10,20)     print(y)

addition_5 = lambda n1, n2, n3, n4, n5: n1 + n2 + n3 + n4 + n5
x = addition_5(1, 2, 3, 4, 5)
print(x)

sum_lst = lambda lst: sum(lst)
print(sum_lst([10, 20, 30, 40]))
