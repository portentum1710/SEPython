# Первый словарь
user = {
    "age": 18,
    "first_name": "Никита",
    "is_active": True,
    "roles": [17, 48],
    "address": {"city": "Москва", "street": "Гагарина", "house": 22}
}

# Второй словарь
profile = {
    "age": 22,
    "first_name": "Nikita",
    "last_name": "Ivanov",
    "email": "user@domain.com"
}

# Расширяем словарь user словарем profile.
# Значения с ключами "first_name" и "age" будут обновлены.
# Значения с ключами "email" и "last_name" будут добавлены.
user.update(profile)


# print(user)

def get_dict(text):
    new_list = []
    for item in text.split(";"):
        new_list.append(item.split(":"))
    return dict(new_list)


# def replace_all(text, num_dict):


# result = replace_all("one, two, three, four", {'one': 'один', 'three': 'три', 'five': 'пять', 'two': 'два'})
# print(result)
text = "one, two, three, four"
lst = "one, two, three, four".split(", ")
print(lst)
dct = {'one': 'один', 'three': 'три', 'five': 'пять', 'two': 'два'}

for item in dct:
    if item in lst:
        print(dct[item])



