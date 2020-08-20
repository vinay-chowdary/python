# let's create calculator app by handling tracebacks
try:
    num1 = int(input("enter first number "))
    num2 = int(input("enter second number "))
except:
    print("invalid number!")
    quit()
try:
    operator = int(
        input("1.addition\n2.subtraction\n3.multiply\n4.divide\n5.modulus\n6.power\n"))
except:
    print("enter numerical input")
if operator in (1, 2, 3, 4, 5, 6):
    if operator == 1:
        print(num1+num2)
    elif operator == 2:
        print(num1-num2)
    elif operator == 3:
        print(num1*num2)
    elif operator == 4:
        print(num1/num2)
    elif operator == 5:
        print(num1 % num2)
    elif operator == 6:
        print(num1**num2)
else:
    print("invalid input")
