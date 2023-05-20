def products_range(qu_products, page):
    start_index = (page - 1) * qu_products
    end_index = start_index + qu_products
    indexes = (start_index, end_index)
    return indexes


def products_range(products_per_page, page):
    return products_per_page * (page - 1), products_per_page * page

print(products_range(3, 2))