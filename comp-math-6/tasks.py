from math import exp


def get_task(task_id):
    if task_id == 1:
        # y' = y + (1 + x) * y^2
        return lambda x, y: y + (1 + x) * (y ** 2), \
               lambda x: -1 / x, \
               1, \
               1.5, \
               -1
    elif task_id == 2:
        # y' = x^2 - 2y
        return lambda x, y: (x ** 2) - 2 * y, \
               lambda x: 3 / 4 * exp(-2 * x) + 1 / 2 * (x ** 2) - 1 / 2 * x + 1 / 4, \
               0, \
               1, \
               1
    else:
        return None
