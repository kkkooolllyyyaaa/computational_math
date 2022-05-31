def euler_method(f, a, b, y0, h):
    # Значения функции, вначале x0 = a
    dots = [(a, y0)]
    n = calculate_n(a, b, h)

    for i in range(0, n):
        # y_(i+1) = y_i + h * f(x_i, y_i)
        dots.append((dots[i][0] + h,
                     dots[i][1] + h * f(dots[i][0], dots[i][1])))
    return dots


# Метод Адамса с четвёртым порядком точности k = 4
def adams_method(f, a, b, y0, h):
    # Пусть вычислены значения в 4 последовательных узлах
    n = calculate_n(a, b, h)
    b0 = min(b, a + 3 * h)
    # Решим для трёх точек приближенно, методом эйлера
    dots = euler_method(f, a, b0, y0, h)

    for i in range(4, n + 1):
        # Конечные разности вычисленные для постоянного шага h
        # При этом, используется интерполяционные многочлен Ньютона
        fi = f(dots[i - 1][0], dots[i - 1][1])
        fi_1 = f(dots[i - 2][0], dots[i - 2][1])
        fi_2 = f(dots[i - 3][0], dots[i - 3][1])
        fi_3 = f(dots[i - 4][0], dots[i - 4][1])

        df = fi - fi_1
        d2f = fi - 2 * fi_1 + fi_2
        d3f = fi - 3 * fi_1 + 3 * fi_2 - fi_3

        x_i = dots[i - 1][0] + h
        y_i = dots[i - 1][1]

        dots.append((
            x_i,
            (y_i + h * fi) +
            (1 / 2 * h ** 2 * df) +
            (5 / 12 * h ** 3 * d2f) +
            (3 / 8 * h ** 4 * d3f)
        ))

    return dots


def calculate_n(a, b, h, eps=0.0001):
    return int((b - a) / h + eps)
