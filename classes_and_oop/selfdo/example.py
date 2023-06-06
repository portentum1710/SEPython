class Human:
    # Статические поля объявляются внутри класса:
    default_name = "no name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        # Динамические поля
        # Публичные
        self.name = name
        self.age = age
        # Приватные св_ва не могут быть доступны вне класса, даже в классах-потомках
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: {self.__money}")
        print(f"House: {self.__house}")

    # Статический метод(может быть вызван без создания объекта(без параметра self)
    @staticmethod
    def default_info():
        # Чтобы обратиться к статическому полю, нужно обратиться к имени класса
        print(f"Default Name: {Human.default_name}")
        print(f"Default Age: {Human.default_age}")


if __name__ == '__main__':
    print(Human.default_name)

    fedor = Human("Fedor", 32)

    fedor.info()

    Human.default_info()
    a = 0
