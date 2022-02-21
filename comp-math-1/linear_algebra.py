from matrix import *
from numpy import linalg

zero_column_error = 'Если столбец нулевой или элементы линейно зависимы, то система не имеет смысла'


# Решение системы
def solve_gauss(slae):
    to_triangular(slae)
    return reverse_course(slae)


# Прямой ход
def to_triangular(slae):
    n, m = slae.coefficients.row, slae.coefficients.col
    for i in range(n - 1):
        slae.swap_equations(i, find_not_zero(slae.coefficients, i, i))
        a_i_i = slae.coefficients.get(i, i)
        for j in range(i + 1, m):
            c_i_i = -slae.coefficients.get(j, i) / a_i_i
            slae.add_eq_to_eq(j, i, c_i_i)
    return


# Обратный ход
def reverse_course(slae):
    n, m = slae.coefficients.row, slae.coefficients.col
    if is_zero(det_triangular(slae.coefficients)):
        return None

    slae_roots = Matrix(m, 1)
    for i in range(n - 1, -1, -1):
        linear_comb = 0
        for j in range(i + 1, m):
            linear_comb += slae.coefficients.get(i, j) * slae_roots.get(j, 0)
        b_i = slae.free_members.get(i, 0)
        a_i_i = slae.coefficients.get(i, i)
        slae_roots.set_row(i, [(b_i - linear_comb) / a_i_i])
    return slae_roots


# Вычисление определителя
def det_triangular(matr):
    if matr.row != matr.col:
        return None
    res = 1
    for i in range(matr.col):
        res *= matr.get(i, i)
    return res


def find_not_zero(matr, from_row, col):
    for i in range(from_row, matr.row):
        if not is_zero(matr.get(i, col)):
            return i
    print(zero_column_error)
    exit(1)


def det_minor(matr):
    n = matr.row
    if n != matr.col:
        return None
    elif n == 1:
        return matr.get(0, 0)
    elif n == 2:
        return matr.get(0, 0) * matr.get(1, 1) - \
               matr.get(0, 1) * matr.get(1, 0)
    det_res = 0
    alg_complement_sign = 1
    for i in range(n):
        det_res += alg_complement_sign * matr.get(0, i) * det_minor(matr.sub_matrix(0, i))
        alg_complement_sign *= -1
    return det_res


def det_numpy(matr):
    if matr.row != matr.col:
        return None
    return linalg.det(matr.matrix)


def residuals(slae, slae_roots):
    n, m = slae.coefficients.row, slae.coefficients.col
    residuals_vector = Matrix(n, 1)
    for i in range(n):
        lin_comb = 0
        for j in range(m):
            lin_comb += slae_roots.get(j, 0) * slae.coefficients.get(i, j)
        residuals_vector.set_row(i, [lin_comb - slae.free_members.get(i, 0)])
    return residuals_vector


def is_zero(numb):
    return math.isclose(numb, 0.0)
