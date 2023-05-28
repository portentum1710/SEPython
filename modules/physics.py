G = 9.8
CONSTANTS = {"G": 9.8}

def ek(m, v):
    return (m * (v ** 2)) / 2

def ep(m, h):
    return  m * CONSTANTS["G"] * h

print("--- Модуль physics импортирован")