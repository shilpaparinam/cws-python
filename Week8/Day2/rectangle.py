class Rectangle:
    def inputDimension(self):
        self.length = int(input("Enter length: "))
        self.breadth = int(input("Enter breadth: "))

    def area(self):
        # return self.length * self.breadth
        print(f"Area of the rectangle is {self.length*self.breadth}")

    def parameter(self):
        print(f"Parameter of rectangle is {2*(self.length + self.breadth)}")


a = Rectangle()


a.inputDimension()
area = a.area()
# print(area)
a.parameter()
