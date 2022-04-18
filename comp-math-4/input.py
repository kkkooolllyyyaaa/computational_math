n_m_values_error = 'Значения n должно быть положительными целыми числом'
line_error = 'В каждой строке должно быть введено в точности 2 числа (x, y), разделенных пробелом'


def read_file():
    with open('file/input.txt', 'r') as file:
        inp = [i for i in file.readline().split()]
        n = getN(inp)
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


def read_console():
    try:
        n = int(input())
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


def getN(inp):
    if len(inp) == 1:
        try:
            n = int(inp[0])
            if n <= 0:
                raise ValueError
            return n
        except ValueError:
            exit_msg(n_m_values_error)
    else:
        exit_msg(n_m_values_error)


def exit_msg(message):
    print(message)
    exit(1)
    pass
