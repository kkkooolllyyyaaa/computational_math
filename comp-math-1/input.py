from Matrix import *
from slae import *

n_m_error = 'Количество параметров в первой строке должно быть равно 1 или 2'
n_m_values_error = 'Значения размерности n и m должны быть положительными целыми числами'
line_error = 'Должно быть введено в точности m + 1 чисел, разделенных пробелом'


def input_from_file():
    with open('file/input.txt', 'r') as file:
        inp = [i for i in file.readline().split()]
        n, m = get_dims(inp)
        coefficients = Matrix(n, m)
        free_members = Matrix(n, 1)
        try:
            for i in range(n):
                values = [float(i) for i in file.readline().strip().split()]
                if len(values) != m + 1:
                    raise ValueError
                coefficients.set_row(i, values[:-1])
                free_members.set_row(i, values[-1:])
            return SLAE(coefficients, free_members)
        except ValueError:
            exit_msg(line_error)


def input_from_cl():
    inp = [i for i in input().split()]
    n, m = get_dims(inp)
    coefficients = Matrix(n, m)
    free_members = Matrix(n, 1)
    try:
        for i in range(n):
            values = [float(i) for i in input().strip().split()]
            if len(values) != m + 1:
                raise ValueError
            coefficients.set_row(i, values[:-1])
            free_members.set_row(i, values[-1:])
        return SLAE(coefficients, free_members)
    except ValueError:
        exit_msg(line_error)


def get_dims(inp):
    if len(inp) == 1:
        try:
            n = int(inp[0])
            if n <= 0:
                raise ValueError
            return n, n
        except ValueError:
            exit_msg(n_m_values_error)
    elif len(inp) == 2:
        try:
            n = int(inp[0])
            m = int(inp[0])
            if n <= 0 or m <= 0:
                raise ValueError
            return n, m
        except ValueError:
            exit_msg(n_m_values_error)
    else:
        exit_msg(n_m_values_error)


def exit_msg(message):
    print(message)
    exit(1)
    pass
