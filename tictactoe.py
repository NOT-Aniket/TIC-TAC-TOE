#Global Variables
game_still_going=True
winner=None
current_player = "X"
#making the board
board=["-" , "-" , "-",
       "-" , "-" , "-",
       "-" , "-" , "-"]
#function to display the board
def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])
#function to start playing
def play_game():
    display_board()
    while game_still_going:

        handle_turn(current_player)
        display_board()
        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner+" won.")
    elif winner == None:
        print("It's a Tie.")
#function to handling turns
def handle_turn(player):
    print(player+"'s Turn")
    if position not in ["1","2","3","4","5","6","7","8","9"]
        print("Invalid Place")
    position  = input("Choose the position you want to play")
    position = int(position)-1
    board[position] = player

#function to check if game is over
def check_if_game_over():
    check_if_win()
    check_if_tie()

#function to check if win
def check_if_win():
    global winner

    row_winner = check_for_row()
    column_winner = check_for_column()
    diagonal_winner = check_for_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner=None
    return
#function that checks for row wins
def check_for_row():
    #setting glocal variables
    global game_still_going
    #checking if someone won
    row_1=board[0] == board[1] ==board[2] != "-"
    row_2=board[3] == board[4] ==board[5] != "-"
    row_3=board[6] == board[7] ==board[8] != "-"
    #if won returning
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    if row_2:
        return board[4]
    if row_3:
        return board[7]
    return

#function that checks for row wins
def check_for_column():
    #setting glocal variables
    global game_still_going
    #checking if someone won
    column_1=board[0] == board[3] ==board[6] != "-"
    column_2=board[1] == board[4] ==board[7] != "-"
    column_3=board[2] == board[5] ==board[8] != "-"
    #if won returning
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

#function that checks for row wins
def check_for_diagonal():
    #setting glocal variables
    global game_still_going
    #checking if someone won
    diagonal_1=board[0] == board[4] ==board[8] != "-"
    diagonal_2=board[2] == board[4] ==board[6] != "-"

    #if won returning
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return

#function to check if tie
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
    return

#function to handling turns
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()