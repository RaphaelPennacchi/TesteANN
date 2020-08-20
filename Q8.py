import math


def F1(x0, h, f):
    return (f(x0) - f(x0 - h)) / h


def F2(x0, h, f):
    return (f(x0 + h) - f(x0 - h)) / 2*h


def F3(x0, h, f):
    return (f(x0 - 2*h) - 8*f(x0 - h) + 8*f(x0 + h) - f(x0 + 2*h)) / (12 * h)


hs = [.1, .05, .025, .0125]

x0 = 1  # p


def f1(x):
    return math.cos(x**x)


def f2(x):
    return math.sin(x)


def f3(x):
    return x**math.cos(x)


def f4(x):
    return math.exp(-x**2)


print('1)')

for h in hs:
    print('aprox F1 com h =', h)
    print(F1(x0, h, f1))
print()
for h in hs:
    print('aprox F2 com h =', h)
    print(F2(x0, h, f1))
print()
for h in hs:
    print('aprox F3 com h =', h)
    print(F3(x0, h, f1))

print('\n2)')

for h in hs:
    print('aprox F1 com h =', h)
    print(F1(x0, h, f2))
print()
for h in hs:
    print('aprox F2 com h =', h)
    print(F2(x0, h, f2))
print()
for h in hs:
    print('aprox F3 com h =', h)
    print(F3(x0, h, f2))

print('\n3)')

for h in hs:
    print('aprox F1 com h =', h)
    print(F1(x0, h, f3))
print()
for h in hs:
    print('aprox F2 com h =', h)
    print(F2(x0, h, f3))
print()
for h in hs:
    print('aprox F3 com h =', h)
    print(F3(x0, h, f3))

print('\n4)')

for h in hs:
    print('aprox F1 com h =', h)
    print(F1(x0, h, f4))
print()
for h in hs:
    print('aprox F2 com h =', h)
    print(F2(x0, h, f4))
print()
for h in hs:
    print('aprox F3 com h =', h)
    print(F3(x0, h, f4))

# import sympy as sy

# x = sy.Symbol('x')
# string = 'x ** x'
# f = sy.sympify(string)
# df = sy.diff(f, x, 2).subs(x, x0)
# print('exact:', df.evalf())
