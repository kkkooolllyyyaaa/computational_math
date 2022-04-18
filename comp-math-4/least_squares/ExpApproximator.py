from least_squares.Approximator import Approximator
from least_squares.LinearApproximator import LinearApproximator
from math import log, exp


class ExpApproximator(Approximator):
    def __init__(self):
        self.description = 'Экспоненциальная'
        self.f = 'a1 * e^(a0x)'

    def approximate(self, data):
        n = len(data['x'])
        for i in range(n):
            if data['y'][i] <= 0:
                return None
        lndata = {'x': [i for i in data['x']], 'y': [log(i) for i in data['y']]}
        pred_res = LinearApproximator().approximate(lndata)

        b = exp(pred_res['params'][0])
        a = pred_res['params'][1]
        S = sum([(data['y'][i] - b * exp(a * data['x'][i])) ** 2 for i in range(n)])

        legend = str(round(a, 3)) + ' e^(' + str(round(b, 3)) + ' * x)'

        return {'params': [b, a], 'disp': S, 'func': lambda z: b * exp(a * z), 'legend': legend}
