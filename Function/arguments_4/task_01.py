def series_connection(*resister):
    total_r = 0
    for r in resister:
        total_r += r
    return  total_r

r = series_connection(1, 1.2, 1.4, 1.6)
print(r)
