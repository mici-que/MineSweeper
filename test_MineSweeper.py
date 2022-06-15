from MineSweeper import Board

### 1. Game board creation

# no input array provided
def test_scenario1_noInput():
    """no input provided to initialize the board, return False"""
    gameBoard = Board()
    assert (gameBoard) == False


def test_scenario1_InputDataTypeFail():
    """board size is string, fail"""
    size = "3"
    mines = [(1, 1)]
    gameBoard = Board(size, mines)
    assert (gameBoard) == False


def test_scenario1_noMines():
    """mines empty, fail"""
    size = 3
    mines = [()]
    gameBoard = Board(size, mines)
    assert (gameBoard) == False


def test_scenario1_CoordinatesFail():
    """mines not coordinates, fail"""
    size = 3
    mines = [(1, 2, 3)]
    gameBoard = Board(size, mines)
    assert (gameBoard) == False


def test_scenario1_MineOffboard():
    """mines are off the board, fail"""
    size = 3
    mines = [(1, 3)]
    gameBoard = Board(size, mines)
    assert (gameBoard) == False


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
    gameBoard = Board(size, mines)
    assert (gameBoard) == False


def test_scenario1_drawBoard():
    """initialized board (3,[[1,1]]), expect initial output as [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]"""
    size = 3
    mines = [(1, 1)]
    gameBoard = Board(size, mines)

    assert (
        (gameBoard.drawBoard())
        == "+-+-+-+\n| | | |\n+-+-+-+\n| | | |\n+-+-+-+\n| | | |\n+-+-+-+\n[Sandbox 3x3] Game created"
    )


## additional test for class behaviour


def test_eqTrue():
    class Mock:
        size = 3
        mines = [(1, 1)]
        status = "[Sandbox 3x3] Game created"
        boardArray = [
            [" " if (x, y) not in [(1, 1)] else "x" for x in range(3)] for y in range(3)
        ]

    testObj = Mock()
    """test __eq__()"""
    size = 3
    mines = [(1, 1)]
    gameBoard = Board(size, mines)
    print(dir(testObj))
    if "size" in vars(gameBoard):
        print("found")
    assert gameBoard == testObj


def test_eqFalse1():
    """test __eq__(): should return False, compared object has no boardArray attribute"""

    class Mock:
        size = 3
        mines = [(1, 1)]
        status = "[Sandbox 3x3] Game created"

    testObj = Mock()
    size = 3
    mines = [(1, 1)]
    gameBoard = Board(size, mines)
    assert gameBoard != testObj


def test_eqFalse2():
    """test __eq__(): should return False, compared Board instance to integer"""
    size = 3
    mines = [(1, 1)]
    gameBoard = Board(size, mines)
    assert gameBoard != 1
