import sys

# Напишите вашу функцию тут.
def sum_mult_index(lst):
    sum = 0
    for indx, num in enumerate(lst):
        sum += indx * num
    return sum
# Не меняйте код ниже, он нужен для проверки задания
values = list(map(int, sys.argv[1:]))
print(sum_mult_index(values))


