def replace_all(text, num_dict):
    for key in num_dict:
        text = text.replace(key, num_dict[key])
    return text

result = replace_all('My favorite animal is {animal}. My favorite color is {color}.', {"{animal}":"dog", "{color}":"blue"})
print(result)
#=====================================================
def replace_all(text: str, data: dict):
    for k, v in data.items():
        text = text.replace(k, v)
    return text

