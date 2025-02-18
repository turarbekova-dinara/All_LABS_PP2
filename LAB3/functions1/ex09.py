import math
def v(r):
    return 4/3 * math.pi * pow(r, 3)

r = int(input())
print(f'Volume = {v(r)}')