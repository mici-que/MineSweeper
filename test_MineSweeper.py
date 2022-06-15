from MineSweeper import board

### 1. Game board creation

# no input array provided
def test_scenario1_noInput():
    """no input provided to initialize the board, return False"""
    gameBoard = board()
    assert (board(gameBoard)) == False


def test_scenario1_InputDataTypeFail():
    """board size is string, fail"""
    size = "3"
    mines = [(1, 1)]
    gameBoard = board(size, mines)
    assert (board(gameBoard)) == False


def test_scenario1_noMines():
    """mines empty, fail"""
    size = 3
    mines = [()]
    gameBoard = board(size, mines)
    assert (board(gameBoard)) == False


def test_scenario1_CoordinatesFail():
    """mines not coordinates, fail"""
    size = 3
    mines = [(1, 2, 3)]
    gameBoard = board(size, mines)
    assert (board(gameBoard)) == False


def test_scenario1_MineOffboard():
    """mines are off the board, fail"""
    size = 3
    mines = [(1, 3)]
    gameBoard = board(size, mines)
    assert (board(gameBoard)) == False


def test_scenario1_TooManyMines():
    """too many mines, fail"""
    size = 3
    mines = [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 1),
    ]
    gameBoard = board(size, mines)
    assert (board(gameBoard)) == False


def test_scenario1_drawBoard():
    """initialized board (3,[[1,1]]), expect initial output as [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]"""
    size = 3
    mines = [(1, 1)]
    gameBoard = board(size, mines)
    print(gameBoard)
    assert (
        (gameBoard.drawBoard())
        == "+-+-+-+\n| | | |\n+-+-+-+\n| | | |\n+-+-+-+\n| | | |\n+-+-+-+\n[Sandbox 3x3] Game created"
    )
