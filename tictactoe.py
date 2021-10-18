import random

# Defines the board as a dictionary, the places are numbered from 1 to 9
board = {'1': ' ', '2': ' ', '3': ' ', '4': ' ','5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

# This function prints the board retrieving the place value from the board dictionary
def print_board():
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

# The players can only choose a value from 1 to 9 and each value can be picked only once in a game
valid_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# The human player makes a choice, the board gets updated and the choice is removed from the valid choices
def human_player():
    choice = input('Make your move! Choose a number from 1 to 9: ')
    if choice in valid_choices:
        board[choice] = 'O'
        valid_choices.remove(choice)
    else:
        choice = input('Invalid choice, please choose an empty place on the board: ')
        board[choice] = 'O'
        valid_choices.remove(choice)

# The random player makes a random choice, the board gets updated and the choice is removed from the valid choices
def random_player():
    random_choice = random.choice(valid_choices)
    board[random_choice] = 'X'
    valid_choices.remove(random_choice)
    print('Computer\'s move: ')

# Determining if a player won the game
def win_or_lose():
    if board['1'] == board['2'] and board['2'] == board['3'] and board['1'] != ' ':
        if board['1'] == 'X':
            return 'Computer wins!'

        else:
            return 'You win!'

    elif board['4'] == board['5'] and board['5'] == board['6'] and board['4'] != ' ':
        if board['4'] == 'X':
            return 'Computer wins!'

        else:
            return 'You win!'

    elif board['7'] == board['8'] and board['8'] == board['9'] and board['7'] != ' ':
        if board['7'] == 'X':
            return 'Computer wins!'

        else:
            return 'You win!'

    elif board['1'] == board['4'] and board['4'] == board['7'] and board['1'] != ' ':
        if board['1'] == 'X':
            return 'Computer wins!'

        else:
            return 'You win!'

    elif board['2'] == board['5'] and board['5'] == board['8'] and board['2'] != ' ':
        if board['2'] == 'X':
            return 'Computer wins!'

        else:
            return 'You win!'

    elif board['3'] == board['6'] and board['6'] == board['9'] and board['3'] != ' ':
        if board['3'] == 'X':
            return 'Computer wins!'

        else:
            return 'You win!'

    elif board['1'] == board['5'] and board['5'] == board['9'] and board['1'] != ' ':
        if board['1'] == 'X':
            return 'Computer wins!'

        else:
            return 'You win!'

    elif board['3'] == board['5'] and board['5'] == board['7'] and board['3'] != ' ':
        if board['3'] == 'X':
            return 'Computer wins!'

        else:
            return 'You win!'

#THIS DOESN'T WORK :)
def game():
    count_moves = 0
    while count_moves < 9:
        if count_moves >= 5 and win_or_lose != None:
            print(win_or_lose())
            break
        elif count_moves == 9:
            print('It\'s a tie!')
            break
        human_player()
        print_board()
        print('\n')
        random_player()
        count_moves += 1
        print_board()
        print('\n')

game()

restart = input('Do you want to play again? y/n: ')
if restart == 'y'.lower():
    game()
else:
    print('Bye bye!')
