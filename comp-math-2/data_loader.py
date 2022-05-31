from math import sin, exp, cos

line_error = 'Должно быть введено 5 чисел id (1, 2, 3), a, b (a <= b), eps (eps >= 0), x0 по одному в строке'
no_solve_error = 'Возможно на интервале нет корней, посмотрите график и введите корректный промежуток изоляции корня'

functions = {
    1: lambda x: exp(x) - x ** 4,
    2: lambda x: sin(x) + cos(x),
    3: lambda x: (x - 4) * (x - 3) * (x - 2) * (x - 1),
    4: lambda x, y: x ** 2 + y ** 2 - 4,
    5: lambda x, y: -3 * x ** 2 + y
}

functions_str = {
    # for single equation
    1: 'e^x - x^4',
    2: 'sin(x) + cos(x)',
    3: 'x^4 - 10x^3 + 35x^2 - 50x + 24',
    # for equation systems:
    4: 'x - 1',
    5: 'x^3 - 6x^2 + 11x - 6'
}


def data_console():
    data = {'f': None, 'a': 0, 'b': 0, 'eps': 0, 'x0': 0}
    print('Выберите одну из предложенных функций:')
    for i in range(len(functions)):
        print(str(i + 1) + ': ' + functions_str[i + 1])
    function_id = int(input())
    data['f'] = functions[function_id]
    data['a'] = float(input('a: '))
    data['b'] = float(input('b: '))
    data['eps'] = float(input('eps: '))
    if data['b'] <= data['a'] or data['f'] is None or data['eps'] <= 0:
        exit_msg(line_error)
    if data['a'] * data['b'] > 0:
        exit_msg(no_solve_error)
    return data


def data_file():
    with open('file/input.txt', 'r') as file:
        data = {'f': None, 'a': 0, 'b': 0, 'eps': 0, 'x0': 0}
        try:
            data['f'] = functions[int(file.readline())]
            data['a'] = float(file.readline())
            data['b'] = float(file.readline())
            data['eps'] = float(file.readline())
            if data['b'] <= data['a'] or data['f'] is None or data['eps'] <= 0:
                raise ValueError
            if data['a'] * data['b'] > 0:
                raise ValueError
            return data
        except ValueError:
            exit_msg(line_error)


def exit_msg(message):
    print(message)
    exit(1)
    pass
