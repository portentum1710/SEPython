def sm(*num: int):
    result = 0
    if num == " ":
        return 0
    else:
        for n in num:
            result += n
    return result
print(sm())


