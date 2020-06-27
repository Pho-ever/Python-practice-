from random import randint 
rand_num = randint(0,10)
count = 0
while True:
    user = (input('Please,pick a number from 1 - 9  \n'))
    user = int(user)
    count += 1
    if user < rand_num: 
        print('Too low')
    elif user > rand_num: 
        print('Too high')
    else: 
        print(f'Congrats, you tried {count} times, You won')
        again = (input('Do you want to play again Yes/No \n'))
        if again == 'No'.lower():
            break 
