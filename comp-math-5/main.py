import numpy as np
import data_loader
import lagrange_pol
import newton_pol
import plot

data = None
data_method = int(input('1 - с файла\n2 - с клавиатуры\n3 - по функции\n'))

if data_method == 1:
    data = data_loader.data_file()
elif data_method == 2:
    data = data_loader.data_console()
elif data_method == 3:
    data = data_loader.data_function()

method_id = int(input('1 - По лагранжу\n2 - По Ньютону\n'))
x = float(input('Введите x: '))

plot_x = np.linspace(min(data['x']), max(data['x']), len(data['x']) * 50)
plot_y = None

if method_id == 1:
    pol = lagrange_pol.interpolate(data)
    print('Приближенный y: ', pol(x).pop())
    plot_y = [pol(xi).pop() for xi in plot_x]
if method_id == 2:
    print('Приближенный y: ', newton_pol.interpolate(data, x))
    plot_y = [newton_pol.interpolate(data, xi) for xi in plot_x]

plot.plot(data, plot_x, plot_y)
