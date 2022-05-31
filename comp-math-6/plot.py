import matplotlib.pyplot as plt


def plot(x1, y1, acc_x, acc_y, x2=None, y2=None):
    plt.plot(x1, y1, label="y1(x)")
    plt.plot(acc_x, acc_y, label="cor_y(x)")

    if x2 is not None and y2 is not None:
        plt.plot(x2, y2, label="y2(x)")
    plt.legend()
    plt.show(block=False)
