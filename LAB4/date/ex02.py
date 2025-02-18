#кеше, бүгін және ертеңгі күнді көрсету
from datetime import *
print("Yesterday: ", (datetime.today() - timedelta(days=1)).strftime('%x'))
print("Today: ", datetime.today().strftime('%x'))
print("Tomorrow: ", (datetime.today() + timedelta(days=1)).strftime('%x'))

#strftime('%x') – Күнді қысқа форматта шығару
#%x - қысқа күн пішімі үшін арналған