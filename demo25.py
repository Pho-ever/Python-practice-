print('Welcome to the guessing game')
print('You pick a number in your head and allow the computer guess the number')
print("If yes,press '1'\nToo low, press '0'\n To high?, press '2'")

def guess(): 
    i = 0
    j = 100 
    m = 50 
    counter = 1
    print('Please guess a number')
    condition = input('is your guess' + str(m) + '?\n')
    while condition != 1:
        counter += 1
        break
        if condition == 0:
            i = m + 1
        elif condition == 2:
            j = m - 1
        m = (i + j)//2
    
        condition = input('is your guess' + str(m) + '?')
guess()


 

