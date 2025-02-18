from task import movies

def check(name="Love"):
    l = [i["imdb"] for i in movies if i["name"] == name]
    if l:
        return l[0] > 5.5
    return False


print(check("Action")) #False