import sys

# Список городов
cities = [
    #   Клд  Мск   СПб,  Каз   Врж,  Тверь
    [0, 1337, 1103, 2192, 1855, 1255],  # Калининград
    [1337, 0, 712, 825, 522, 192],  # Москва
    [1103, 712, 0, 1526, 1337, 531],  # Санкт-Петербург
    [2192, 825, 1526, 0, 1080, 1006],  # Казань
    [1855, 522, 1337, 1080, 0, 815],  # Воронеж
    [1255, 192, 531, 1006, 815, 0]  # Тверь
]

def calc_distance(path):
    distance = 0
    for idx, idx_city in enumerate(path):
        next_idx = idx + 1
        if next_idx > len(path) - 1:
            break
        distance += cities[idx_city][path[next_idx]]
    return distance

path = list(map(int, sys.argv[1:]))

# Выводим результат
print(calc_distance(path))
#---------------------------------------------------------
def calc_distance(path):
    """
    Вычисляем расстояние между городами.
    """
    distance = 0
    prev_city = path[0]
    for city in path[1:]:
        distance += cities[prev_city][city]
        prev_city = city

    return distance

