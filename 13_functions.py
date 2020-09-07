def fun(num1, num2, operator):
    print(num1, operator, num2)


fun(1, 2, "+")

print(max(1, 2, 3, 65, 4, 3, 49, 5))

# in a string min and max is based on ASCII value
print(max("Hello hO"))

# smallest is space
print(min("Hello hO"))

# small among true and false
print(min(True, False))

# default arguments


def computepay(h=0, r=0):
    if h > 40:
        return ((h-40)*r*1.5)+40*r
    else:
        return h*r


try:
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
except:
    print("error")

# named arguments
p = computepay(r=rate, h=hrs)
print("Pay", p)
