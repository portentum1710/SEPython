# Инкапсуляция заключается в сборе в одно место(класс) данных и методов для работы с ними И предоставлении
# пользователю публичного интерфейса(API)
# Нижнее подчеркивание "_" Это знак того что этот атрибут не предназначен для прямого использовния,
# Работа объекта не гарантируется, при использованнии таких атрибутов
class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self.__age = age
        self.__one__ = 1

    def set_age(self, age):
        if age < 1 or age > 120:
            raise ValueError("Age must be range 1-120")
        self.__age = age

    def describe(self):
        print(f"I`m {self._first_name} {self._last_name}.I am {self.__age} years old!")


if __name__ == '__main__':
    ivan = Person("Ivan", "Ivanov", 24)
    ivan.describe()
    print(ivan.__age)
    print(dir(ivan))
