class Point:
    def __new__(cls, *args, **kwargs):
        print("Вызов __new__ для " + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print("вызов _init__ для " + str(self))
        self.x = x
        self.y = y


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")


if __name__ == '__main__':
    pt = Point(1, 2)
    print(pt)
    db = DataBase("root", "1, 2, 3, 4", 80)
    db2 = DataBase("root2", "19, 28, 34, 47", 40)
    print(id(db), id(db2))
