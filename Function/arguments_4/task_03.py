def sm(*num: int):
    result = 0
    if num == " ":
        return 0
    else:
        for n in num:
            result += n
    return result
print(sm(2, 59, 3, 90))

def compare_str(s1, s2, reg=False, trim=True):
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:
        s1 = s1.strip()
        s2 = s2.strip()

    return s1 == s2

print(compare_str("Python", "PYTHON", True, False))
