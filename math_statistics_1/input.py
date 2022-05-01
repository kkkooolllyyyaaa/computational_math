N_ERROR = 'Значения n должно быть неотрицательным целыми числом'
line_error = 'Должно быть введено не менее n вещественных чисел, разделенных пробельными символами'


def exit_msg(message):
    print(message)
    exit(1)
    pass


def read_file(filename):
    with open(filename) as file:
        data = []
        try:
            while True:
                line = file.readline()
                if line == "":
                    break
                values = [float(i) for i in line.strip().split()]
                for element in values:
                    data.append(element)
            return data
        except ValueError:
            exit_msg(line_error)
