class Auto:
    def __init__(self):
        self._number = []

    @property
    def number(self):
        return "".join(self._number).upper()

    @number.setter
    def number(self, new_number):
        if new_number.__len__() != 6:
            print("Номер должен состоять из 6 символов")
        else:
            self._number = []
            for i in new_number:
                self._number.append(i)
    # number = property(get_number, set_number)

    @number.deleter
    def number(self):
        self._number = []


if __name__ == '__main__':
    auto1 = Auto()

    auto1.number = "a111aag"
    print("a1:", auto1.number)
