class Student:
    name = ""
    roll = ""
    gpa = ""

    def display(self):
        print(f"Name = {self.name}, Roll = {self.roll}, GPA = {self.gpa}")

    def setValue(self,name,roll,gpa):
        self.name=name
        self.roll=roll
        self.gpa=gpa


rahim = Student()
rahim.setValue("Rahim Banerjee",26,4.9)
rahim.display()


subrata = Student()
subrata.setValue("Subrata saha",69,6.8)
subrata.display()

