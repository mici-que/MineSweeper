def initBoard(size=None, mines=None):
    # basic input check check
    if not isinstance(size, int) or not size > 1 or not isinstance(mines, list):
        return False
    # remove duplicate values
    mines = list(set(mines))
    # too many mines
    if len(mines) >= (size * size) - 1:
        return False
    # check if all coordinates on board
    if (
        len(
            [
                1
                for mine in mines
                if mine
                not in [
                    (x, y) for x in range(size) for y in range(size)
                ]  # array with board coordinate tuples
            ]
        )
        != 0
    ):
        return False

    board = [
        [" " if (x, y) not in mines else "x" for x in range(size)] for y in range(size)
    ]
    return board


def drawBoard(board=None):
    if board == False:
        return False
    size = len(board)
    boardString = "+" + "-+" * size + "\n"
    for x in range(size - 1, -1, -1):
        for y in range(size):
            boardString += "|" + (" " if board[x][y] in (" ", "x") else board[x][y])
        boardString += "|\n"
        boardString += "+" + "-+" * size + "\n"
    return boardString
