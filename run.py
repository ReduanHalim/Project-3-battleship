from random import randint

board = []

for x in range (5):
    board.append(["0"] * 5)

def print_board (board):
    for row in board:
        print((" ").join(row))

print("Let's play Battleship!")
print_board(board) 

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len (board[0]) - 1)

ship_row = random_row (board)
ship_col = random_col (board)

for turn in range (4):
    print("Turn"),turn 
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sank the ship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col <0 or guess_col > 4):
            print (" Oops, you missed.")
        elif(board[guess_row][guess_col] == "X"):
            print ("You already guessed that one")
        else:
            print("You missed my ship!")
            board[guess_row][guess_col] == "X"

if turn == 3:
    print("Game over")
                    


                    