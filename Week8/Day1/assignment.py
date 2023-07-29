# """
# Q1. Write a Python class named Rectangle with two variables
# length and width. Write a method named area that calculates
# and returns the area of the rectangle.
# """

# class Rectangle:
#     length = 0
#     width = 0

#     def area(self):
#         self.length = int(input("enter length"))
#         self.width = int(input("enter width"))
#         return self.length * self.width

# s1 = Rectangle()
# s2 = s1.area()
# print(s2)

# """
# Q2. Write a Python class named Car with two instance variables
# make and model. Write a method named getMakeModel that
# returns the make and model of the car as a string.
# """


# class Car:
#     make = ""
#     model = ""

#     def getMakeModel(self):
#         self.make = input("enter make of car: ")
#         self.model = input("enter model of car:   ")
#         return self.make, self.model


# s1 = Car()
# s2 = s1.getMakeModel()
# print(s2)

"""
Q3. Write a Python class named BankAccount with two instance
variables balance and accountNumber. Write methods named
deposit and withdraw that allow the user to deposit or withdraw
money from the account.
"""


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.accountNumber = 0

    def deposit(self):
        newAmount = int(input("enter amount to deposit"))
        self.balance = self.balance + newAmount
        print(f"Amount deposited successfully, New Balance is {self.balance}")

    def withdraw(self):
        newAmount = int(input("enter amount to withdraw"))
        self.balance = self.balance - newAmount
        print(f"Amount Withdrawn, new balance is {self.balance}")


s1 = BankAccount()
s1.deposit()
s1.withdraw()
