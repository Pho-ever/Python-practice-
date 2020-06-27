print('Rock...')
print('Paper...')
print('Scissors...')
while True: 

    user1 = input('Player1 please make your move: ')
    user2 = input('Player2 please make your move: ')
    if user1 == 'rock':
        if user2 == 'scissors':
            print('Player1 won')
        elif user2 == 'paper':
            print('Player2 won')
    elif user1 == 'paper':
        if user2 == 'rock':
            print('Player1 won')
        elif user2 == 'scissors':
            print('Player2 won')
    elif user1 == 'scissors':
        if user2 == 'rock':
            print('Player2 won')
        elif user2 == 'paper':
            print('Player1 won')
    user = input('Do you want to play a new game? yes/no \n')
    if user == 'no':
        break  
    


