class Student:
    def __init__(self, n, a, g):
        print("Contructor is called")

        # self.name = input("enter name")
        # self.age = input("enter age")
        # self.gender = input("enter gender")

        self.name = n
        self.age = a
        self.gender = g

    def greet(self):
        print(f"Your name is {self.name}")
        print(f"Your age is {self.age}")
        print(f"Your gender is {self.gender}")

    # def getData(self):
    # self.name = input("enter name")
    # self.age = input("enter age")
    # self.gender = input("enter gender")
    # self.city = "Surat"


s1 = Student("shilpa", 31, "female")
s2 = Student("sumedha", 3, "female")
# s1.getData("shilpa", 31, "female")
# s1.getData()
# s2.getData()
s1.greet()
s2.greet()
