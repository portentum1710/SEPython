def resize_disk(new_size_disk, old_blocks):
    increase = new_size_disk // sum(old_blocks)
    remains = new_size_disk % sum(old_blocks)
    return remains

result = resize_disk(102, [10, 10, 20, 10])
print(result)
