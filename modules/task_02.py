from math import factorial
import  sys

n = int(sys.argv[1])
k = int(sys.argv[2])
def get_combination(n, k):
    c = factorial(n) / (factorial(k) * factorial(n - k))
    return int(c)

print(get_combination(n, k))