from least_squares.Approximator import Approximator
import numpy as np


class Pol2Approximator(Approximator):
    def __init__(self):
        self.description = 'Полиномиальная 2 степени'
        self.f = 'a0 + a1x + a2x^2'

    def approximate(self, data):
        n = len(data['x'])
        sx, sx2, sx3, sx4 = 0, 0, 0, 0
        sy, sxy, sx2y = 0, 0, 0

        for i in range(n):
            x = data['x'][i]
            y = data['y'][i]
            sx += x
            sx2 += x ** 2
            sx3 += x ** 3
            sx4 += x ** 4
            sy += y
            sxy += x * y
            sx2y += (x ** 2) * y

        delta = np.linalg.det(
            [[n, sx, sx2],
             [sx, sx2, sx3],
             [sx2, sx3, sx4]])
        delta1 = np.linalg.det([
            [sy, sx, sx2],
            [sxy, sx2, sx3],
            [sx2y, sx3, sx4]])
        delta2 = np.linalg.det([
            [n, sy, sx2],
            [sx, sxy, sx3],
            [sx2, sx2y, sx4]])
        delta3 = np.linalg.det(
            [[n, sx, sy],
             [sx, sx2, sxy],
             [sx2, sx3, sx2y]])

        try:
            a2 = delta3 / delta
            a1 = delta2 / delta
            a0 = delta1 / delta
        except ZeroDivisionError:
            return None

        S = sum([
            (a2 * data['x'][i] ** 2 + a1 * data['x'][i] + a0 - data['y'][i]) ** 2
            for i in range(n)
        ])
        legend = str(round(a2, 3)) + 'x^2 + ' + str(round(a1, 3)) + 'x + ' + str(round(a0, 3))

        return {'params': [a0, a1, a2], 'disp': S, 'func': lambda z: a2 * z ** 2 + a1 * z + a0, 'legend': legend}
