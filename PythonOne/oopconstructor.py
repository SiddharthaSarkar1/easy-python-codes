class Student:
    name = ""
    roll = ""
    gpa = ""
    #This is the constructor------------------
    def __init__(self,name,roll,gpa):
        self.name=name
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"Name = {self.name}, Roll = {self.roll}, Gpa = {self.gpa}")

jordan = Student("Jordan Das",69,5.6)
jordan.display()

std2 = Student("Ananda Dey",12,6.9)
std2.display()