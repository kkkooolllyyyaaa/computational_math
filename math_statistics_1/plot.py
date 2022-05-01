import numpy as np
import matplotlib.pyplot as plt


class StatisticsPlot:
    def __init__(self, statistics):
        self.statistics = statistics
        self.left = statistics.first_ordinal - statistics.sturgess / 2
        self.right = statistics.n_ordinal + statistics.sturgess / 2

    def build_empirical_distribution(self):
        x = np.linspace(self.left, self.right, self.statistics.n * 100)
        fx = self.statistics.empirical_distribution_func
        y = [fx(j).pop() for j in x]
        plt.plot(x, y, color='black')

        plt.xlabel('x')
        plt.ylabel('count')
        plt.xticks(np.arange(self.left, self.right, round(self.statistics.sturgess, 2)))
        plt.show()

    def build_frequencies_polygon(self):
        values = self.statistics.frequencies_polygon_values
        x = [i[0] for i in values]
        y = [i[1] for i in values]

        plt.xlabel('x')
        plt.ylabel('ni')
        plt.plot(x, y, color='black', marker='o')
        plt.xticks(np.arange(self.left, self.right, round(self.statistics.sturgess, 2) / 2))
        plt.show()

    def build_frequencies_hist(self):
        intervals = self.statistics.interval_selection
        bins_list = [i['interval']['start'] for i in intervals]
        bins_list.append(intervals[len(intervals) - 1]['interval']['end'])

        values = self.statistics.selection
        n, bins = np.histogram(values, bins_list)
        n = [float(i) / self.statistics.sturgess for i in n]
        plt.bar(bins[:-1], n, width=np.diff(bins), ec="k", color='white')

        plt.xlabel('x')
        plt.ylabel('ni / h')

        xticks_pos = [i - self.statistics.sturgess / 2 for i in bins_list]
        plt.xticks(xticks_pos, [str(round(i, 2)) for i in bins_list])

        for i in range(len(bins_list) - 1):
            plt.annotate(str(round(n[i], 3)), xy=(bins[i], n[i]), ha='center', va='bottom')
        plt.show()

    def build_graphs(self):
        self.build_empirical_distribution()
        self.build_frequencies_polygon()
        self.build_frequencies_hist()
