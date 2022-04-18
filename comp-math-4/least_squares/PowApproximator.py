from least_squares.Approximator import Approximator
from least_squares.LinearApproximator import LinearApproximator
from math import log, exp


class PowApproximator(Approximator):
    def __init__(self):
        self.description = 'Степенная'
        self.f = 'a1 * x^a0'

    def approximate(self, data):
        n = len(data['x'])
        for i in range(n):
            if data['x'][i] <= 0 or data['y'][i] <= 0:
                return None
        lndata = {'x': [log(i) for i in data['x']], 'y': [log(i) for i in data['y']]}
        pred_res = LinearApproximator().approximate(lndata)

        a = exp(pred_res['params'][0])
        b = pred_res['params'][1]
        S = sum([(data['y'][i] - a * (data['x'][i]) ** b) ** 2 for i in range(n)])

        return {'params': [b, a], 'disp': S, 'func': lambda z: a * (z ** b)}
