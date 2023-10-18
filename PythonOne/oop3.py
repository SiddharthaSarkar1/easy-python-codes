class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def calcu(self):
        area=0.5*self.base*self.height
        print("Triangle area is =",area)

tri1 = Triangle(4,5)
tri1.calcu()