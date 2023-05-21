def mult(z, y):
    if type(z) == str and z.isdigit():
        z = int(z)
    if type(y) == str and y.isdigit():
        y = int(y)
    if type(z) not in [int, float] or type(y) not in [int, float]:
        raise TypeError
    return z * y
print(mult(2, 7))
print(mult(2.5, 7.12))
print(mult("8", 3))

print(mult(4.5, 0.6).__round__(2))

