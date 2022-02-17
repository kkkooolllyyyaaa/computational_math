from input import *
from linear_algebra import *
import copy


def print_vector(vector, word):
    for i in range(0, vector.row):
        print(word + str(i + 1) + ' = ' + str(round((vector.get(i, 0)), 15)), end=' ')
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

    "Скопируем первоначальную матрицу для вычисления вектора невязок"
    first_slae = copy.deepcopy(slae)

    slae_roots = solve_gauss(slae)
    print('СЛАУ приведенная к ступенчатому (треугольному) виду:')
    print(slae)

    print('Определитель матрицы:')
    print('Элементарные преобразования (диагональ):', det_triangular(slae.coefficients))
    print('Разложение по первой строке:            ', det_minor(first_slae.coefficients))
    print('Через встроенную функцию numpy:         ', det_numpy(first_slae.coefficients))
    print()

    if slae_roots is None:
        print('СЛАУ является несовместной или имеет бесконечное количество решений')
        print()
        exit(0)

    print('Корни уравнения:')
    print_vector(slae_roots, 'x')
    print()

    residuals_vector = residuals(first_slae, slae_roots)
    print('Вектор невязок:')
    print_vector(residuals_vector, 'r')
    print()


start()
