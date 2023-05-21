# file_card = open("db.txt", "w+", encoding="utf-8")
# file_card.write("""123456;841
# 855814;123
# 471856;731""")
# file_card.close()


# Создайте функцию check_access в этом месте

def check_access(card, floor):
    access = None
    for data in open("db.txt", "r", encoding="utf-8"):
        data = data.strip().split(";")
        if card not in data[0]:
            continue
        if floor in data[1][0]:
            access = "True"
        else:
            access = "False"
            break
    return access

print(check_access("018471", "1"))
#------------------------------------------------------------
# Создайте функцию check_access в этом месте
def check_access(card_number, floor):
    for card in open("db.txt", "r"):
        file_card_number, room = card.strip().split(";")
        file_floor = room[0]
        if card_number == file_card_number:
            return floor == file_floor
    return None



