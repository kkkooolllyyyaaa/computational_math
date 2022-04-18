from least_squares.Approximator import Approximator
from least_squares.LinearApproximator import LinearApproximator
from math import log


class LogApproximator(Approximator):
    def __init__(self):
        self.description = 'Логарифмическая'
        self.f = 'a1 * ln(x) + a0'

    def approximate(self, data):
        n = len(data['x'])
        for i in range(n):
            if data['x'][i] <= 0:
                return None
        lndata = {'y': [i for i in data['y']], 'x': [log(i) for i in data['x']]}
        pred_res = LinearApproximator().approximate(lndata)

        b = pred_res['params'][0]
        a = pred_res['params'][1]
        S = sum([(data['y'][i] - (a * log(data['x'][i]) + b)) ** 2 for i in range(n)])

        legend = str(round(a, 3)) + ' * ln(x) + ' + str(round(b, 3))
        return {'params': [b, a], 'disp': S, 'func': lambda z: a * log(z) + b, 'legend': legend}
