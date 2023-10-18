def myname():
    print("Siddhartha Sarkar")

myname()

def add(a,b):
    print(f"Addition of {a} and {b} is : ")
    print(a+b)

add(5,10)

def add1(x,y,z):
    return x+y+z

result=add1(10,20,30)
print("Result is =",result)

def oddEven(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

res=oddEven(7)
print(res)

def fun1(*args):
    print(args)

fun1(1,2,"hello","world")
fun1(1,2,"he","wod","hji","bye")

def student(**std):
    for key,value in std.items():
        print(key,value)


student(id=102,name="Anis")
student(id=103,name="Sourav",clas="IgnouMCA")

lbd = (lambda x : x*x*x)(3)
print(lbd)

import random
rand_num = random.randint(1,10)
print(rand_num)

guess_num = random.random()
print(guess_num)

list1 = ["Siddhartha","Anusri","Kali"]
cho = random.choice(list1)
print(cho)