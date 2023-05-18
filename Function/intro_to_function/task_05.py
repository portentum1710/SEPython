import math


def speed_to_pace(speed):
    total_sec = 3600 / speed
    minutes = int(total_sec / 60)
    sec = total_sec % 60
    return "{}:{:02.0f}".format(minutes, sec)

print(speed_to_pace(12.5))
#---------------------------------------------------
def speed_to_pace(speed):
    """
    Функция переводит скорость (speed) в км/ч в темп (км/мин).
    """
    temp = 60 / speed
    minutes = int(temp)
    seconds = (temp - minutes) * 60
    return "{}:{:02.0f}".format(minutes, seconds)