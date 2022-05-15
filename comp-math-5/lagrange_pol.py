from functools import reduce
from operator import mul


def interpolate(data):
    x_data = data['x']
    y_data = data['y']

    li_x = lambda x, index: {
        reduce(mul, [
            x - x_data[i]
            if i != index
            else 1
            for i in range(len(x_data))
        ])
    }

    return lambda x: {
        sum([
            y_data[i] * (li_x(x, i).pop() / li_x(x_data[i], i).pop())
            for i in range(len(data['x']))
        ])
    }
