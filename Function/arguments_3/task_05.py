def get_dict(text):
    new_list = []
    for item in text.split(";"):
        new_list.append(item.split(":"))
    return dict(new_list)


result = get_dict("a:10;b:20;c:30")
print(result)
# -----------------------------------------
# def get_dict(text: str):
#     data = {}
#     for item in text.split(";"):
#         k, v = item.split(":")
#         data[k] = v
#     return data
