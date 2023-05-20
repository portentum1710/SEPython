file_card = open("db.txt", "w+", encoding="utf-8")
file_card.write("""123456;841
855814;123
471856;731""")
file_card.close()

card_number = "471856"
floor = "733"
for data in open("db.txt", "r", encoding="utf-8"):
    if card_number in data and floor in data:
        print("True")
    if card_number in data and floor not in data:
        print("False")
    else:
        print(None)