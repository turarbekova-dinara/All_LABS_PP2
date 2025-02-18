#0-ден n-ге дейінгі 3-ке де, 4-ке де бөлінетін сандарды шығарады
def f(n):
    for i in range(0, n+1, 12): 
        yield i

for i in f(100): 
    print(i)