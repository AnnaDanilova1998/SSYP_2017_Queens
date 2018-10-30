import random


class Solution:
    def __init__(self, n):
        self.hits = 0
        self.genotype = [i for i in range(n)]

        random.shuffle(self.genotype)
        self._count_errors_number()

    def _count_errors_number(self):
        size = len(self.genotype)

        for i in range(size):

            # lower right

            x, y = i + 1, self.genotype[i] + 1

            while 0 <= x < size and 0 <= y < size:
                if self.genotype[x] == y:
                    self.hits += 1
                    break
                else:
                    x += 1
                    y += 1

            # lower left

            x, y = i + 1, self.genotype[i] - 1

            while 0 <= x < size and 0 <= y < size:
                if self.genotype[x] == y:
                    self.hits += 1
                    break
                else:
                    x += 1
                    y -= 1

            # top right

            x, y = i - 1, self.genotype[i] + 1

            while 0 <= x < size and 0 <= y < size:
                if self.genotype[x] == y:
                    self.hits += 1
                    break
                else:
                    x -= 1
                    y += 1

            # top left

            x, y = i - 1, self.genotype[i] - 1

            while 0 <= x < size and 0 <= y < size:
                if self.genotype[x] == y:
                    self.hits += 1
                    break
                else:
                    x -= 1
                    y -= 1
