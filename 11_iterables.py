from math import sqrt
from functools import reduce
l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = [7, 8, 9, 10, 11, 12, 13]
it = l1.__iter__()
print(it.__next__(), it.__next__(), it.__next__())

# another way
it = iter(l2)
print(next(it), next(it), next(it))


def isPrime(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return num


lst = list(map(isPrime, l2))

print(lst)

lst = list(filter(isPrime, l2))
print(lst)


D = dict(enumerate(lst))
print(D)

s = {x for x in zip(l1, l2)}
print(s)


def isVowel(letter):
    if letter in "aeiou":
        return True
    else:
        return False


# ******************* map object can be consumed only once

alpha = list(map(chr, range(97, 123)))

f = filter(isVowel, alpha)
print(list(f))
z = dict(zip(alpha, map(ord, alpha)))
print(z)


r = reduce(lambda x, y: x*y, range(1, 6))  # factorial of 5
print(r)

# any(),all(),bool()
