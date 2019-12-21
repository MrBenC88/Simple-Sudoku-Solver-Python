#sudoku.py


'''

Backtracking Sudoku Puzzle Solver

1. Parse through board and find empty space
2. Place digits 1-9 in space.
3. Check if digit is valid in spot and if board is valud.
4. If digit valid, fill next spot in board.
    If not valid, reset the square to empty (bd[row][col] = 0 )
    using backtracking and try different value
5. Once board is full, it is solved.


'''


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


board2 = [
    [0,0,0,4,0,0,1,0,0],
    [6,0,0,0,0,5,0,0,9],
    [0,0,0,6,0,1,0,7,0],
    [0,0,0,0,0,0,2,6,0],
    [0,0,1,0,0,0,0,3,0],
    [9,0,0,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,0,0,0,0,7,0,0,0],
    [0,4,0,2,0,0,0,0,7]
]





def printbd(bd):
    #Param: Board    
    #Prints the Sudoku Board State

    for i in range (len(bd)):
        if i % 3 ==0 and i !=0:
            print("- - - - - - - - - - - -")

        for j in range (len(bd[0])): #Length of each row            
            if j != 0 and j % 3 == 0:
                print(" | ", end="")


            if j == 8:
                print(bd[i][j])
            else:
                print(str(bd[i][j]) + " ", end="")


def solve(bd):
    #Assume that Board is filled.

    #Base case
    find = findEmptySquare(bd)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        #Check values 1-9 and see if they are valid after adding them in solution
        if valid(bd, i, (row,col)):
            bd[row][col] = i
            
            if solve(bd): # Solve helper function
                return True

            bd[row][col] = 0 #Backtracking. Reset last element and try diff value
            
    return False

        

def findEmptySquare(bd):
    # Given board, finds empty square and returns its position
    # Empty is denoted by integer 0
    for i in range (len(bd)):
        for j in range (len (bd[0])):
            if bd[i][j] == 0:
                return (i, j) # row, col
    return None # if no blank squares , then return none.

def valid(bd, num, pos):
    #Checks if Board is valid
    
    #Check row
    for i in range (len(bd[0])):
        if bd[pos[0]][i] == num and pos[1] != i:
            #Check through each element in the row
            #If matches the number that we added in, return false.
            #If it is the position we inserted then ignore that position
            return False

    #Check columns
    for i in range (len(bd)):
        if bd[i][pos[1]] == num and pos[0] != i:
            #Check column value
            return False

    #Check Box of 9 (3x3 grids)
    '''
    We use integer division to get the specific locations of each grid of 3.
    The 9 boxes thus would be.
    (0,0)  | (0,1) |  (0,2)
    - - - - - - - - - - - -
    (1,0)  | (1,1) |  (1,2)
    - - - - - - - - - - - -
    (2,0)  | (2,1) |  (2,2)

    '''
    gridx = pos[1] // 3
    gridy = pos[0] // 3

    for i in range(gridy*3, gridy*3 + 3):
        # from the gridx, gridy, we only get 0, 1, 2.
        # Note that to check elements within each box,
        # We have to take the gridx, gridy values and multiple by 3, and add 3

        #ie. if we have box at y =2, we will be in lower right-hand box
        # Multiply 3 and then add 3 to get to index (for index 6, 7, 8, etc.)
        for j in range(gridx*3, gridx*3 + 3):
            if bd[i][j] == num and (i,j) != pos:
                return False
        return True

solve(board)
printbd(board)

print("---------------------------------------")
solve(board2)
printbd(board2)


