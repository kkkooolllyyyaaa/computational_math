from sympy import *


def f(number):
    if number == "1":
        return lambda x, y: 4 - x ** 2 - y ** 2, \
               lambda x, y: 3 * x ** 2 - y


def system_newtons_method():
    f1 = 'x**2 + y**2 - 4'
    f2 = "-3*x**2 + y"
    print('Выбранные функции')
    print(f1, '= 0')
    print(f2, '= 0')
    eps = float(input('Введите точность eps: '))
    x, y = symbols("x y")
    x1, y1 = Symbol('x1'), Symbol('y1')
    x0 = 10
    y0 = 20
    # Матрица якоби частных производных
    a = Matrix([f1, f2]).jacobian([x, y])
    # Вектор столбец неизвестных
    b = Matrix([["x1"], ["y1"]])
    # Составляю матрицу для решение СЛАУ
    M = a * b
    func1, func2 = f("1")
    iter = 0
    print('Начальное приближение:')
    print(x0, y0)
    while True:
        c = M.subs([(x, x0), (y, y0)])
        fu1 = func1(x0, y0)
        fu2 = func2(x0, y0)
        equation = Eq(c[0], fu1), Eq(c[1], fu2)
        ans = solve(equation, ['x1', 'y1'], dict=True)
        ans1 = ans[0][x1]
        ans2 = ans[0][y1]
        x_1 = x0 + ans1
        y_1 = y0 + ans2
        print(float(x_1), float(y_1))
        if abs(x_1 - x0) <= eps:
            print('x', '\t\t\t\t y')
            print(float(x_1), float(y_1))
            break
        x0 = x_1
        y0 = y_1
        iter += 1
    print('Количество итераций')
    print(iter)
