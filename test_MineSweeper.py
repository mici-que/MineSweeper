import MineSweeper

### 1. Game board creation

# no input array provided
def test_scenario1_noInput():
    """no input provided to initialize the board, return False"""
    assert (MineSweeper.initBoard()) == False


def test_scenario1_InputDataTypeFail():
    size = "3"
    mineCoordinates = [(1, 1)]
    """board size is string, fail"""
    assert (MineSweeper.initBoard(size, mineCoordinates)) == False


def test_scenario1_noMines():
    """mineCoordinates empty, fail"""
    size = 3
    mineCoordinates = [()]
    assert (MineSweeper.initBoard(size, mineCoordinates)) == False


def test_scenario1_CoordinatesFail():
    """mineCoordinates not coordinates, fail"""
    size = 3
    mineCoordinates = [(1, 2, 3)]
    assert (MineSweeper.initBoard(size, mineCoordinates)) == False


def test_scenario1_MineOffboard():
    """mineCoordinates are off the board, fail"""
    size = 3
    mineCoordinates = [(1, 3)]
    assert (MineSweeper.initBoard(size, mineCoordinates)) == False


def test_scenario1_TooManyMines():
    """too many mines, fail"""
    size = 3
    mineCoordinates = [
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
    assert (MineSweeper.initBoard(size, mineCoordinates)) == False


def test_scenario1_drawBoard():
    """initialized board (3,[[1,1]]), expect initial output as [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]"""
    size = 3
    mineCoordinates = [(1, 1)]
    board = MineSweeper.initBoard(size, mineCoordinates)
    assert (
        MineSweeper.drawBoard(board)
    ) == "+-+-+-+\n| | | |\n+-+-+-+\n| | | |\n+-+-+-+\n| | | |\n+-+-+-+\n"


def test_scenario1_drawBoardFailedInit():
    """initialized board (3,[()]), expect initial output as False"""
    size = 3
    mineCoordinates = [()]
    board = MineSweeper.initBoard(size, mineCoordinates)
    assert (MineSweeper.drawBoard(board)) == False
