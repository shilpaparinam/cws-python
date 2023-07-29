# """
# Bank
#     New object create (Constructor)
#         amount=0
#         account_no=randomly
#         name=input
#         bank_name

#     Withdraw
#     Deposit
#     Display
#     DisplayBalance
#     Update
# obj

# """
# import random


# class Bank:
#     def __init__(self):
#         self.amount = 0
#         self.accno = random.randint(100000, 999999)
#         self.name = input("Enter your name = ")
#         self.bankName = input("Enter your bank name = ")

#     def display(self):
#         print(f"\n-------INFO-------")
#         print(f"Account number = {self.accno}")
#         print(f"Balance = {self.amount}")
#         print(f"Name = {self.name}")
#         print(f"Bank name = {self.bankName}")

#     def displayBalance(self):
#         print(f"Your balance = {self.amount}")

#     def deposit(self):
#         newAmount = int(input("Enter amount to deposit = "))
#         self.amount = self.amount + newAmount
#         self.displayBalance()

#     def withdraw(self):
#         newAmount = int(input("Enter amount to withdraw = "))
#         if newAmount > self.amount:
#             print(f"Insufficient balance. Your actual balance is {self.amount}")
#         else:
#             self.amount = self.amount - newAmount
#             self.displayBalance()

#     def update(self):
#         newName = input("Enter new name. Or if you want default leave blank = ")
#         if newName != "":
#             self.name = newName
#         newBankName = input(
#             "Enter new bank name. Or if you want default leave blank = "
#         )
#         if newBankName != "":
#             self.bankName = newBankName


# obj = Bank()
# #obj2 = Bank()
# obj.deposit()
# obj.withdraw()
# obj.update()
# obj.display()
# #obj2.display()


import random


class Bank:
    """This class is used to create a bank object with some functions"""

    def __init__(self):
        self.amount = 0
        self.accno = random.randint(100000, 999999)
        self.name = input("Enter your name = ")
        self.bankName = input("Enter your bank name = ")

    def __str__(self):
        return "You have printed an object directly"

    def display(self):
        print(f"\n-------INFO-------")
        print(f"Account number = {self.accno}")
        print(f"Balance = {self.amount}")
        print(f"Name = {self.name}")
        print(f"Bank name = {self.bankName}")

    def displayBalance(self):
        """This is used to display all balance"""
        print(f"Your balance = {self.amount}")

    def deposit(self):
        """This method is used to deposit money in bank account"""
        newAmount = int(input("Enter amount to deposit = "))
        self.amount = self.amount + newAmount
        self.displayBalance()

    def withdraw(self):
        newAmount = int(input("Enter amount to withdraw = "))
        if newAmount > self.amount:
            print(f"Insufficient balance. Your actual balance is {self.amount}")
        else:
            self.amount = self.amount - newAmount
            self.displayBalance()

    def update(self):
        newName = input("Enter new name. Or if you want default leave blank = ")
        if newName != "":
            self.name = newName
        newBankName = input(
            "Enter new bank name. Or if you want default leave blank = "
        )
        if newBankName != "":
            self.bankName = newBankName


obj = Bank()
accounts = []

while True:
    print("1. Add an account")
    print("2. Print all accounts")
    print("3. Exit")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        obj = Bank()
        accounts.append(obj)
        print(accounts)
    elif choice == 2:
        for i in accounts:
            i.display()
    elif choice == 3:
        acc_no = int(input("enter account number= "))
        for i in accounts:
            if i.accno == acc_no:
                i.display()
                break
        else:
            print("No accounts found")
print(obj)
print(obj.name)
print(obj.amount)
