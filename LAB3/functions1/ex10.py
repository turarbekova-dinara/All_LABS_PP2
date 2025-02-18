def unique(l):
    d = []
    for i in l:
        if i not in d: 
            d.append(i)
    return d

l = list(map(int, input().split()))
print(unique(l))