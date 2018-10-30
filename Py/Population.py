from Py.Solution import Solution
from random import randint


class Population:
    def __init__(self, population_size=250, solution_size=8):
        self.size = population_size
        self.solutions = [Solution(solution_size) for i in range(population_size)]
        self.solutions.sort(key=lambda obj: obj.hits)

    def new_generation(self):
        index = self.size - self.size // 3

        for i in range(self.size):
            self.solutions[i] = Solution.crossing(self.solutions[randint(0, index)], self.solutions[randint(0, index)])

        # if self.solutions[0].hits == 2 and self.solutions[self.size // 2].hits == 2 and randint(0, 10) == 1:
        #     if self.solutions[0].genotype == self.solutions[self.size // 2].genotype:
        #         for i in range(self.size // 10, self.size):
        #             self.solutions[i] = Solution(self.solutions[0].size)

        # for i in range(self.size // 10, self.size):
        #     if randint(0, 10) == 1:
        #         self.solutions[i].mutation()

        self.solutions.sort(key=lambda obj: obj.hits)
