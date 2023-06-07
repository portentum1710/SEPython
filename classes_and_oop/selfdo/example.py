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

    def earn_money(self, amount):
        self.__money += amount
        print(f"Earned {amount} money!Current value: {self.__money}")

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("Not enough money!")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def final_price(self, discount):
        final_price = self.price * (100 - discount) / 100
        print(f"Final price: {final_price}")
        return final_price


# Приватный метод:


if __name__ == '__main__':
    print(Human.default_name)

    fedor = Human("Fedor", 32)

    fedor.info()

    Human.default_info()

    fedor.earn_money(10_000)

    fedor.info()

    house = House(100, 15000)

    fedor.buy_house(house, 3)
    a = 0
