def pace_to_speed(minutes, seconds = 0):
    seconds = (minutes * 60) + seconds
    speed = 3600 / seconds
    return round(speed, 1)

print(pace_to_speed(4))

#-----------------------------------------
def pace_to_speed(minutes, seconds=0):
    """
    Функция переводит темп бега км/мин в скорость.
    """
    # Преобразовываем к десятичном виду.
    time = minutes + (seconds / 60)

    # Округляем и выводим результат.
    return round(60 / time, 1)