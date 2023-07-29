# # num1 = int(input("Enter 1 num: "))
# if num1 % 3 == 0:
#     print("Number is divisible by 3")
# else:
#     print("Number is not divisible by 3")


# num1 = int(input("Enter 1 num: "))
# if num1 % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

# len = int(input("Enter len: "))
# width = int(input("Enter width: "))
# if len == width:
#     print("It is a square")
# else:
#     print("It is not a square")
#

# tot_class = int(input("Enter no of classes held"))
# class_att = int(input("enter no of classes attended"))
# percent = (class_att / tot_class) * 100
# print(f"Student Attendance is : {percent} ")
# if percent < 75:
#     print("Person is not allowed to sit in the exam")
# elif percent > 75 and percent <= 100:
#     print("Person is allowed to sit in the exam")
# else:
#     print("Invalid input")


# marks = int(input("enter marks: "))
# if marks >= 80:
#     print("Grade= A")
# elif marks > 60 and marks < 80:
#     print("Grade= B")
# elif marks > 50 and marks < 60:
#     print("Grade = C")
# elif marks > 45 and marks < 50:
#     print("Grade = D")
# elif marks > 25 and marks < 45:
#     print("Grade= E")
# elif marks > 0 and marks < 25:
#     print("Grade = F")
# else:
#     print("Invalid input")


s = input("enter one string: ")
if s == s[::-1]:
    print("it is palindrome")
else:
    print("it is not a palindrome")
