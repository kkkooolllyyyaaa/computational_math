from input import *
from linear_algebra import *


def print_vector(vector, word):
    for i in range(0, vector.row):
        print(word + str(i + 1) + ' = ' + str(round(vector.get(i, 0), 2)), end=' ')
    print()


def start():
    print('[file] - получить матрицу с файла')
    print('[cl] - получить матрицу с клавиатуры')
    print()

    input_str = input().strip()
    slae = None
    if input_str == 'file':
        slae = input_from_file()
    elif input_str == 'cl':
        slae = input_from_cl()
    else:
        print('Нет команды ' + input_str)
        exit(1)

    print('Введенная система линейных алгебраических уравнений:')
    print(slae)

    slae_roots = solve_gauss(slae)
    print('СЛАУ приведенная к ступенчатому (треугольному) виду:')
    print(slae)

    print('Определитель матрицы:')
    print(det_triangular(slae.coefficients))
    print()

    if slae_roots is None:
        print('СЛАУ является несовместной')
        print()
        exit(0)

    print('Корни уравнения:')
    print_vector(slae_roots, 'x')
    print()

    residuals_vector = residuals(slae, slae_roots)
    print('Вектор невязок:')
    print_vector(residuals_vector, 'r')
    print()


start()
