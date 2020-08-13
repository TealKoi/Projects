
class sudoku():
    def __init__(self):
        self.board = [
            [0,9,0,5,0,0,0,0,8],
            [0,0,0,8,0,0,2,0,6],
            [8,0,3,0,1,0,7,0,9],
            [0,2,5,0,0,0,0,0,0],
            [0,0,0,0,2,0,0,0,0],
            [0,0,0,0,0,0,1,9,0],
            [5,0,2,0,9,0,3,0,7],
            [1,0,7,0,0,3,0,0,0],
            [4,0,0,0,0,5,0,6,0]
        ]
        self.print_board()

    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - -   - - -   - - - ")
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i,j)
        return None

    def valid(self, num, pos):
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == num and (i,j) != pos:
                    return False
        return True

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
        for i in range(1,10):
            if self.valid(i, (row, col)):
                self.board[row][col] = i
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

def main():
    s = sudoku()
    s.solve()
    print("_____________________\n")
    s.print_board()

if __name__ == "__main__":
    main()