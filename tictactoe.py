import string

class TicTacToe:
    matrix = [[], [], []]
    cells_input = "         "
    X = True
    turns = 0

    def __init__(self):
        self.cells_matrix()
        self.printing()

    def cells_matrix(self):
        counter = 0
        for elem in self.cells_input:
            if counter < 3:
                self.matrix[0].append(elem)
            elif counter > 2 and counter < 6:
                self.matrix[1].append(elem)
            elif counter > 5:
                self.matrix[2].append(elem)
            counter += 1

    def printing(self):
        print('---------')
        print(f'| {self.matrix[0][0]} {self.matrix[0][1]} {self.matrix[0][2]} |')
        print(f'| {self.matrix[1][0]} {self.matrix[1][1]} {self.matrix[1][2]} |')
        print(f'| {self.matrix[2][0]} {self.matrix[2][1]} {self.matrix[2][2]} |')
        print('---------')
        self.win()

    def win(self):
        cell_rows = [self.matrix[0], self.matrix[1], self.matrix[2]]
        cells_columns = [[self.matrix[0][0], self.matrix[1][0], self.matrix[2][0]],
                         [self.matrix[0][1], self.matrix[1][1], self.matrix[2][1]],
                         [self.matrix[0][2], self.matrix[1][2], self.matrix[2][2]]]
        cells_diagonals = [[self.matrix[0][0], self.matrix[1][1], self.matrix[2][2]],
                           [self.matrix[2][0], self.matrix[1][1], self.matrix[0][2]]]
        possibilities = cell_rows + cells_columns + cells_diagonals
        O_wins = ['O', 'O', 'O']
        X_wins = ['X', 'X', 'X']
        if X_wins in possibilities:
            print("X wins")
        elif O_wins in possibilities:
            print("O wins")
        elif self.turns == 9:
            print("Draw")
        else:
            self.filter_input()

    def filter_input(self):
        coordinates = input("Enter the coordinates: ").strip()
        if string.ascii_letters in coordinates or string.punctuation in coordinates:
            print("You should enter numbers!")
        else:
            try:
                a, b = coordinates.split()
                x, y = int(a), int(b)
                self.assign(x, y)
            except ValueError:
                print("You should enter numbers")
                self.filter_input()

    def assign(self, x, y):
        if 0 < x < 4 and 0 < y < 4:
            if self.matrix[abs(y - 3)][x - 1] == " ":
                if self.X:
                    self.matrix[abs(y - 3)][x - 1] = "X"
                    self.X = False
                else:
                    self.matrix[abs(y - 3)][x - 1] = "O"
                    self.X = True
                self.turns += 1
                self.printing()
            else:
                print("This cell is occupied! Chose another one!")
                self.filter_input()
        else:
            print("Coordinates should be from 1 to 3!")
            self.filter_input()

tictactoe = TicTacToe()