from numpy import *


class Matrix:
    def __init__(self, rows, columns, matr=None):
        self.row = rows
        self.col = columns
        if matr is None:
            self.matrix = zeros((rows, columns), dtype=float)
        else:
            self.matrix = matr

    def add_row_to_row(self, row_to, row_from, coef=1):
        if not self.check_row(row_to) or not self.check_row(row_from):
            return False

        self.matrix[row_to] += coef * self.matrix[row_from]
        return True

    def add_col_to_col(self, col_to, col_from, coef=1):
        if not self.check_col(col_to) or not self.check_col(col_from):
            return False

        for i in range(self.row):
            self.matrix[i][col_to] += coef * self.matrix[i][col_from]
        return True

    def swap_rows(self, row1, row2):
        if not self.check_row(row1) or not self.check_row(row2):
            return False

        self.matrix[[row1, row2]] = self.matrix[[row2, row1]]
        return True

    def swap_cols(self, col1, col2):
        if not self.check_col(col1) or not self.check_col(col2):
            return False

        self.matrix[:, [col1, col2]] = self.matrix[:, [col2, col1]]

    def sub_matrix(self, i, j):
        if not self.check_row(i) or not self.check_col(j):
            return None
        if self.row != self.col:
            return None
        if self.row < 2 or self.col < 2:
            return None

        l_m = [[self.matrix[row][col] for col in range(self.col) if col != j] for row in range(self.row) if row != i]
        return Matrix(self.row - 1, self.col - 1, asarray(l_m))

    def get(self, row, col):
        if not self.check_row(row) or not self.check_col(col):
            return None

        return self.matrix[row][col]

    def set_row(self, row, values):
        if not self.check_row(row):
            return False
        if len(values) != self.col:
            return False

        self.matrix[row] = asarray(values, dtype=float)
        return True

    def get_row(self, row):
        if not self.check_row(row):
            return None

        return self.matrix[row, :]

    def get_col(self, col):
        if not self.check_col(col):
            return None

        return self.matrix[:, col]

    def check_row(self, row):
        return 0 <= row < self.row

    def check_col(self, col):
        return 0 <= col < self.col
