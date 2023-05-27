def os_path(*args):
    print(args)

os_path("F:\\~stepik.org", "Добрый, добрый Python (Питон)", "39\\p39. Функции.docx")

def path(*args):
    file_path = ""
    for p in args:
        file_path += f"/{p}"
    return file_path
#----------------------------------------
def path(*args):
    return "/" + "/".join(args)

print(path("var", "www"))
