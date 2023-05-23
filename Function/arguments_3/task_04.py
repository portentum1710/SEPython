def resize_disk(new_size_disk, old_blocks):
    increase = new_size_disk / sum(old_blocks)
    new_blocks = []
    for block in old_blocks:
        new_blocks.append(int(block * increase))
    remains = new_size_disk - sum(new_blocks)
    if remains:
        new_blocks[-1] = new_blocks[-1] + remains
    return new_blocks

result = resize_disk(150, [15, 15, 20, 10, 40])
print(result)
#=====================================================
def resize_disk(new_size, parts):
    # Сперва вычисляем % увеличения диска
    current_size = sum(parts)
    percent = new_size / current_size

    # Заводим список для хранения новых размеров
    new_parts = []
    new_parts_size = 0
    for part in parts:
        # Вычисляем новый размер блок и добавляем его в список
        new_part_size = int(part * percent)
        new_parts.append(new_part_size)
        new_parts_size += new_part_size

    # Если суммарный объем блоков меньше объема нового диска
    # то мы увеличиваем последний блок на величину разницы.
    if new_parts_size < new_size:
        new_parts[-1] += new_size - new_parts_size

    return new_parts