def validateMines(mines, size):
    for mine in mines:
        if (
            not isinstance(mine, tuple)
            or len(mine) != 2
            or not isinstance(mine[0], int)
            or not isinstance(mine[1], int)
            or not (0 <= mine[0] < size)
            or not (0 <= mine[1] < size)
        ):
            return False
    return True


def initBoard(size=None, mines=None):
    # basic input check check
    if not isinstance(size, int) or size <= 1 or not isinstance(mines, list):
        return False
    # remove duplicate values
    mines = list(set(mines))
    # too many mines
    if len(mines) >= (size * size) - 1:
        return False
    # check if all items in mines are actual coordinates on the board
    if validateMines(mines, size):
        board = [
            [" " if (x, y) not in mines else "x" for x in range(size)]
            for y in range(size)
        ]
        return board
    return False


def drawBoard(board=None):
    if board == False:
        return False
    size = len(board)
    separator = "+" + "-+" * size + "\n"
    boardString = separator
    for x in range(size - 1, -1, -1):
        for y in range(size):
            boardString += "|" + (" " if board[x][y] in (" ", "x") else board[x][y])
        boardString += "|\n"
        boardString += separator
    return boardString
