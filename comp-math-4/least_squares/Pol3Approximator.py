from least_squares.Approximator import Approximator
import numpy as np


class Pol3Approximator(Approximator):
    def __init__(self):
        self.description = 'Полиномиальная 3 степени'
        self.f = 'a0x + a1x  + a2x^2 + a3x^3'

    def approximate(self, data):
        n = len(data['x'])
        sx, sx2, sx3, sx4, sx5, sx6 = 0, 0, 0, 0, 0, 0
        sy, sxy, sx2y, sx3y = 0, 0, 0, 0

        for i in range(n):
            x = data['x'][i]
            y = data['y'][i]
            sx += x
            sx2 += x ** 2
            sx3 += x ** 3
            sx4 += x ** 4
            sx5 += x ** 5
            sx6 += x ** 6
            sy += y
            sxy += x * y
            sx2y += (x ** 2) * y
            sx3y += (x ** 3) * y

        delta = np.linalg.det(np.array([
            [n, sx, sx2, sx3],
            [sx, sx2, sx3, sx4],
            [sx2, sx3, sx4, sx5],
            [sx3, sx4, sx5, sx6]]))
        delta1 = np.linalg.det(np.array([
            [sy, sx, sx2, sx3],
            [sxy, sx2, sx3, sx4],
            [sx2y, sx3, sx4, sx5],
            [sx3y, sx4, sx5, sx6]]))
        delta2 = np.linalg.det(np.array([
            [n, sy, sx2, sx3],
            [sx, sxy, sx3, sx4],
            [sx2, sx2y, sx4, sx5],
            [sx3, sx3y, sx5, sx6]]))
        delta3 = np.linalg.det(np.array([
            [n, sx, sy, sx3],
            [sx, sx2, sxy, sx4],
            [sx2, sx3, sx2y, sx5],
            [sx3, sx4, sx3y, sx6]]))
        delta4 = np.linalg.det(np.array([
            [n, sx, sx2, sy],
            [sx, sx2, sx3, sxy],
            [sx2, sx3, sx4, sx2y],
            [sx3, sx4, sx5, sx3y]]))

        try:
            a3 = delta4 / delta
            a2 = delta3 / delta
            a1 = delta2 / delta
            a0 = delta1 / delta
        except ZeroDivisionError:
            return None

        S = sum([(a3 * data['x'][i] ** 3 + a2 * data['x'][i] ** 2 + a1 * data['x'][i] + a0 - data['y'][i]) ** 2
                 for i in range(n)])

        legend = str(round(a3, 3)) + 'x^3 +' + str(round(a2, 3)) + 'x^2 + ' + str(round(a1, 3)) + 'x + ' + str(
            round(a0, 3))

        return {'params': [a0, a1, a2, a3], 'disp': S, 'func': lambda z: a3 * z ** 3 + a2 * z ** 2 + a1 * z + a0,
                'legend': legend}
