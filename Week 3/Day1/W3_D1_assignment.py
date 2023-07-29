# 1
l1 = [12, 3, 4, 5, 642, 245, 4, "shshs"]
print(len(l1))

# 2
l1 = [12, 3, 4, 5, 642, 245, 4, "shshs"]
if len(l1) % 2 == 0:
    print("List is even")
else:
    print("list is odd")

# 3
l1 = [12, 3, 4, 5, 62, 245, 4, "shshs"]
sum = 0
for i in range(0, len(l1) - 1):
    if l1[i] % 3 == 0:
        sum = sum + l1[i]
print(f"sum is {sum}")

# 4
l1 = [12, 3, 4, 0, -12, -23]
count_even = 0
count_odd = 0
for i in range(0, len(l1)):
    if l1[i] >= 0:
        count_even = count_even + 1
    elif l1[i] < 0:
        count_odd = count_odd + 1
print(f"positive no={count_even}")
print(f"negative no={count_odd}")

# 5
l = [1, 3, 4, 5, 68, 89]
l = l[::-1]
print(l)

# 6
my_list = [45, 12, 59, 60, 47, 3412, 3111]
for i in range(0, len(my_list)):
    if i % 2 == 0:
        print(my_list[i], end=" ")
