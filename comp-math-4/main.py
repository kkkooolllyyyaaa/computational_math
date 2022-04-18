import numpy as np

from input import read_console
from input import read_file
from plot import plot

import least_squares.LinearApproximator as linear
import least_squares.Pol2Approximator as pol2
import least_squares.Pol3Approximator as pol3
import least_squares.PowApproximator as pow
import least_squares.ExpApproximator as exp
import least_squares.LogApproximator as log

'-----------------------------------------------------------------------------'
format_len = 30
format_print_len = 60
digits = 3
inf = 1e100

print('[file] - прочитать с файла', '[console] - прочитать с консоли', sep='\n')
read_mode = input()

table = None
if read_mode == 'file':
    table = read_file()
elif read_mode == 'console':
    table = read_console()
else:
    print('Неверный формат режима чтения')
    exit(1)

n = len(table['x'])
functions = [linear.LinearApproximator(), pol2.Pol2Approximator(), pol3.Pol3Approximator(),
             exp.ExpApproximator(), pow.PowApproximator(), log.LogApproximator()]
results = [i.approximate(table) for i in functions]

'-----------------------------------------------------------------------------'
st_dev = []
for i in results:
    if i is not None:
        st_dev.append((i['disp'] / n) ** (1 / 2))
    else:
        st_dev.append(None)

print(20 * ' ' + '[Среднеквадратичные отклонение]' + ' ' * 3 + '[Мера отклонения]')

for i in range(len(results)):
    res = (str(i + 1) + ') ' +
           functions[i].description +
           ' ' * (format_len - len(functions[i].description)))
    if st_dev[i] is not None:
        res += str(round(st_dev[i], digits))
    else:
        res += 'None'
    S = None
    if results[i] is not None:
        S = round(results[i]['disp'], digits)
    res += ' ' * (format_print_len - len(res)) + str(S)
    print(res)
print('\n')

best_i = 0
best_dev = inf
for i in range(len(st_dev)):
    if st_dev[i] is None:
        continue
    if st_dev[i] < best_dev:
        best_dev = st_dev[i]
        best_i = i

'-----------------------------------------------------------------------------'
print('Наилучшая аппроксимация: ')
print(functions[best_i].description + ': ' + functions[best_i].f)
print()

print('Параметры [a0, a1, ... ]:')
print(results[best_i]['params'])
print()

print('Среднеквадратичное отклонение:')
print(round(best_dev, digits))
print()

'-----------------------------------------------------------------------------'
if type(functions[best_i]) == type(linear.LinearApproximator()):
    print('Коэффициент Корреляции Пирса:')
    kkp = round(results[best_i]['r'], digits)
    print(kkp)
    if kkp > 0:
        print('Связь прямая')
    else:
        print('Связь обратная')
    kkp = abs(kkp)
    if kkp < 0.3:
        print("Связь слабая")
    elif 0.3 <= kkp < 0.5:
        print("Связь умеренная")
    elif 0.5 <= kkp < 0.7:
        print("Связь заметная")
    elif 0.7 <= kkp < 0.9:
        print("Связь высокая")
    elif 0.9 <= kkp < 0.99:
        print("Связь весьма высокая")

'-----------------------------------------------------------------------------'
plot_x = np.linspace(np.min(table['x']), np.max(table['y']), 100)
plot_y = []
labels = []

for i in range(len(results)):
    result = results[i]
    if result is None:
        continue
    plot_y.append([result['func'](x) for x in plot_x])
    labels.append(result['legend'])
    # labels.append(functions[i].f)
plot(table['x'], table['y'], plot_x, plot_y, labels)
plot(table['x'], table['y'], plot_x,
     [[results[best_i]['func'](x) for x in plot_x]],
     ['Наилучшая аппроксимация:\n' + results[best_i]['legend']])

'-----------------------------------------------------------------------------'
R = 0
div1, div2 = 0, 0
for i in range(n):
    R += (table['y'][i] - results[best_i]['func'](table['x'][i])) ** 2
    div1 += results[best_i]['func'](table['x'][i]) ** 2
    div2 += results[best_i]['func'](table['x'][i])

print('Достоверность аппроксимации:')
print(1 - R / (div1 - 1 / n * (div2 ** 2)))
