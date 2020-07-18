
# special operators is , is not , in
x = 10
fruit = "banana"
banana = "banana"
found = True
none = None
if found is not True:
    print("x is 10")
if none is None:
    print("x is not 10")
if "n" in fruit:
    print("n is in fruit")
if fruit is banana:
    print("yes")


# thia may give syntax error dont use is operator to comapre literal and variable
if "banana" is fruit:
    print("yup")
