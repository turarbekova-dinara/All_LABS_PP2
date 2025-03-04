def count_case(s):
    upper = 0
    lower = 0
    for c in s:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    return {"Uppercase": upper, "Lowercase": lower}

text = "Hello World!"
print(count_case(text))  # Uppercase: 2, Lowercase: 8
