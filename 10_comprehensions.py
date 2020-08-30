# List comprehension
L1 = [10, 20, 30, 40]
L2 = [x+5 for x in L1]
L3 = [x+5 for x in range(10, 50, 10)]
s = "Think Merit, Think Transparency, Think SASTRA"
L4 = [x for x in s.split(',')]
L5 = [x.strip() for x in s.split(',')]
L6 = [x.strip().upper() for x in s.split(',')]
L7 = [x for x in range(50) if x % 2 == 0]
print(L1, L2, L3, L4, L5, L6, L7, sep="\n")

# set comprehension
S1 = {10, 20, 30, 40}
S2 = {x+5 for x in L1}
S3 = {x+5 for x in range(10, 50, 10)}
S4 = {x for x in s.split(',')}
S5 = {x.strip() for x in s.split(',')}
S6 = {x.strip().upper() for x in s.split(',')}
S7 = {x for x in range(50) if x % 2 == 0}
print(S1, S2, S3, S4, S5, S6, S7, sep="\n")


# dictionary comprehension
L1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
D1 = {x: ord(x) for x in L1}
D2 = {x: x**2 for x in range(1, 11)}
L1 = [(x, ord(x)) for x in 'abcdefghijklmnopqrstuvwxyz']
# D3 = {x: y for (x, y) in L1}
D3 = {x: y for x, y in L1}
L1 = [['Joe', 48], ['Kim', 32], ['Raja', 25], ['Ajai', 60]]
# D4 = {a: b for [a, b] in L1}
D4 = {a: b for a, b in L1}
print(D1, D2, D3, D4, sep="\n")


# tuple comprehension
D1 = {'Joe': 48, 'Kim': 32, 'Raja': 25, 'Ajai': 60}
T1 = tuple(D1.items())
T2 = tuple((x.upper(), y) for x, y in D1.items())
L1 = [1, 2, 3, 4]
L2 = [10, 20]
T3 = tuple((x, y, x*y) for x in L1 for y in L2)
print(T1, T2, T3, sep="\n")


# assignment 2
l = [[2, 3, 5, 1, 8], [4, 1, 2, 6, 1], [6, 4, 5, 7, 9]]
# o = [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
transpose = [[row[i] for row in l]for i in [0, 1, 2, 3, 4]]
# print(o)
s = "string is a string is a string"
d = {x: s.count(x) for x in s}
print(d)
print(transpose)
