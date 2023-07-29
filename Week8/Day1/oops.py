class Student:  # Class
    name = ""
    age = 0
    gender = ""

    #
    def greet(self):
        print(f"your name is {self.name}")
        print(f"your age is {self.age}")
        print(f"your gender is {self.gender}")

    def getData(self):
        self.name = input("Enter name:    ")
        self.age = input("enter age:  ")
        self.gender = input("enter gender:    ")


s1 = Student()
s2 = Student()
s3 = Student()
s2.name = "sumedha"
s2.age = 3
s2.gender = "female"
s1.getData()
s1.greet()
s2.getData()
s2.greet()


"""
Rectangle - Class

inputDimension()
    Ask user - Length, Breadth

area()
    print Area

parameter()
    print parameter


a,b,c
r1,r2,r3
"""
