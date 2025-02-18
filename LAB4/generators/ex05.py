#n-ден 0-ге дейінгі сандарды кері бағытта шығару
def down(n):
    for i in range(n, -1, -1):  # n-ден 0-ге дейін кері қарай жүреміз
        yield i
        
for i in down(5):
    print(i)