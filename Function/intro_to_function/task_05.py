def speed_to_pace(speed):
    sec = int(3600 / speed)
    minute = int(sec // 60)
    sec = sec - minute * 60
    return f"{minute}:{sec}"

t = speed_to_pace(12)
print(t)
