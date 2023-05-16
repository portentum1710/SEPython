def strip(string):
    mod_string = string.split()
    return " ".join(mod_string)

#------------------------------------
def strip(text):
    """
    Вариант на методах.
    """
    return " ".join(text.strip().split())


def strip(text):
    """
    Классический вариант на цикле.
    """
    prev_space = False  # Является ли предыдущий символ пробелом
    start_text = False  # Отметка о том, что начался текст

    final_text = ""

    for c in text:
        # Если пробел
        if c == " ":
            # Если текст уже начался, то основной алгоритм, а если еще нет,
            # то итерация отработает в холостую
            if start_text:
                # Если предыдущий символ пробел, то пропускаем этот
                if prev_space:
                    continue

                # Если предыдущий символ не пробел, то добавляем пробел
                final_text += c

                # Запоминаем, что предыдущий символ пробел
                prev_space = True
        # Вариант, когда встретили не пробел
        else:
            start_text = True   # Отмечаем, что текст начался
            final_text += c     # Добавляем символ к финальному тексту
            prev_space = False  # Запоминаем, предыдущий символ НЕ пробел

    # Убираем последний символ, если перед ним был пробел
    if prev_space:
        final_text = final_text[:-1]

    return final_text


def strip(text):
    """
    Вариант с enumerate.
    Изменение списка в процессе его обхода.
    При удалении элементов список меняет длину,
    поэтому после каждого удаления нужно увеличивать смещение shift.
    """
    result = list(text)
    shift = 0  # Смещение (для учета удаленных символов)
    for i, _ in enumerate(result[1:]):
        if result[i - shift] == " " and result[i - shift - 1] == " ":
            del result[i - shift]
            shift += 1
    return ''.join(result).strip()


# В ходе обсуждения тут https://shultais.education/lms/courses/python-3/1489?thread=7132
# выяснили, что операция del на больших данных работает медленно.
# Вместо неё решили решили просто проставлять None для дублей пробелов.
# А в данном обсуждении https://shultais.education/lms/courses/python-3/1489?thread=8196
# нашли ошибку и исправили её.
def strip(text):
    result = list(text)
    for i, _ in enumerate(result[1:]):
        if result[i] == " " and result[i - 1] in (" ", None):
            result[i] = None
    return ''.join(filter(lambda x: x is not None, result)).strip()
