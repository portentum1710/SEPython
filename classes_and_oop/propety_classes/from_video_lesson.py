class Auto:
    def __init__(self):
        self._number = []

    def get_number(self):
        print("Запуск get_number")
        return "".join(self._number).upper()

    def set_number(self, new_number):
        if new_number.__len__() != 6:
            print("Номер должен состоять из 6 символов")
        else:
            self._number = []
            for i in new_number:
                self._number.append(i)
    number = property(get_number, set_number)


if __name__ == '__main__':
    auto1 = Auto()

    auto1.number = "a111aa"
    print("a1:", auto1.number)

