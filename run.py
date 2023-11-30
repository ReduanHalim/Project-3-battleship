# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint

board = []

for x in range (5):
    board.append(["0"] * 5)

def print_board (board):
    for row in board:
        print " ".join(row)

print_board(board) 
            