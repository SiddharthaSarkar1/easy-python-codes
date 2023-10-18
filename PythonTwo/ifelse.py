num = input("Enter a number : ")
num = int(num)

if num>20:
    print(num,"is greater than 20.")
elif num==20:
    print(num,"is equal to 20.")
else:
    print(num,"is lesser than 20.") 



username = "admin"
password = "1234"

uname = input("Enter username : ")
pw = input("Enter password : ")

if username==uname and password==pw:
    print("Successfully Logged in")
else:
    print("Invalid username and password")