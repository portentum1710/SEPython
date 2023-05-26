def parallel_connection(*resister):
    total_r = 0
    for r in resister:
        total_r += 1 / r
    return  round(1 / total_r, 3)

r = parallel_connection(2, 6)
print(r)
