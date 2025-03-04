import time
import math

def delayed_sqrt(num, delay):
    time.sleep(delay / 1000)  # Миллисекундты секундқа айналдыру
    print(math.sqrt(num))

delayed_sqrt(25100, 2123)
