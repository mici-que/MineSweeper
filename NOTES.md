# Notes for pair programming

## General considerations
- board (size*size)
  - squares
    - mines

Use one two-dimensional array of size*size with strings to represent the board and the square's content:
- covered mine "x", uncovered mine "X"
- flag "*"
- covered square " "
- uncovered square "0"..."8"

***
- initialize board -> scenario #1

- when player steps on a square
  - if it's a mine, player lost -> scenario #2
  - if it's not a mine, set square to number of mines in neighbouring cells -> scenario #3
    - if it's zero, step on all the neighbours -> scenario #6
  (- if it's flagged, do nothing)
  (- if it contains a number already, do nothing)
- if all squares with no bombs are revealed, player won -> scenario #5 #6

- player can flag and unflag uncovered squares to mark guessed position of mines -> scenario #4

Count the number of steps completed, this will equal the uncovered squares.
winning condition: step count is equal to number of squares minus mines count

loop while step < squares-mines
    Display board
    if we lost or won, display message and end game
    Do action (step/flag/unflag)


## 1. Game board creation

**Initialize board:**
- inputs board size and array of mine coordinates
  - need to validate size: integer bigger than 1
  - need to validate mineCoordinates array:
    - number of items bigger than 0 and smaller than size^2
    - items must be unique (or we could just ignore duplicates)
    - items must be an tuple of two integers
      - integers not bigger than size
- create two-dimensional array with square contents according to mapping

**Draw board**
initial output will always be, as all squares are covered:
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+
[Sandbox 3x3] Game created

- don't test for internal representation of board, only the output

- changed function to validate mines - creating list of coordinate tuples for board slow for big boards

🔴 🟢 ♻️

- back to RED, need to adjust tests:
  - missed status line
  - use board as class
- codesmell and bug on sonarcloud
check __eq__ 
fix __new__
change naming convention on sonarcloud
fixed __eq__ added test for coverage

🔴 🟢 ♻️ ♻️ ♻️ ♻️ ♻️ ♻️

## 2. Game Over - Step on a bomb on 1;1
+-+-+-+
| | | |
+-+-+-+
| |X| |
+-+-+-+
| | | |
+-+-+-+
[Sandbox 3x3] BOOM! – Game Over.

- implement step and lose:
  - step (x,y) as input: 
    - validate x and y are onboard
  - if square value is "x" 
    - draw board and print lost message

( - exit ) => introduce gameplay in next cycle


🔴 🟢 ♻️ ♻️


## 3. Clean square 0;0 and get the number of bombs around
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+
|3| | |
+-+-+-+
[Sandbox 3x3] 3 bombs around your square.

- board to be tested: size=3, mine coordinates (0,1),(1,1),(1,0)

- implement step and calculate:
  - if square value is " "
    - calculate number of neighbour mines and add to board
    - draw board and print message

🔴 🟢 ♻️

***
✅ 🍅 🔴 🟢 ♻️ 💿