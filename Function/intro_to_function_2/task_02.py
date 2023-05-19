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