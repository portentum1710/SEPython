def replace_all(text, num_dict):
    modify_text = ""
    for key in num_dict:
        if key in text:
            modify_text = text.replace(key, num_dict[key])
    return modify_text

#result = replace_all('Мой любимый язык программирования C++', {'Java': 'Python', 'PHP': 'Python', 'C++': 'Python'})
#result = replace_all("one, two, three, four", {'one': 'один', 'three': 'три', 'five': 'пять', 'two': 'два'})
result = replace_all('My favorite animal is {animal}. My favorite color is {color}.', {"{animal}":"dog", "{color}":"blue"})

print(result)
