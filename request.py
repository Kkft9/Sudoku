import requests

SIZE=9 #This is a constant

def getSudoku(level) :
    # Making a GET request to get unsolved sudoku board json
    response = requests.get("http://www.cs.utep.edu/cheon/ws/sudoku/new?size={}&level={}".format(SIZE, level))
    boardJson = response.json()["squares"] #Extracting Json 
    length = len(boardJson)
    board = [[0]*9 for _ in range(9)] #Sudoku board

    for i in range(length) :
        xCoordinate = boardJson[i]["x"]
        yCoordinate = boardJson[i]["y"]
        value = boardJson[i]["value"]
        board[xCoordinate][yCoordinate] = value

    return board
