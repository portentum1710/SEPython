def usm(*args):
    total = 0
    string = ""
    if type(args[0]) == int:
        for num in args:
            total += int(num)
        return total
    else:
        for substr in args:
            string += str(substr)
        return string

print(usm('23'))
#-------------------------------------------
def usm(*args):
    # Начальный аргумент.
    value = args[0]

    # Перебираем все аргументы начиная с первого.
    for arg in args[1:]:
        if type(value) is str:
            value += str(arg)
        else:
            value += int(arg)

    return value

#
# Альтернативный вариант в функциональном стиле
#
def usm(*digits):
    return sum(map(int, digits)) if type(digits[0]) == int else "".join(map(str, digits))

