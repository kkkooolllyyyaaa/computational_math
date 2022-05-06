import math
from colorama import Fore, Style


def build_interval(start, end, count):
    return {'interval': {'start': start, 'end': end}, 'count': int(count)}


class Statistics:
    def __init__(self, selection):
        self.selection = sorted(selection)
        self.n = len(selection)
        self.expectation = 0
        self.standard_deviation = 0
        self.corrected_standard_deviation = 0
        self.range = 0
        self.first_ordinal = 0
        self.n_ordinal = 0
        self.digits = 3
        self.sturgess = 0
        self.interval_selection = []
        self.interval_distribution_func = None
        self.empirical_distribution_func = None
        self.frequencies_polygon_values = []

    def calculate_expectation(self):
        expect = 0
        for element in self.selection:
            expect += element
        self.expectation = expect / self.n

    def calculate_standard_deviation(self):
        deviation = 0
        for element in self.selection:
            deviation += (element - self.expectation) ** 2
        deviation /= self.n
        self.corrected_standard_deviation = math.sqrt(deviation * self.n / (self.n - 1))
        self.standard_deviation = math.sqrt(deviation)

    def calculate_range(self):
        self.range = self.selection[self.n - 1] - self.selection[0]

    def calculate_ordinals(self):
        self.first_ordinal = self.selection[0]
        self.n_ordinal = self.selection[self.n - 1]

    def calculate_sturgess(self):
        self.calculate_range()
        self.sturgess = self.range / (1 + math.log(float(self.n), 2.0))

    def build_interval_sample(self):
        self.calculate_sturgess()
        h = self.sturgess
        current = self.selection[0] + h / 2.0
        count = 0

        for i in range(len(self.selection)):
            element = self.selection[i]
            count += 1
            if element >= current:
                self.interval_selection.append(build_interval(current - h, current, count))
                count = 0
                current += h
            if (i + 1) == len(self.selection):
                self.interval_selection.append(build_interval(current - h, current, count))

    def build_interval_distribution_function(self):
        self.interval_distribution_func = lambda x: {
            sum([j['count'] if j['interval']['start'] < x else 0
                 for j in self.interval_selection])
        }

    def build_empirical_distribution_function(self):
        self.empirical_distribution_func = lambda x: {
            sum(1 if j < x else 0
                for j in self.selection) / self.n
        }

    def build_frequencies_polygon_values(self):
        for el in self.interval_selection:
            mid = (el['interval']['start'] + el['interval']['end']) / 2
            before = el['interval']['start']
            after = el['interval']['end']
            fx = self.interval_distribution_func
            self.frequencies_polygon_values.append((mid, fx(after).pop() - fx(before).pop()))

    def formatted(self, number):
        space = ''
        if number > 0:
            space = ' '
        formatted = space + str(float(round(number, self.digits)))
        while len(formatted) < 6:
            formatted += '0'
        return formatted

    def print_sample_numerated(self):
        for i in range(len(self.selection)):
            print(i, self.selection[i])
        for element in self.selection:
            print(self.formatted(element), end=' ')
        print()

    def print_sample(self):
        for element in self.selection:
            print(self.formatted(element), end=' ')
        print()

    def print_interval_sample(self):
        for element in self.interval_selection:
            interval_start = self.formatted(element['interval']['start'])
            interval_end = self.formatted(element['interval']['end'])
            interval_str = '[' + interval_start + '; ' + interval_end + ')'
            print(interval_str, '-', element['count'])

    def print_raspr_sample(self):
        n = len(self.interval_selection) - 1
        values = [i['interval']['start'] for i in self.interval_selection]
        values.append(self.interval_selection[n]['interval']['end'])
        print(' 0.000 для x < ' + self.formatted(values[0]))
        for i in range(len(values) - 1):
            left = self.formatted(values[i])
            right = self.formatted(values[i + 1])
            fx = self.formatted(self.empirical_distribution_func(values[i + 1]).pop())
            print(fx + ' для ' + left + ' <= x < ' + right)
        print(' 1.000 для x > ' + self.formatted(values[n]))

    def calculate_all(self):
        self.calculate_ordinals()
        self.calculate_range()
        self.calculate_expectation()
        self.calculate_standard_deviation()
        self.build_interval_sample()
        self.build_interval_distribution_function()
        self.build_empirical_distribution_function()
        self.build_frequencies_polygon_values()

    def print_all(self):
        print(Fore.GREEN + 'Размер выборки:' + Style.RESET_ALL)
        print(self.n)
        print()

        print(Fore.GREEN + 'Вариационные ряд:' + Style.RESET_ALL)
        self.print_sample()
        print()

        print(Fore.GREEN + 'Первая порядковая статистика:' + Style.RESET_ALL)
        print(self.formatted(self.first_ordinal))
        print()

        print(Fore.GREEN + str(self.n) + '-ая порядковая статистика:' + Style.RESET_ALL)
        print(self.formatted(self.n_ordinal))
        print()

        print(Fore.GREEN + 'Размах:' + Style.RESET_ALL)
        print(self.formatted(self.range))
        print()

        print(Fore.GREEN + 'Математическое ожидание:' + Style.RESET_ALL)
        print(self.formatted(self.expectation))
        print()

        print(Fore.GREEN + 'Среднеквадратичное отклонение:' + Style.RESET_ALL)
        print(self.formatted(self.standard_deviation))
        print()

        print(Fore.GREEN + 'Исправленное среднеквадратичное отклонение:' + Style.RESET_ALL)
        print(self.formatted(self.corrected_standard_deviation))
        print()

        print(Fore.GREEN + 'h по формуле Стерджесса:' + Style.RESET_ALL)
        print(self.formatted(self.sturgess))
        print()

        print(Fore.GREEN + 'Интервальный статистический ряд:' + Style.RESET_ALL)
        self.print_interval_sample()
        print()

        print(Fore.GREEN + 'Функция распределения:' + Style.RESET_ALL)
        self.print_raspr_sample()
        print()
