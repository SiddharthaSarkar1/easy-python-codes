class Shape:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2

    def area(self):
        print("I am the area method of shape class.")

class Triangle(Shape):

    def area(self):
        area = 0.5*self.dim1*self.dim2
        print("Area of the triangle is",area)

class Rectangle(Shape):
    def area(self):
        area = self.dim1*self.dim2
        print("Area of the rectangle is",area)


t1=Triangle(4,5)
t1.area()

r1=Rectangle(20,10)
r1.area()