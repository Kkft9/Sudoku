# Method for solving Sudoku
def solveSudoku(board) :
    row = [[0]*9 for _ in range(9)]
    column = [[0]*9 for _ in range(9)]
    box = [[0]*9 for _ in range(9)]

    #Filling all the non-empty cells 
    for i in range(9) :
        for j in range(9) :
            if board[i][j] != 0 :
                row[i][board[i][j] - 1] = 1
                column[j][board[i][j] - 1] = 1
                box[(i//3)*3 + (j//3)][board[i][j] - 1] = 1

    # Recursive method
    def solveSudokuHelper(rowIndex, colIndex) :
        if rowIndex==9 :
            return True
        
        # If non-empty cell then check for next cell
        if board[rowIndex][colIndex] != 0 :
            if colIndex==8 :
                if solveSudokuHelper(rowIndex+1, 0) :
                    return True
            else :
                if solveSudokuHelper(rowIndex, colIndex+1) :
                    return True
            
            return False

        # If empty cell, then check for all numbers from 1-9
        for i in range(9) :
            if row[rowIndex][i]==0 and column[colIndex][i]==0 and box[(rowIndex//3)*3 + (colIndex//3)][i]==0 :
                row[rowIndex][i] = 1
                column[colIndex][i] = 1
                box[(rowIndex//3)*3 + (colIndex//3)][i] = 1
                board[rowIndex][colIndex] = i+1

                if(colIndex == 8) :
                    if solveSudokuHelper(rowIndex+1, 0):
                        return True
                else :
                    if solveSudokuHelper(rowIndex, colIndex+1) :
                        return True
                
                row[rowIndex][i] = 0
                column[colIndex][i] = 0
                box[(rowIndex//3)*3 + (colIndex//3)][i] = 0
                board[rowIndex][colIndex] = 0

        return False
    
    solveSudokuHelper(0, 0)
    return board
