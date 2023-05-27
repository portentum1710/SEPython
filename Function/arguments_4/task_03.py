def sm(*num: int):
    result = 0
    if num == " ":
        return 0
    else:
        for n in num:
            result += n
    return result
print(sm(2, 59, 3, 90))

#---------------------------------------
def sm(*args):
    i = 0
    # Перебираем все аргументы.
    for arg in args:
        i += arg

    return i

# Вариант 2: хак с помощью sum.
def sm(*args):
    return sum(args)
