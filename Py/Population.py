from Py.Solution import Solution
from pprint import pprint


class Population:
    def __init__(self, population_size=250, solution_size=8):
        self.size = population_size
        self.solutions = [Solution(solution_size) for i in range(population_size)]
        self.solutions.sort(key=lambda obj: obj.hits)
