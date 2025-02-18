import random
def guess(num, i = 0):
    print('Take a guess.')
    n = int(input())
    if n < num:
        print('\nYour guess is too low.')
        return guess(num, i+1)
    elif n > num:
        print('\nYour guess is too high.')
        return guess(num, i+1)
    else:
        return i+1
    

name = input('Hello! What is your name?\n')
num = random.randint(1, 20)
print(f'\nWell, {name}, I am thinking of a number between 1 and 20.')
attempts = guess(num)
print(f'\nGood job, {name}! You guessed my number in {attempts} guesses!')