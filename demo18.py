import random
print("Welcome to the Cows and Bulls Game")
guess = input('Enter a four digit number')
bulls = 0
cows = 0
numbers = ('0123456789')
length = 4


if len(guess) < 4:
    print("Please pick only four digits")
elif len(guess) > 4:
    print("Please pick only four digits")
    

def cow_bull():
    for value in guess:
    if value in values:
        bulls += 1
    elif value not in values:
        cows += 1
cow_bull()


