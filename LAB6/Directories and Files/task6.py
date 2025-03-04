import string

for letter in string.ascii_uppercase:
    open(f"{letter}.txt", "w").write(f"This is {letter}.txt\n")
