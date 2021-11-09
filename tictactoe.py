import random

# Defines the board as a dictionary, the places are numbered from 1 to 9
board = [' ' for x in range(9)]

# This function prints the board retrieving the place value from the board
def print_board():
    print(board[0], board[1], board[2], sep=' | ')
    print('--+---+--')
    print(board[3], board[4], board[5], sep=' | ')
    print('--+---+--')
    print(board[6], board[7], board[8], sep=' | ')

# The players can only choose a value from 1 to 9 and each value can be picked only once in a game
valid_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# The human player makes a choice, the board gets updated and the choice is removed from the valid choices
def human_player():
    choice = input('Make your move! Choose a number from 1 to 9: ')
    if choice in valid_choices:
        board_index = int(choice) - 1
        board[board_index] = 'O'
        valid_choices.remove(choice)
    else:
        return human_player()

# The random player makes a random choice, the board gets updated and the choice is removed from the valid choices
def random_player():
    random_choice = random.choice(valid_choices)
    board_index = int(random_choice) - 1
    board[board_index] = 'X'
    valid_choices.remove(random_choice)
    print('Computer\'s move: ')

# Determining if a player won the game
def check_win(board):
    wins = [board[:3], board[3:6], board[6:9], board[0:8:3], board[1:9:3], board[2:10:3], board[0:10:4], board[2:8:2]]
    for row in wins:
        if row.count('X') == 3:
            print('Computer wins!')
            return True
        elif row.count('O') == 3:
            print('You win!')
            return True
        else:
            return False

def game():
    count_moves = 0
    #while check_win(board) == False:
    while count_moves < 9  and check_win(board) == False:
        human_player()
        count_moves += 1
        print_board()
        print('\n')
        if count_moves < 9 and check_win(board) == False:
            random_player()
            count_moves += 1
            print_board()
            print('\n')
        check_win(board)
        if count_moves == 9 and check_win(board) == False:
            print('It\s a tie!')

game()

restart = input('Do you want to play again? y/n: ')
if restart == 'y'.lower():
    board = [' ' for x in range(9)]
    valid_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    game()
else:
    print('Bye bye!')
