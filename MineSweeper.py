class Board:
    statusMessages = {
        "lose": "BOOM! - Game Over.",
        "flag": "Square flagged as bomb.",
        "win": "the land is cleared! GOOD JOB!",
        "uncover": "bombs around your square.",
    }

    def __init__(self, size, mines):
        self.stepCount = 0
        self.size = size
        self.mines = mines
        self.setStatus("Game created")
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
        if mines == [mine for mine in mines if obj.validCoordinates(mine, size)]:
            return obj
        return False

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

    def setStatus(self, message=None):
        if isinstance(message, str):
            self.status = (
                "[Sandbox " + str(self.size) + "x" + str(self.size) + "] " + message
            )
            return True
        return False

    def drawBoard(self):
        translate = {"x": " ", "#": "*"}
        separator = "+" + "-+" * self.size + "\n"
        boardString = separator
        for x in range(self.size - 1, -1, -1):
            for y in range(self.size):
                boardString += "|"
                if self.boardArray[x][y] in translate.keys():
                    boardString += translate[self.boardArray[x][y]]
                else:
                    boardString += self.boardArray[x][y]
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

    def step(self, square=None):
        if self.validCoordinates(square):
            x = square[1]
            y = square[0]
            squareContent = self.boardArray[x][y]
            if squareContent == "x":
                self.boardArray[x][y] = "X"
                self.setStatus(self.statusMessages["lose"])
                return True
            elif squareContent == " ":
                neighBours = self.calculateNeighbours((x, y))
                self.boardArray[x][y] = str(neighBours[0])
                self.setStatus(
                    str(neighBours[0]) + " " + self.statusMessages["uncover"]
                )
                self.stepCount += 1

                self.checkWin()
                self.checkNeighbours(neighBours)

                return True
        return False

    def checkWin(self):
        if self.stepCount == (self.size * self.size) - len(self.mines):
            self.setStatus(self.statusMessages["win"])

    def checkNeighbours(self, neighBours):
        if neighBours[0] == 0:
            for neighbour in neighBours[1]:
                self.step(neighbour)

    def calculateNeighbours(self, square):
        mines = 0
        neighbours = [
            (x, y)
            for x in range(square[0] - 1, square[0] + 2)
            for y in range(square[1] - 1, square[1] + 2)
            if self.validCoordinates((x, y))
        ]
        for square in neighbours:
            if self.boardArray[square[0]][square[1]] in ["x", "#"]:
                mines += 1
        return [mines, neighbours]

    def flag(self, square):
        if self.validCoordinates(square):
            x = square[1]
            y = square[0]
            squareContent = self.boardArray[x][y]

            if squareContent in ["x", " "]:
                translate = {"x": "#", " ": "*"}
                self.boardArray[x][y] = translate[squareContent]
                self.setStatus(self.statusMessages["flag"])
                return True
        return False
