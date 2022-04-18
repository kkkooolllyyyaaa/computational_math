from abc import abstractmethod


# Abstract superclass for approximations
class Approximator:
    # Returns data with: [params], [disp], [func], [r]
    @abstractmethod
    def approximate(self, data):
        pass
