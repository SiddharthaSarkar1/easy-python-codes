num1=100
num2=45

print(num1 if num1<num2 else num2)

#using and
a=100
b=20
c=30

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


ch = 'a'
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("vowel")
else:
    print("Consonant")


nm=1
while nm <= 10:
    print(nm)
    nm=nm+1
print("End")


i=1
while i<50:
    if i%2==0:
        print(i)
    i=i+1
print("End")

ii=1
while ii<50:
    if ii%2!=0:
        print(ii)
    ii=ii+1
print("End")

#Sum of n numbers
# n=int(input("Enter the number upto you want sum : "))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)

import math
print("Factorial is:")
print(math.factorial(5))