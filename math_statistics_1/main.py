from Statistics import Statistics
from plot import StatisticsPlot
from input import read_file

sample = read_file('file/sample1')
statistics = Statistics(sample)

statistics.calculate_all()
statistics.print_all()

graphs = StatisticsPlot(statistics)
graphs.build_graphs()
