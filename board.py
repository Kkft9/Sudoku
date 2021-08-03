import pygame, sys

pygame.init()  

black = (0, 0, 0)
white = (255, 255, 255)
grey = (169, 169, 169)

boardLength = 650
boardWidth = 650
boardStart = [55, 15]
cellSize = 540//9

board = pygame.display.set_mode((boardLength,boardWidth))  
pygame.display.set_caption("Sudoku by Kkft9!")
icon = pygame.image.load("images\icon.jpg")
pygame.display.set_icon(icon)


def drawGrid() :
    x = boardStart[0]
    y = boardStart[1]

    #Small cells 
    for i in range(9) :
        for j in range(9) :
            pygame.draw.rect(board, grey, [x+i*cellSize, y+j*cellSize, cellSize, cellSize], 1)

    #Big cells -> box
    for i in range(3) :
        for j in range(3) :
            pygame.draw.rect(board, black, [x+i*cellSize*3, y+j*cellSize*3, cellSize*3, cellSize*3], 2)

  
def drawBoard():  
    board.fill(white)
    drawGrid()
    pygame.display.flip() #Updates the entire display

    while True:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                sys.exit(0)

