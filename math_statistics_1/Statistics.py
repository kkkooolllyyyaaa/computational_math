import math


def build_interval(start, end, count):
    return {'interval': {'start': start, 'end': end}, 'count': int(count)}


class Statistics:
    def __init__(self, selection):
        self.selection = sorted(selection)
        self.n = len(selection)
        self.expectation = 0
        self.standard_deviation = 0
        self.range = 0
        self.first_ordinal = 0
        self.n_ordinal = 0
        self.digits = 3
        self.sturgess = 0
        self.interval_selection = []
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
            deviation += (self.expectation - element) ** 2
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

    def build_empirical_distribution_function(self):
        self.empirical_distribution_func = lambda x: {
            sum([j['count'] if j['interval']['start'] < x else 0
                 for j in self.interval_selection])
        }

    def build_frequencies_polygon_values(self):
        for el in self.interval_selection:
            mid = (el['interval']['start'] + el['interval']['end']) / 2
            before = mid - self.sturgess
            fx = self.empirical_distribution_func
            self.frequencies_polygon_values.append((mid, fx(mid).pop() - fx(before).pop()))

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

    def calculate_all(self):
        self.calculate_ordinals()
        self.calculate_range()
        self.calculate_expectation()
        self.calculate_standard_deviation()
        self.build_interval_sample()
        self.build_empirical_distribution_function()
        self.build_frequencies_polygon_values()

    def print_all(self):
        print('Размер выборки:')
        print(self.n)
        print()

        print('Вариационные ряд:')
        self.print_sample()
        print()

        print('Первая порядковая статистика:')
        print(self.formatted(self.first_ordinal))
        print()

        print(str(self.n) + '-ая порядковая статистика:')
        print(self.formatted(self.n_ordinal))
        print()

        print('Размах:')
        print(self.formatted(self.range))
        print()

        print('Оценка математического ожидания:')
        print(self.formatted(self.expectation))
        print()

        print('Оценка среднеквадратичного отклонения:')
        print(self.formatted(self.standard_deviation))
        print()

        print('h по формуле Стерджесса:')
        print(self.formatted(self.sturgess))
        print()

        print('Интервальный статистический ряд:')
        self.print_interval_sample()
        print()
