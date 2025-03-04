import os

def list_contents(path):
    return os.listdir(path)

print(list_contents("."))
