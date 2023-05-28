from physics import ep, CONSTANTS
from physics_2 import height

m = 80

print("Ускорение свободного падения:", CONSTANTS["G"])
print("Потенциальная энергия:", ep(m, 2))
print("Расстояние:", height(20))

print("Ускорение свободного падения(еще раз):", CONSTANTS["G"])
print("Потенциальная энергия (еще раз):", ep(m, 2))