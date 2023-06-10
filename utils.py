
'''This contains the code for solving a sudoku puzzle '''

def valid(board, pos, num):
    '''Whether a number is valid in that cell, returns a bool'''   
    
    i = pos[0]
    j = pos[1] 
    
    for k in range(len(board)):

        if(board[i][k]==num):
            return False
        if(board[k][j]==num):
            return False
        if(board[3*(i//3)+k//3][3*(j//3)+k%3]==num):
            return False
    
    return True


def solve(board):
    '''Solves the Sudoku board via the backtracking algorithm'''

    rows = len(board)
    columns  = len(board[0])

    for i in range(rows):
        for j in range(columns):
            
            if board[i][j]==0:
                
                for num in range(1,10):

                    if valid(board,(i,j),num):
                        
                        board[i][j] = num
                        if solve(board):
                            return True
                        board[i][j] = 0
                
                return False

    return True


def find_empty(board):

    rows = len(board)
    columns  = len(board[0])

    for i in range(rows):
        for j in range(columns):
            if board[i][j]==0:
                return (i,j)
    return None


def print_board(board):
    '''Prints the board'''

    boardString = ''
    for i in range(9):
        for j in range(9):
            boardString += str(board[i][j]) + ' '
            if (j + 1) % 3 == 0 and j != 0 and j + 1 != 9:
                boardString += '| '

            if j == 8:
                boardString += '\n'

            if j == 8 and (i + 1) % 3 == 0 and i + 1 != 9:
                boardString += '- - - - - - - - - - - \n'
    print(boardString)


if __name__ == '__main__':
    board =  [
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3],
        [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0]
    ]
    solve(board)
    print_board(board)
