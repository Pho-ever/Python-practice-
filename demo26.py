# ----Global Variable ----


# If game is still going
game_still_going = True

winner = None
# Game board
board =     ["_", "_", "_",
            "_", "_", "_",
            "_", "_", "_" ]

# who's turn is it?
current_player = 'X'

# Displaying the initial board
def display_board():
    print( board[0] + "|" + board[1] + "|" + board[2])
    print( board[3] + "|" + board[4] + "|" + board[5])
    print( board[6] + "|" + board[7] + "|" + board[8])

    # Play game
def play_game():

    display_board()
    
    # while the game is still going
    while game_still_going:

        # handle a big turnof arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

        # The game has ended
        if winner == "X" or winner == "O":
            print(winner + " won.")
        elif winner == "":
            print('Tie.')

def check_for_winner():
    # set up global variables
    global winner 

    # check row
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()


    if row_winner:
        winner = row_winner
        # there was a win
    elif column_winner:
        winner = column_winner
        # there was a win 
    elif diagonal_winner:
        winner = diagonal_winner
        # there was na win
    else:
        winner = None
    return

def check_rows():
    # set up global variables
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    # If
    if row_1 or row_2 or row_3:
        game_still_going = False
# Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    # set up global variables
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    # If
    if column_1 or column_2 or column_3:
        game_still_going = False
# Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # set up global variables
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"
    # If
    if diagonal_1 or diagonal_2 :
        game_still_going = False
# Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

# def check_if_tie():
#     return


# # flip player from 'X' to 'O'
# def flip_player():
#     return



# Handle a single turn of an arbitrary player
def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1 
    board[position] = 'X'
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()

    
play_game()