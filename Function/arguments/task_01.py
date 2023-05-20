def buh(int_num):
    if int_num < 0:
        return "({0:,})".format(abs(int_num)).replace(",", " ")
    else:
        return "{0:,}".format(int_num).replace(",", " ")

#----------------------------------------------------------------
def buh(amount):
    negative = amount < 0
    amount = abs(amount)

    # Разбиваем на классы
    result = f"{amount:,}".replace(",", " ")

    # Работа с отрицательными числами
    if negative:
        result = f"({result})"

    return result