def calc_money(cost, time_spent):
    hours = time_spent[0]
    minutes = time_spent[1] + hours * 60
    cost_minute = cost / 60
    money = minutes * cost_minute
    return round(money)

money = calc_money(700, (2, 11))
print(money)
#--------------------------------------------
def calc_money(rate_per_hour, duration):
    # Распаковываем список в две отдельные переменные
    hours, minutes = duration
    # Считаем часы
    hours_money = hours * rate_per_hour
    # Считаем минуты с округлением.
    minutes_money = round((minutes * rate_per_hour / 60), 0)
    return int(hours_money + minutes_money)

