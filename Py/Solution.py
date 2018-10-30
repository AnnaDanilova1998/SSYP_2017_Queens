import random


class Solution:
    def __init__(self, n):
        self.hits = 0
        self.size = n
        self.genotype = [i for i in range(n)]

        random.shuffle(self.genotype)
        self._count_errors_number()

    @staticmethod
    def crossing(parent_1, parent_2):
        new_solution = Solution(parent_1.size)

        for i in range(parent_1.size):
            if parent_1.genotype[i] == parent_2.genotype[i]:
                index = new_solution.genotype.index(parent_1.genotype[i])

                new_solution.genotype[i], new_solution.genotype[index] = new_solution.genotype[index], \
                                                                         new_solution.genotype[i]

        return new_solution

    def _count_errors_number(self):
        for i in range(self.size):

            # lower right

            x, y = i + 1, self.genotype[i] + 1

            while 0 <= x < self.size and 0 <= y < self.size:
                if self.genotype[x] == y:
                    self.hits += 1
                    break
                else:
                    x += 1
                    y += 1

            # lower left

            x, y = i + 1, self.genotype[i] - 1

            while 0 <= x < self.size and 0 <= y < self.size:
                if self.genotype[x] == y:
                    self.hits += 1
                    break
                else:
                    x += 1
                    y -= 1

            # top right

            x, y = i - 1, self.genotype[i] + 1

            while 0 <= x < self.size and 0 <= y < self.size:
                if self.genotype[x] == y:
                    self.hits += 1
                    break
                else:
                    x -= 1
                    y += 1

            # top left

            x, y = i - 1, self.genotype[i] - 1

            while 0 <= x < self.size and 0 <= y < self.size:
                if self.genotype[x] == y:
                    self.hits += 1
                    break
                else:
                    x -= 1
                    y -= 1

    def mutation(self):
        for k in range(2):
            i, j = random.randint(self.size)
            self.genotype[i], self.genotype[j] = self.genotype[j], self.genotype[i]
