try:
    list=[20,0,10]
    result = list[0]/list[1]
    print(result)
    print("Done")

except ZeroDivisionError as ze:
    print(ze)
    print("Division by zero is not possible")

except IndexError as ie:
    print(ie)
    print("Index Error")

finally:
    print("Successful")



#swapping

a=20
b=10

a,b=b,a
print("a =",a,",","b =",b)
#--------------------------------------------------------------------------------

try:
    val1 = int(input("Enter first number : "))
    val2 = int(input("Enter second number : "))

    result=val1/val2
    print(result)

except ValueError as ve:
    print(ve)
    print("VALUE ERROR")

except ZeroDivisionError as zde:
    print(zde)
    print("ZERO DIVISION ERROR")
finally:
    print("Thanx!!")