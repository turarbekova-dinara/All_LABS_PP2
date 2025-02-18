from task import movies

def categories(category = "Action"): #"Romance"
    l = [i['name'] for i in movies if i['category']==category]
    return l

print(categories())