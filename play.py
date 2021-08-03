import pygame, sys
from solver import solveSudoku
from request import getSudoku

pygame.init()  

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
darkGray = (64,64,64)
gray = (169, 169, 169)
lightGray = (220,220,220)
blue = (0,0,255)

# Fonts
textFont = pygame.font.SysFont('comicsans', 60)

# Dimensions
gridLength = 650
gridWidth = 650
gridStart = [55, 15]
cellSize = 540//9

grid = pygame.display.set_mode((gridLength,gridWidth))  
pygame.display.set_caption("Sudoku by Kkft9!")
icon = pygame.image.load("images\icon.jpg")
pygame.display.set_icon(icon)


def drawGrid(board, isDraw) :
    x = gridStart[0]
    y = gridStart[1]

    #Filling the non-empty cells 
    for i in range(9) :
        for j in range(9) :
            # If non-empty cell
            if board[i][j] :
                # Grey background only for non-empty given cells
                if isDraw :
                    pygame.draw.rect(grid, lightGray, [x+i*cellSize, y+j*cellSize, cellSize, cellSize])

                # Filling the cell with the value
                value = textFont.render(str(board[i][j]), True, black)
                grid.blit(value, [x+i*cellSize+20, y+j*cellSize+15])

    #Draw lines
    for i in range(10) :
        if i%3 == 0 :
            pygame.draw.line(grid, black, (x, y+i*cellSize), (x+540, y+i*cellSize), 2)
            pygame.draw.line(grid, black, (x+i*cellSize, y), (x+i*cellSize, y+540), 2)

        else :
            pygame.draw.line(grid, gray, (x, y+i*cellSize), (x+540, y+i*cellSize), 1)
            pygame.draw.line(grid, gray, (x+i*cellSize, y), (x+i*cellSize, y+540), 1)

  
def playSudoku():  
    board = getSudoku(3) #Get the unsolved board from the sudoku api
    grid.fill(white)
    drawGrid(board, True)
    pygame.display.flip() #Updates the entire display

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    board = solveSudoku(board) #Get back the solved sudoku
                    print("Solve Sudoku!!!")
                    drawGrid(board, False)
                    pygame.display.flip()

            elif event.type == pygame.QUIT:  
                sys.exit(0)

