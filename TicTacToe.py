board = {0:" ", 1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" "}

board_keys = []

for i in board:
    board_keys.append(board[i])

def printBoard(board):
    print(board[0], "|", board[1], "|", board[2])
    print(" - - - - - -")
    print(board[3], "|", board[4], "|", board[5])
    print(" - - - - - -")
    print(board[6], "|", board[7], "|", board[8])

def game():
    turn = "X"
    count = 0
    for i in range(10):
        printBoard(board)
        print("It is {}'s turn.".format(turn))
        move = int(input("Where would you like to move? "))
        if board[move] == " ":
            board[move] = turn
            count += 1
        else:
            print("Please pick a valid space!\n(Remember, the top-left board is 0 and the top-right is 2)")
        if count >= 5:
            if board[0] == board[1] and board[1] == board[2] and board[0] != " ":
                print(turn, "Has Won!")
                break
            elif board[3] == board[4] and board[4] == board[5] and board[3] != " ":
                print(turn, "Has Won!")
                break
            elif board[6] == board[7] and board[7] == board[8] and board[6] != " ":
                print(turn, "Has Won!")
                break
            elif board[0] == board[3] and board[3] == board[6] and board[0] != " ":
                print(turn, "Has Won!")
                break
            elif board[1] == board[4] and board[4] == board[7] and board[1] != " ":
                print(turn, "Has Won!")
                break
            elif board[2] == board[5] and board[5] == board[8] and board[2] != " ":
                print(turn, "Has Won!")
                break
            elif board[0] == board[4] and board[4] == board[8] and board[0] != " ":
                print(turn, "Has Won!")
                break
            elif board[2] == board[4] and board[4] == board[6] and board[2] != " ":
                print(turn, "Has Won!")
                break
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    print(board)
    restart = input("Would you like to restart? y/n ")
    if restart.lower() == "y":
        for i in board:
            i = board_keys[i]
        game()
    else:
        print("See you next time!")

if __name__ == "__main__":
    game()