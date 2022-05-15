def interpolate(data, x):
    x_data = data['x']
    y_data = data['y']

    if x <= x_data[len(x_data) // 2]:
        return first_interpolate(x_data, y_data, x)
    else:
        return second_interpolate(x_data, y_data, x)


def first_interpolate(x_data, y_data, x):
    h = x_data[1] - x_data[0]
    after_index = 0
    for i in range(len(x_data)):
        if x >= x_data[i]:
            after_index = i
        else:
            break

    t = (x - x_data[after_index]) / h
    answer = dki(y_data, after_index, 0)
    fact = 1
    for i in range(1, len(x_data) - after_index):
        answer += (t_calc(t, i) * dki(y_data, after_index, i)) / fact
        fact *= i + 1
    return answer


def second_interpolate(x_data, y_data, x):
    h = x_data[1] - x_data[0]
    n = len(x_data)
    t = (x - x_data[n - 1]) / h

    answer = dki(y_data, n - 1, 0)
    fact = 1
    for i in range(1, n):
        answer += (t_calc(t, i, False) * dki(y_data, n - i - 1, i)) / fact
        fact *= i + 1
    return answer


def dki(data, i, k):
    if k == 0:
        return data[i]
    elif k == 1:
        return data[i + 1] - data[i]
    else:
        return dki(data, i + 1, k - 1) - dki(data, i, k - 1)


def t_calc(t, n, forward=True):
    result = t
    for i in range(1, n):
        if forward:
            result *= t - i
        else:
            result *= t + i
    return result
