def pretty(query):
    return str(round(query, 2))


class SLAE:
    def __init__(self, coefficients, free_members):
        self.coefficients = coefficients
        self.free_members = free_members
        self.swap_cnt = 0

    def add_eq_to_eq(self, row_to, row_from, coef=1):
        self.coefficients.add_row_to_row(row_to, row_from, coef)
        self.free_members.add_row_to_row(row_to, row_from, coef)

    def swap_equations(self, row1, row2):
        self.coefficients.swap_rows(row1, row2)
        self.free_members.swap_rows(row1, row2)
        if row1 != row2:
            self.swap_cnt += 1

    def __str__(self):
        res = ''
        for i in range(0, self.coefficients.row):
            res += pretty(self.coefficients.get(i, 0)) + ' x1'
            for j in range(1, self.coefficients.col):
                res += ' + ' + pretty(self.coefficients.get(i, j)) + ' x' + str(j + 1)
            res += ' = ' + pretty(self.free_members.get(i, 0)) + '\n'
        return res
