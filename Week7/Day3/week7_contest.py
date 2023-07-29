# r = open("file.txt", "r")

# # s = r.read()
# # print(f"Characters: {len(s)}")
# # y = r.readlines()
# # print(f"Lines: {len(y)}")

# def characters():
#     s = r.read()
#     print(f"Characters: {len(s)}")


# def lines():
#     y = r.readlines()
#     print(f"Lines: {len(y)}")


# # def words():
# x = lines()
# j = characters()


r = input(open("file.txt", "r"))
m = input(r)
n = int(input("enter a num:   "))
s = r.read()
print(f"{s.read()}")
print(f"{s.readline(n)}")
