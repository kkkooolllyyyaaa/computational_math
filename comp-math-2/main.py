import data_loader
import methods
import system_methods


def error_exit_message(message):
    print(message)
    exit(1)


def input_error_exit():
    error_exit_message('Неправильный ввод')


print('1 - Решить одно уравнение\n2 - Решить систему уравнений')
solve_id = int(input())
if solve_id == 1:
    print('1 - Метод Ньютона\n2 - Метод простой итерации')
    method_id = int(input())

    data = data_loader.data_console()
    answer = None

    roots = methods.step_method(data['a'], data['b'], data['f'])
    print('Всего найдено', len(roots[0]), 'корней:')
    answers = []
    method = None
    if method_id == 1:
        method = methods.newtons_method
    elif method_id == 2:
        method = methods.simple_iteration_method
    else:
        input_error_exit()
    for i in range(len(roots[0])):
        print('a =', methods.number(roots[0][i]), 'b =', methods.number(roots[1][i]))
        answers.append(method(roots[0][i], roots[1][i], data['f'], data['eps']))
        print()

elif solve_id == 2:
    system_methods.system_newtons_method()
    pass
else:
    input_error_exit()
