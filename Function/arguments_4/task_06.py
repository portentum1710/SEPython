def get_chars(str, *digits):
    new_str = ''
    for idx in digits:
        new_str += str[idx]
    return new_str

print(get_chars("I am Programmer", 0, 2, 4, 6))
#------------------------------------------------
def get_chars(chars, *indexes):
    """
    Функция принимает строку chars и произвольное количество индексов indexes.
    """
    result = ""
    for index in indexes:
        result += chars[index]
    return result