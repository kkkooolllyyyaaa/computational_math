import math


def exit_msg(message):
    print(message)
    exit(1)
    pass


class Func:
    def __init__(self, func, text):
        self.func = func
        self.text = text


def f1(x):
    return x ** 3 - 2 * (x ** 2) - 5 * x + 24


function1 = Func(f1, 'x^3 - 2x^2 - 5x+24')


def f2(x):
    return (math.sin(x)) ** 2


function2 = Func(f2, 'sin^2(x)')


def f3(x):
    if x == 0:
        exit_msg('Нельзя взять логарифм от 0')
    return math.log(x * x)


function3 = Func(f3, 'ln(x^2)')


def f4(x):
    if x == 0:
        exit_msg('Нельзя делить на 0')
    return 1 / (x ** 2) + 7 * x


function4 = Func(f4, '1/x^2 + 7*x')


def f5(x):
    return x ** 2


function5 = Func(f5, 'x^2')
