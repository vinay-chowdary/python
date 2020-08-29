num1 = 12345.6789
print("{: .2f}".format(num1))
print("{: .4f}".format(num1))
print("{:,.2f}".format(num1))
print("{: 15,.2f}".format(num1))


num2 = 12345
print("{: d}".format(num2))
print("{: ,d}".format(num2))


num3 = 0.12345
print("{:.0%}".format(num3))
print("{:.1%}".format(num3))


num4 = 12345.6789
print("{:.2e}".format(num4))
print("{:.4e}".format(num4))

# > is right justify
print("{:15} {:>10} {:>5}".format("Description", "Price", "Qty"))
print("{:15} {:>10.2f} {:>5d}".format("Hammer", 9.99, 3))
print("{:15} {:>10.2f} {:>5d}".format("Nails", 14.50, 10))


######### formatting strings #########

f1 = '%s, eggs, and %s' % ('spam', 'SPAM!')
f2 = '{0}, eggs, and {1}'.format('spam', 'SPAM!')
# numbers are optional from python 3.1+
f3 = '{}, eggs, and {}'.format('spam', 'SPAM!')
print(f1, f2, f3, sep=" == ")
print('{:,.2f}'.format(296999.2567))
print('%.2f | %+10d' % (3.14159, -42))

# TODO:locale module
