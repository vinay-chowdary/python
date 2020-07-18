# variables , Expressions and type conversions

a = 10
b = 5.4
print("addition :", a*b, "\nsubtraction :", a-b, "\nmultiply :", a*b)
print("division :", a/b, "\nmodulus :", a % b, "\npower :", 4**2)
s = "this is vinay chowdary."
print("type of a", type(a), "type of b", type(b))
print(type(s))

# type conversion

b = int(b)
print("converted to int from float", type(b))

# if the string has only digits it can be converted to integer
s = "123"
s = int(s)
s = s+1
print(s)
