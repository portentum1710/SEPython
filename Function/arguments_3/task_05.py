def get_dict(text):
    get_list = text.split(";")
    return get_list

result = get_dict("a:10;b:20;c:30")
print(result)