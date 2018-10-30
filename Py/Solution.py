import random


class Solution:
    def __init__(self, n):
        self.errors_number = 0
        self.genotype = []

        self._generate(n)
        self._count_errors_number()

    def _generate(self, n):
        self.genotype = random.shuffle(range(n))

    def _count_errors_number(self):
        pass
