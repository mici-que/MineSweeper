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
        for mine in mines:
            if not obj.validCoordinates(mine, size):
                return False
        return obj

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

    def validCoordinates(self, coordinates, size=None):
        if size == None:
            size = self.size
        if (
            not isinstance(coordinates, tuple)
            or len(coordinates) != 2
            or not isinstance(coordinates[0], int)
            or not isinstance(coordinates[1], int)
            or not (0 <= coordinates[0] < size)
            or not (0 <= coordinates[1] < size)
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

        if len([square]) != 1:
            return False
        if not self.validCoordinates(square):
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


thisBoard = Board(3, [(1, 1)])
thisBoard.step((1, 1))
print(thisBoard.drawBoard())
