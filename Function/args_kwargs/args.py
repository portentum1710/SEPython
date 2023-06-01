# позиционные аргументы всегда идут в начале
#              СПЕЦСИМВОЛЫ:
# / - все что слева - только позиционные аргументы
# * - все что справа - только keyword аргумент
# **kwargs собирает все keyword аргуметы в словарь
a, *_, c = [1, 2, 3, 4, 5]

def example(a, b, *, c, d):
    print(a)
    print(b)
    print(c)
    print(d)

def my_print(*args, **kwargs):
    print(f"Got keywords: {kwargs}")
    for arg in args:
        print(str(arg), **kwargs)

if __name__ == '__main__':
    #print(*[1, 3, 5, 0])
    #example(1, 2, c=True, d=False)
    my_print(1, 2, 3, 4, 5, sep=":", end="-")
