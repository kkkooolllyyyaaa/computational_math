import functions
from methods import RectangleMethod, SimpsonMethod


def exit_msg(message):
    print(message)
    exit(1)
    pass


func1 = functions.function1
func2 = functions.function2
func3 = functions.function3
func4 = functions.function4
func5 = functions.function5


def get_func(number):
    if number == 1:
        return func1
    elif number == 2:
        return func2
    elif number == 3:
        return func3
    elif number == 4:
        return func4
    elif number == 5:
        return func5
    else:
        return None


print('Выберите метод решения:')
print(' 1 — Метод прямоугольников')
print(' 2 — Метод Симпсона')

chosen_method = int(input())
if chosen_method != 1 and chosen_method != 2:
    exit_msg('Данного метода нет в списке')

print('\nВыберите функцию:')
print(' 1 — ' + func1.text)
print(' 2 — ' + func2.text)
print(' 3 — ' + func3.text)
print(' 4 — ' + func4.text)
print(' 5 — ' + func5.text)

chosen_func = int(input())
if chosen_func not in range(1, 6):
    exit_msg('Функции с данным номером нет в списке')

print('\nВведите пределы интегрирования:')
try:
    a = float(input('a: '))
    b = float(input('b: '))
except ValueError:
    exit_msg('Пределы интегрирования должны быть числами')

print("\nВведите погрешность вычисления:")
try:
    eps = float(input('eps: '))
except ValueError:
    exit_msg('Погрешность вычисления должен быть числом')

result = 'None'
if chosen_method == 1:
    solver = RectangleMethod(get_func(chosen_func))
    min_n = 4
    method = int(input('1 - левое, 2 - среднее, 3 - правое: '))
    if method == 1:
        method = 0
    elif method == 2:
        method = 1 / 2
    elif method == 3:
        method = 1
    else:
        exit_msg('Метод прямоугольника может быть только левым, средним или правым')
    result = solver.solve_while(a, b, eps, min_n, method)
else:
    solver = SimpsonMethod(get_func(chosen_func))
    result = solver.solve_while(a, b, eps)

if result is None:
    exit_msg('Произошла ошибка')

print('Результат: ' + str(round(result['result'], 10)))
print('Количество разбиений: ' + str(round(result['n'], 10)))
