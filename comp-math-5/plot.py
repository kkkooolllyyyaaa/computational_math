import matplotlib.pyplot as plt


def plot(data, plot_x, plot_y):
    plt.plot(data['x'], data['y'], 'o',
             plot_x, plot_y)
    plt.show(block=False)
