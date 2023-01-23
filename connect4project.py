import numpy as np

turn = 1
board = np.zeros((6, 7), dtype=int)
print(board)
print(turn)
still_playing = 1


def legal_move(row, col, turn, ):
    if (row == 5):
        if (turn % 2 == 0):
            board[row, col] = 2
        else:
            board[row, col] = 1
            print(board)

    else:
        if (board[row + 1, col] == 1 or board[row + 1, col] == 2):
            if (turn % 2 == 0):
                board[row, col] = 2
            else:
                board[row, col] = 1
        else:
            print("Illegal move: try again")
            return False
    return True 


def win_check(board):
    board_state = [board, board.transpose(), downward_diagnol_transpose(board)]
    for situation in board_state:
        x_length = situation.shape[0]
        y_length = situation.shape[1]
        x = 0
        y = 0
        while (x_length - 1 >= x):
            y = 0
            while (y <= y_length - 4):
                if (situation[x, y] == 2 and situation[x, y + 1] == 2 and situation[x, y + 2] == 2 and situation[x, y + 3] == 2):
                    print("PLAYER 2 WINS!!!")
                elif (situation[x, y] == 1 and situation[x, y + 1] == 1 and situation[x, y + 2] == 1 and situation[x, y + 3] == 1):
                    print("PLAYER 1 WINS!!!")
                y += 1
            y += 1
            x += 1
        print("Checked horizontals")


def downward_diagnol_transpose(board):
    
    dummy_array = np.empty(0)
    long_axis_length = max(board.shape)
    max_diagonal_length = np.diagonal(board, 0).size
    
    for iteration in range(1, long_axis_length):
        above_diagonal = np.diagonal(board, iteration)
        above_diagonal_length =  above_diagonal.size
        below_diagonal = np.diagonal(board, -iteration)
        below_diagonal_length =  below_diagonal.size
        
        zeros_needed = max_diagonal_length - above_diagonal_length
        for fill in range(zeros_needed):
            above_diagonal = np.append(above_diagonal, 0)
            
        zeros_needed = max_diagonal_length - below_diagonal_length
        for fill in range(zeros_needed):
            below_diagonal = np.append(below_diagonal, 0)
            
        dummy_array = np.append(dummy_array, above_diagonal)
        dummy_array = np.append(dummy_array, below_diagonal)
        final_dummy_length = max_diagonal_length
        final_dummy_area = dummy_array.size
        final_dummy_width = int(final_dummy_area/ final_dummy_length)
    dummy_array = dummy_array.reshape(final_dummy_width, final_dummy_length)
    return dummy_array
    
    # x moves 3 times
    # y moves once first time
    # y moves twice
    # y moves three times
    # twice and once again


while (still_playing == 1):
    print(turn)
    if (turn % 2 == 0):
        user_row_input = int(input(
            "It is player 2s turn. What row would you like to place your piece on?  ")) - 1
        user_col_input = int(input("What column?  ")) - 1
        legal_move(user_row_input, user_col_input, turn)
        if(legal_move):
            turn += 1
            print(board)
            win_check(board)
        else:
            continue
        #win_check(board.transpose)
       # diagnol_check()
    else:
        user_row_input = int(input("It is player 1s turn. What row would you like to place your piece on?  ")) - 1
        user_col_input = int(input("What column?  ")) - 1
        legal_move(user_row_input, user_col_input, turn)
        if(legal_move):
            turn += 1
            win_check(board)
            win_check(board.transpose)
        else:
            continue
        # diagnol_check()

    end = input("Do you still want to play?  ")
    if (end == "No" or end == "no"):
        still_playing = 2



