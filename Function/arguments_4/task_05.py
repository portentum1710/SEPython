def usm(*args):
    if type(args[0]) == int:
        return "int"
    else:
        return "str"

print(usm('4', 1, 5, 9))

