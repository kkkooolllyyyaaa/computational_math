import numpy as np


def dx(x, f, n=1, h=1e-9):
    if n == 0:
        return f(x)
    elif n < 0:
        return None
    elif n == 1:
        return (f(x + h) - f(x)) / h
    else:
        return (dx(x + h, f, n=n - 1) - dx(x, f, n=n - 1)) / h


# Шаговый метод для отделения корней
def step_method(a, b, f, n_iters=1000000):
    answer = ([], [])
    h = max(0.25, (b - a) / n_iters)
    fx = f(a)
    while a < b:
        a += h
        if f(a) * fx <= 0:
            answer[0].append(a - h)
            answer[1].append(a)
        fx = f(a)
    print(answer)
    return answer


def newtons_method(a, b, f, eps):
    x_i = get_x0_newton(a, b, f)
    try:
        iteration = 0
        while True:
            h = f(x_i) / dx(x_i, f)
            x_i_1 = x_i - h
            # Условие сходимости метода
            if abs(x_i_1 - x_i) <= eps:
                break
            iteration += 1
            x_i = x_i_1
        print_newton(x_i, f(x_i), dx(x_i, f), x_i_1, abs(x_i_1 - x_i))
        return [x_i, f(x_i), dx(x_i, f), x_i_1, abs(x_i_1 - x_i)], iteration
    except ValueError:
        print("Incorrect Value")


def get_x0_newton(a, b, f):
    # Выбор начального приближения
    if f(a) * dx(a, f, n=2) > 0:
        print('Начальное приближение a')
        return a
    else:
        print('Начальное приближение b')
        return b


def print_newton(x_k, f_x_k, dfx_k, x_k_1, accuracy):
    print('x_k =', number(x_k))
    print('f(x_k) =', number(f_x_k))
    print('f\'(x_k) =', number(dfx_k))
    print('x_k+1 =', number(x_k_1))
    print('|x_k - x_k+1| =', number(accuracy))


def simple_iteration_method(a, b, f, eps, max_iter=1000):
    cur = a
    max_dx = dx(cur, f)
    while cur < b:
        cur_dx = dx(cur, f)
        max_dx = max(max_dx, cur_dx)
        cur += (b - a) / 10000
    lamb = -1 / max_dx

    def phi(x):
        return x + lamb * f(x)

    iters = 0
    x0 = a
    xi = phi(x0)

    while (abs(xi - x0) > eps or abs(f(xi)) > eps) and iters < max_iter:
        x0 = xi
        xi = phi(x0)
        iters += 1
    if abs(xi - x0) > eps:
        print('Добиться точности', eps, 'при max_iter =', max_iter, 'не удалось')
    print_sim((x0, xi, phi(xi), f(xi), abs(xi - x0), iters))
    return x0, xi, phi(xi), f(xi), abs(xi - x0), iters


def print_sim(answer):
    print('x_i =', number(answer[0]))
    print('x_i+1 =', number(answer[1]))

    print('phi(x_i+1) =', number(answer[2]))
    print('f(x_i+1) =', number(answer[3]))

    print('|x_i+1 - x_i| =', answer[4])
    print('Всего итераций: ', answer[5])


def number(x):
    return round(x, 5)
