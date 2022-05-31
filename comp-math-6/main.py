import numpy as np
from methods import euler_method, adams_method
from plot import plot
from tasks import get_task

INF = 1e19


def get_data_input():
    data = {}

    print("Выберите метод дифференцирования.")
    print(" 1 — Метод Эйлера")
    print(" 2 — Метод Адамса")
    while True:
        try:
            method_id = input()
            if method_id != '1' and method_id != '2':
                raise AttributeError
            break
        except AttributeError:
            print("Метода нет в списке!")
    data['method_id'] = method_id

    print("\nВыберите задачу.")
    print(" 1 — y' = y + (1 + x)y²\n     на [1; 1,5] при y(1) = -1")
    print(" 2 - y' = x² - 2y\n     на [0; 1] при y(0) = 1")
    while True:
        try:
            task_id = int(input())
            func, acc_func, a, b, y0 = get_task(task_id)
            if func is None:
                raise AttributeError
            break
        except AttributeError:
            print("Функции нет в списке!")
    data['f'] = func
    data['acc_f'] = acc_func
    data['a'] = a
    data['b'] = b
    data['y0'] = y0

    print("\nВведите шаг точек.")
    while True:
        try:
            h = float(input("Шаг точек: "))
            if h <= 0:
                raise ArithmeticError
            break
        except (ValueError, ArithmeticError):
            print("Шаг точек должен быть положительным числом.")
    data['h'] = h

    return data


def solve():
    data = get_data_input()

    runge_p = 0
    method = None
    if data['method_id'] == '1':
        method = euler_method
        runge_p = 1
    elif data['method_id'] == '2':
        method = adams_method
        runge_p = 4
    else:
        print("\n\nВо время вычисления произошла ошибка!")
        exit(1)

    answer = None
    runge_answer = None
    epsilon = float(input('Введите точность вычислений: '))
    while True:
        try:
            answer = method(data['f'], data['a'], data['b'], data['y0'], data['h'])
            runge_answer = method(data['f'], data['a'], data['b'], data['y0'], data['h'] / 2)
            last = len(answer) - 1
            runge_error_i = abs(answer[last][1] - runge_answer[2 * last][1]) / (2 ** runge_p - 1)
            if runge_error_i > epsilon:
                raise OverflowError
        except OverflowError:
            print('Шаг', data['h'], 'слишком велик, понизим его в 2 раза')
            data['h'] /= 2
            continue
        print('Шаг равен', data['h'])
        break

    x = np.array([dot[0] for dot in answer])
    y = np.array([dot[1] for dot in answer])

    acc_x = np.linspace(np.min(x), np.max(x), 100)
    acc_y = [data['acc_f'](i) for i in acc_x]

    print("\nРезультаты вычисления:")
    print('\t\tx\t\t', '\ty\t\t', 'acc_y\t\t', ' runge')
    for i in range(len(answer)):
        runge_error_i = abs(answer[i][1] - runge_answer[2 * i][1]) / (2 ** runge_p - 1)
        print("%12.4f%12.4f%12.4f%12.8f" % (answer[i][0], answer[i][1], data['acc_f'](answer[i][0]), runge_error_i))
    plot(x, y, acc_x, acc_y)


solve()
