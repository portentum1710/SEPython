
# lesson from Python russian

# Объект - сущность, объеденяющая данные и методы для работы с ними
# Чертеж = класс, объект это дом.
# Класс это НОВЫЙ ТИП данных, объект - его КОНКРЕТНЫЙ представитель
# У любого объекта есть id(адрес в памяти), значение и тип
# Первая потребность для классов - когда не хватает встроенных типов, разное состояние
# Метод это функция, которая принадлежит классу
# Dunder метод(Магические методы)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} says: Meow")


if __name__ == '__main__':
    tom = Cat("Tom", 2)
    angela = Cat("Angela", 1)
    print(tom)
    print(angela)
    tom.meow()  # стр.1 неявно передоёт self
    #  Cat.meow(tom) cтп.2 !!! Стр.1 и стр.2 Аналогичны!!!!
    angela.meow()
