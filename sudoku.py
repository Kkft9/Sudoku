from solver import solveSudoku
from request import getSudoku
from board import *

# Method for displaying the Sudoku board
def displayBoard(board) :
    for row in range(9) :
        if row in [3, 6] :
            print ('------+-------+------')
        for column in range(9) :
            if column in [3, 6] :
                print ("| ", end="")

            if column==8:
                print(board[row][column])
            else:
                print(str(board[row][column]) + " ", end="")

# Main method
def main() :
    print("Welcome to Sudoku Solver by Kkft9!")

    drawBoard() #Draw empty Sudoku board

    board = getSudoku(3) #Get the unsolved board from the sudoku api

    board = solveSudoku(board) #Get back the solved sudoku

if __name__ == '__main__' :
    main()