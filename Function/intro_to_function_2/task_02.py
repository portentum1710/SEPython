file_men = open("man.txt", "w+", encoding="utf-8")
file_men.write("""Иван
Петр
Владимир
Алексей
Вадим"""
)
file_wemen = open("woman.txt", "w+", encoding="utf-8")
file_wemen.write("""Наталья
Светлана
Екатерина
Маргорита
Ирина
""")
file_wemen.close()
file_men.close()

def wellcome(name):
    men_names = open("man.txt", encoding="utf-8").read().split("\n")
    weman_names = open("woman.txt", encoding="utf-8").read().split("\n")
    if name in men_names:
        return f"Уважаемый {name}!"
    elif name in weman_names:
        return f"Уважаемая {name}!"
    else:
        return f"Здравствуйте, {name}!"

print(wellcome("Дормидонт"))
#--------------------------------------------------------------------------
def wellcome(name):
    # Сперва открываем файлы и сохраняем их данные в списки.
    man_file = open("man.txt")
    man = man_file.read().split("\n")

    woman_file = open("woman.txt")
    woman = woman_file.read().split("\n")

    # Проверяем нет ли искомого имени в списках.
    if name in man:
        text = "Уважаемый {}!".format(name)
    elif name in woman:
        text = "Уважаемая {}!".format(name)
    else:
        text = "Здравствуйте, {}!".format(name)

    return text