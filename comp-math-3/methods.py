class RectangleMethod:
    def __init__(self, function):
        self.function = function

    # method may be 0, 1/2 or 1 (left, mid, right respectively)
    def solve(self, a, b, n, method=1 / 2):
        result = 0
        h = (b - a) / n
        start = a

        for i in range(n):
            result += self.function.func(start + h * method) * h
            start += h

        return result

    def solve_while(self, a, b, eps, min_n=4, method=1 / 2, max_n=2 ** 25):
        n = min_n
        result = float('inf')
        last_result = 0

        while abs(result - last_result) / 3 > eps:
            last_result = result
            result = self.solve(a, b, n, method)
            n *= 2
            if n >= max_n:
                print('Добиться требуемой точности за разумное время не удалось')
                print('eps = ' + str(abs(last_result - result)))
                break

        return {'n': n, 'result': result}


class SimpsonMethod:
    def __init__(self, function):
        self.function = function

    def solve(self, a, b, n):
        if n % 2 != 0:
            return None

        h = (b - a) / n
        x = a + h
        result = 0

        for i in range(n - 1):
            if i % 2 == 0:
                result += 4 * self.function.func(x)
            else:
                result += 2 * self.function.func(x)
            x += h
        result *= h / 3

        return result

    def solve_while(self, a, b, eps, min_n=4, max_n=2 ** 25):
        if min_n % 2 != 0:
            return None

        n = min_n
        result = float('inf')
        last_div = float('inf')
        last_result = 0

        while abs(result - last_result) / 15 > eps:
            last_result = result
            result = self.solve(a, b, n)
            n *= 2
            if n >= max_n:
                print('Добиться требуемой точности за разумное время не удалось')
                print('eps = ' + str(abs(last_result - result)))
                break
            if abs(last_result - result) > last_div:
                print('Интеграл расходится')
                exit(1)

            last_div = abs(last_result - result)
        return {'n': n, 'result': result}

