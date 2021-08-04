import pygame, sys
from solver import solveSudoku
from request import getSudoku

pygame.init()  

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
darkGray = (105,105,105)
gray = (169, 169, 169)
lightGray = (220,220,220)
activeColor = pygame.Color('dodgerblue2')
inactiveColor = pygame.Color('dodgerblue4')

# Fonts
textFont = pygame.font.SysFont('comicsans', 60)
solveButtonFont = pygame.font.SysFont('comicsans', 35)
newButtonFont = pygame.font.SysFont('comicsans', 32)

# Board Dimensions
gridLength = 650
gridWidth = 650
gridStart = [55, 15]
cellSize = 540//9

# Solve Button Dimensions
solveButtonStart = [150, 587.5]
buttonLength = 150
buttonWidth = 40

# New Sudoku Button dimensions
newButtonStart = [350, 587.5]

# Display
grid = pygame.display.set_mode((gridLength,gridWidth))  
pygame.display.set_caption("Sudoku by Kkft9!")
icon = pygame.image.load("images\icon.jpg")
pygame.display.set_icon(icon)

# Method for creating the board and filling the numbers
def drawGrid(board, isDraw, isGiven) :
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
                    isGiven[i][j] = 1

                # Filling the cell with the value
                if isGiven[i][j] :
                    color = black
                else :
                    color = darkGray
                value = textFont.render(str(board[i][j]), True, color)
                grid.blit(value, [x+i*cellSize+20, y+j*cellSize+15])

    #Draw lines
    for i in range(10) :
        if i%3 == 0 :
            pygame.draw.line(grid, black, (x, y+i*cellSize), (x+540, y+i*cellSize), 2)
            pygame.draw.line(grid, black, (x+i*cellSize, y), (x+i*cellSize, y+540), 2)

        else :
            pygame.draw.line(grid, gray, (x, y+i*cellSize), (x+540, y+i*cellSize), 1)
            pygame.draw.line(grid, gray, (x+i*cellSize, y), (x+i*cellSize, y+540), 1)


# Method for creating Solve buttons
def drawButton(button) :
    pygame.draw.rect(grid, button['color'], button['rect'])
    grid.blit(button['text'], button['textBox'])

def createButton(x, y, w, h, text, func) :
    buttonBox = pygame.Rect(x, y, w, h)
    if text=='Solve' :
        text = solveButtonFont.render(text, True, white)
    else :
        text = newButtonFont.render(text, True, white)
    textBox = text.get_rect(center=buttonBox.center)
    button = {
        'rect' : buttonBox,
        'text' : text,
        'textBox' : textBox,
        'color' : inactiveColor,
        'function' : func
    }
    return button

# Logic for playing Sudoku
def playSudoku():  
    def getUnsolvedSudoku(level) :
        return getSudoku(level) #Get the unsolved board from the sudoku api

    def getSolvedSudoku(board) :
        return solveSudoku(board) #Get back the solved sudoku

    board = getUnsolvedSudoku(3) #Get the unsolved board from the sudoku api
    grid.fill(white)
    isGiven = [[0]*9 for _ in range(9)]
    drawGrid(board, True, isGiven)

    solveButton = createButton(solveButtonStart[0], solveButtonStart[1], buttonLength, buttonWidth, 'Solve', getSolvedSudoku)
    newSudokuButton = createButton(newButtonStart[0], newButtonStart[1], buttonLength, buttonWidth, 'New Sudoku', playSudoku)
    buttonArray = [solveButton, newSudokuButton]
    pygame.display.flip() #Updates the entire display

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION :
                for button in buttonArray :
                    if button['rect'].collidepoint(event.pos) :
                        button['color'] = activeColor
                    else :
                        button['color'] = inactiveColor

            elif event.type == pygame.MOUSEBUTTONDOWN :
                # 1->left click ; 2->middle click ; 3->right click
                if event.button == 1 :
                    for button in buttonArray :
                        if button['rect'].collidepoint(event.pos) :
                            if button==solveButton:
                                board = button['function'](board)
                                print("Solve Sudoku!!!")
                                drawGrid(board, False, isGiven)
                            elif button==newSudokuButton :
                                print("Get New Sudoku!")
                                button['function']()

            elif event.type == pygame.QUIT:  
                sys.exit(0)

        for button in buttonArray :
            drawButton(button)
        pygame.display.flip()


