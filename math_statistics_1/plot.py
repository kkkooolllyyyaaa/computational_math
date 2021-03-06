import numpy as np
import matplotlib.pyplot as plt


class StatisticsPlot:
    def __init__(self, statistics):
        self.statistics = statistics
        self.left = statistics.first_ordinal - statistics.sturgess / 2
        self.right = statistics.n_ordinal + statistics.sturgess / 2

    def build_empirical_distribution(self):
        data = self.statistics.selection
        values = [data[0] - self.statistics.sturgess / 2] + data

        fx = self.statistics.empirical_distribution_func
        left = values[0]
        for i in range(len(values)):
            right = values[i]
            height = fx(right).pop()
            plt.plot([left, right], [height, height], c='black')
            plt.plot([left, left], [fx(left).pop(), fx(right).pop()],
                     '--', color='black', linewidth=0.5)
            left = right

        plt.plot([left, left * 1.1], [1.0, 1.0], c='black')
        plt.plot([left, left], [fx(left).pop(), fx(left * 1.1).pop()],
                 '--', color='black', linewidth=0.5)

        plt.xlabel('x')
        plt.ylabel('count')
        plt.yticks(np.arange(0, 1.1, 0.1))
        plt.xticks(np.arange(self.left, self.right, round(self.statistics.sturgess, 2)))
        plt.show()

    def build_frequencies_pol(self):
        intervals = self.statistics.interval_selection
        bins_list = [i['interval']['start'] for i in intervals]
        bins_list.append(intervals[len(intervals) - 1]['interval']['end'])

        values = self.statistics.selection
        n, bins = np.histogram(values, bins_list)
        n = [float(i) for i in n]
        plt.plot(bins[:-1], n, color='black', marker='o')
        plt.xlabel('x')
        plt.ylabel('ni')
        xticks_pos = [i - self.statistics.sturgess / 2 for i in bins_list]
        plt.xticks(xticks_pos, [str(round(i, 2)) for i in bins_list])

        for i in range(len(bins_list) - 1):
            plt.annotate(str(round(n[i], 3)), xy=(bins[i], n[i]), ha='center', va='bottom')
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
        self.build_frequencies_pol()
        self.build_frequencies_hist()
