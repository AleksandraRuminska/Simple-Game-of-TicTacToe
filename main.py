board = [' ','1','2','3','4','5','6','7','8','9']

def display(board):
    print(' '+board[7]+' | '+board[8]+' | '+ board[9] + ' ')
    print('------------')
    print(' '+board[4]+' | '+board[5]+' | '+ board[6] + ' ')
    print('------------')
    print(' '+board[1]+' | '+board[2]+' | '+ board[3] + ' ')


def choose_place(board, num):
    place = '0'

    while not place.isdigit() or place == '0':
        while int(place) not in range(1, 10):
            if num == 1:
                place = input("Player 1! Choose an empty space for your symbol (numbers between 1 and 9): ")
            else:
                place = input("Player 2! Choose an empty space for your symbol (numbers between 1 and 9): ")

    return int(place)


def check_if_over(board, player1):
    symbol = ' '
    in_a_row = 0
    start = 7

    if board[start] == board[start + 1] == board[start + 2]:
        symbol = board[start]

    elif board[start] == board[start - 3] == board[start - 6]:
        symbol = board[start]

    elif board[start] == board[start - 2] == board[start - 4]:
        symbol = board[start]

    elif board[start - 4] == board[start - 5] == board[start - 1]:
        symbol = board[start - 4]

    elif board[start - 3] == board[start - 2] == board[start - 1]:
        symbol = board[start - 3]

    elif board[start - 4] == board[start - 1] == board[start + 2]:
        symbol = board[start - 4]

    elif board[start - 6] == board[start - 2] == board[start + 2]:
        symbol = board[start - 6]

    elif board[start - 6] == board[start - 5] == board[start - 4]:
        symbol = board[start - 6]

    if symbol != ' ':
        if symbol == player1:
            print('Congratulations! Player 1 won!')
        else:
            print('Congratulations! Player 2 won!')
        return 1
    else:
        return 0


def full_board(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return 0

    print("Game over! It's a tie!")
    return 1


game_over = 0
choice = ''

print(
    'Hello! This is a tic tac toe game for 2 players.\nTo win a game you need to place three of your symbols in a row, column or diagonal.\nTo select where to put a symbol write the number when asked\nThe board looks as follows:')
display(board)


while choice != 'X' and choice != 'O':
    choice = input("Welcome! Choose your symbol by typing 'X' or 'O': ")

    if choice != 'X'and choice != 'O':
        print('Wrong symbol!')

player1 = 'X'
player2 = 'O'

if choice == 'X':
    print("You chose 'X' so you are now a Player 1! You will start the game!")
else:
    print("You chose 'O' so you are now a Player 2! Player 1 will start the game!")

num = 1
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


while not game_over:
    display(board)

    if num % 2 == 0:

        index = choose_place(board, 2)
        while board[index] != ' ':
            print('\nThat space is already taken! Choose different place')
            index = choose_place(board, 2)

        board[index] = player2

    else:

        index = choose_place(board, 1)
        while board[index] != ' ':
            print('\nThat space is already taken! Choose different place')
            index = choose_place(board, 1)

        board[index] = player1

    num += 1
    game_over = check_if_over(board, player1)

    if not game_over:
        game_over = full_board(board)
    if game_over:
        display(board)
