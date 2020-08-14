
puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
]

def print_board(board):
    for r in range(len(board)):
        if r % 3 == 0 and r != 0:
            print("- - -   - - -   - - - ")
        for c in range(len(board[r])):
            if c % 3 == 0 and c != 0:
                print("| ", end="")
            if c == 8:
                print(board[r][c])
            else:
                print(str(board[r][c]) + " ", end="")

def find_empty(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                return (r,c)
    return None

def valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def solve(board):
    find = find_empty(puzzle)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(board, i, (row,col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def main():
    print_board(puzzle)
    solve(puzzle)
    print("   ")
    print_board(puzzle)

if __name__ == "__main__":
    main()