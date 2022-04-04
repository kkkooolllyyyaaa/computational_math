def func1(x):
    return 2 * x


def func2(x):
    return 3 * x


def main_func(x, func):
    return func(x)


def main():
    print(main_func(2, func1))

    print(main_func(2, func2))

    print('h')
