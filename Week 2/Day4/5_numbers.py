"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    # print("\n")  # it will leave 2 lines
    print()  # it will leave 1 line
