from random import randrange

def InitBoard():
    global current_player

    # Board 3 X 3
    board = [['' for i in range(3)] for j in range(3)]

    cellnumber = 1
    # Fill corresponding cell number in eachof the cells
    for row in range(3):
        for col in range(3):
            board[row][col] = cellnumber
            cellnumber += 1
    #print(type(board))
    board[1][1] = 'x'
    current_player = 'o'
    #print(board)
    return board

#InitBoard()

def start_game():
    game_status = '0'

    while game_status != '-1':
        print('*-----------------------------*')
        print('*      TicTacToe            ', ' *')
        print('* Enter 0 to start the game.', ' *')
        print('* Enter -1 to end the game.', '  *')
        print('*-----------------------------*')

        game_status = input('Enter your choice : ')
        if type(game_status) != "<class 'str'>" and game_status not in ['0', '-1']:
            print('Please enter 0 or -1')
            continue

        if game_status == '-1':
            break

        board = InitBoard()
        play(board)
        DisplayBoard(board)
        #GetListofFreefields(board)

        if winner != None :
                print()
                print('Player', winner, 'wins the game!')
                print()
        else:
            print('game Tied :-)')

# Display current board position
def DisplayBoard(board):
    print('+-------' * 3, '+', sep='')
    for row in range(3):
        print('|       ' * 3, '|', sep='')
        for col in range(3):
            print('|  ', str(board[row][col])+ '   ', end='')
        print('|')
        print('|       ' * 3, '|', sep='')
        print('+-------' * 3, '+', sep='')

def play(board):
    free_fields = len(GetListofFreefields(board))

    global winner
    global current_player

    while free_fields!=0:
        DisplayBoard(board)
        if current_player == 'o':
            # player
            EnterMove(board)
        else:
            #computer
            AutoMove(board)
        
        game_winner = checkWinStatus(board, current_player)
    
        if game_winner != None:
            winner = game_winner
            break
        else:
            if current_player == 'o':
                current_player = 'x'
            else:
                current_player = 'o'

        free_fields = len(GetListofFreefields(board))

def checkWinStatus(board, sign):
    # check rows
    for row in range(3):
        if board[row][0] == sign and board[row][0] == board[row][1] and board[row][1]==board[row][2]:
            return sign
    
    # check columns
    for column in range(3):
        if board[0][column] == sign and board[0][column] == board[1][column] and board[0][column]==board[2][column]:
            return sign
    
    # check diagonals
    if board[0][0] == sign and board[0][0] == board[1][1] and board[1][1] == board[2][2] or \
        board[0][2] == sign and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return sign

    return None


def EnterMove(board):
    turn_ok = False
    
    while not turn_ok:
        move = input('Enter a cell (1 to 9) : ')
        
        if len(move) != 1 or move <= '0' or move > '9':
            print("Your move is Illegal, enter again ")
            continue
        
        move = int(move) - 10
        row = move // 3
        col = move % 3
        
        if board[row][col] in ['o', 'x']:
            print("Enter un occupied cell, please retry again !")
            continue

        turn_ok = not turn_ok
        board[row][col] = 'o'

def AutoMove(board):
    free_fields = GetListofFreefields(board)

    free_fields_l = len(free_fields)
    if free_fields_l > 0:
        random = randrange(free_fields_l)
        row, col = free_fields[random] 
        board[row][col] = 'x'

def GetListofFreefields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['o','x']:
                free_fields.append((row, col))
    #print(free_fields)
    return free_fields


# Starting point
start_game()