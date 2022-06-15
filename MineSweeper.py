class board:
    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.status = "[Sandbox " + str(size) + "x" + str(size) + "] Game created"
        self.boardArray = [
            [" " if (x, y) not in mines else "x" for x in range(size)]
            for y in range(size)
        ]

    def __new__(board, size=None, mines=None):
        # basic input check check
        if not isinstance(size, int) or size <= 1 or not isinstance(mines, list):
            return False
        # remove duplicate values
        mines = list(set(mines))
        # too many mines
        if len(mines) >= (size * size) - 1:
            return False
        # check if all items in mines are actual coordinates on the board
        if board.validateMines(board, mines, size):
            return object.__new__(board)
        return False

    def drawBoard(self):
        separator = "+" + "-+" * self.size + "\n"
        boardString = separator
        for x in range(self.size - 1, -1, -1):
            for y in range(self.size):
                boardString += "|" + (
                    " "
                    if self.boardArray[x][y] in (" ", "x")
                    else self.boardArray[x][y]
                )
            boardString += "|\n"
            boardString += separator
        boardString += self.status
        return boardString

    def validateMines(self, mines, size):
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

    def __eq__(self):
        return False
