from math import sqrt, sin, exp

n_m_values_error = 'Значения n должно быть натуральным числом'
line_error = 'В каждой строке должно быть введено в точности 2 числа (x, y), разделенных пробелом'
left_right_error = 'Значение правой границы должно быть строго больше значения левой границы'

functions = {
    1: lambda x: exp(x),
    2: lambda x: sin(x),
    3: lambda x: sqrt(x),
}

functions_description = {
    1: 'e^x',
    2: 'sin(x)',
    3: 'sqrt(x)'
}


def data_function():
    data = {'x': [], 'y': []}
    print('Выберите одну из предложенных функций:')
    for i in range(len(functions)):
        print(str(i + 1) + ': ' + functions_description[i + 1])
    id = int(input())
    n = int(input('Количество точек: '))
    left = float(input('Левый край: '))
    right = float(input('Правый край: '))
    if right < left:
        exit_msg(left_right_error)
    h = (right - left) / n
    for i in range(n):
        data['x'].append(left)
        data['y'].append(functions[id](left))
        left += h

    print('Полученные точки:')
    for i in range(len(data['x'])):
        x = round(data['x'][i], 4)
        y = round(data['y'][i], 4)
        print(x, ';', y)
    return data


def data_file():
    with open('file/input.txt', 'r') as file:
        n = int(file.readline())
        data = {'x': [], 'y': []}
        try:
            for i in range(n):
                values = [float(i) for i in file.readline().strip().split()]
                if len(values) != 2:
                    raise ValueError
                data['x'].append(float(values[0]))
                data['y'].append(float(values[1]))
            return data
        except ValueError:
            exit_msg(line_error)


def data_console():
    try:
        n = int(input('Введите n: '))
        print('Вводите два числа (x_i, y_i) через пробел в одной строке')
        data = {'x': [], 'y': []}
        for i in range(n):
            values = [float(i) for i in input().strip().split()]
            if len(values) != 2:
                raise ValueError
            data['x'].append(float(values[0]))
            data['y'].append(float(values[1]))
        return data
    except ValueError:
        exit_msg(line_error)


def exit_msg(message):
    print(message)
    exit(1)
    pass
