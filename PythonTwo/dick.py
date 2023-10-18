student = {"Name" : "Siddhartha", "Roll no" : "1", "Subject" : "Computer Science", "Class" : "3rd year"}
print(student)
print(student["Name"])
print(student["Roll no"])
print(student["Subject"])
print(student["Class"])
print(student.keys())
print(student.items())

Cstd = student.copy()
print(Cstd)

ddstudent = {"name":"Sourav", "roll":"77", "subject":{"sub1":"math", "sub2":"physics" ,"sub3":"computer"}, "class":"1st year"}
print(ddstudent)
print(ddstudent["subject"]["sub2"])