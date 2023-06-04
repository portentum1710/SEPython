class People:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name.upper()


vavan = People("vavan")
print(vavan.__dict__)
print(vavan.get_name())

