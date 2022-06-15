class Board:
    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.status = "[Sandbox " + str(size) + "x" + str(size) + "] Game created"
        self.boardArray = [
            [" " if (x, y) not in mines else "x" for x in range(size)]
            for y in range(size)
        ]

    def __new__(cls, size=None, mines=None):
        # basic input check check
        if not isinstance(size, int) or size <= 1 or not isinstance(mines, list):
            return False
        # remove duplicate values
        mines = list(set(mines))
        # too many mines
        if len(mines) >= (size * size) - 1:
            return False
        # check if all items in mines are actual coordinates on the board
        obj = super().__new__(cls)
        if obj.validateMines(mines, size):
            return obj
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

    def __eq__(self, other):
        return (
            isinstance(self, object)
            and isinstance(other, object)
            and "size" in dir(other)
            and "mines" in dir(other)
            and "status" in dir(other)
            and "boardArray" in dir(other)
            and int(self.size) == int(other.size)
            and list(self.mines) == list(other.mines)
            and str(self.status) == str(other.status)
            and list(self.boardArray) == list(other.boardArray)
        )

    def step(self, square=None):
        if not len([square]) == 1:
            return False
        if not self.validateMines([square], self.size):
            return False
        if self.boardArray[square[0]][square[1]] == "x":
            self.boardArray[square[0]][square[1]] = "X"
            self.status = (
                "[Sandbox "
                + str(self.size)
                + "x"
                + str(self.size)
                + "] BOOM! - Game Over."
            )
            return True
        pass


thisBoard = Board(3, [(1, 1)])
thisBoard.step((1, 1))
print(thisBoard.drawBoard())
