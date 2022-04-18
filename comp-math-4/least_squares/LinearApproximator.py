from least_squares.Approximator import Approximator


class LinearApproximator(Approximator):
    def __init__(self):
        self.description = 'Линейная'
        self.f = 'a0 + a1x'

    def approximate(self, data):
        n = len(data['x'])
        sx, sx2, sy, sxy = 0, 0, 0, 0
        for i in range(n):
            x = data['x'][i]
            y = data['y'][i]
            sx += x
            sx2 += x ** 2
            sy += y
            sxy += x * y

        delta = sx2 * n - sx * sx
        delta1 = sxy * n - sx * sy
        delta2 = sx2 * sy - sx * sxy

        try:
            a = delta1 / delta
            b = delta2 / delta
        except ZeroDivisionError:
            return None

        sxn = sx / n
        syn = sy / n

        S, r, rdivx, rdivy = 0, 0, 0, 0
        for i in range(n):
            x = data['x'][i]
            y = data['y'][i]
            r += (x - sxn) * (y - syn)
            rdivx += (x - sxn) ** 2
            rdivy += (y - syn) ** 2
            S += (a * x + b - y) ** 2

        r = r / ((rdivx * rdivy) ** (1 / 2))
        return {'params': [b, a], 'disp': S, 'func': lambda z: a * z + b, 'r': r}
