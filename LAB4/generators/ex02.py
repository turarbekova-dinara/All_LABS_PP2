#0-ден n-ге дейінгі жұп сандарды үтірмен шығару
n = int(input())
l = (i for i in range(n+1) if i%2==0)
print(*l, sep=', ') #separator