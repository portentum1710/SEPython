class House:
    def __init__(self):
        self.price = 0
        self.square = 0


if __name__ == '__main__':
    house = House()
    print(house.price)
    print(house.square)
    house.price = 1000
    print(house.price)
