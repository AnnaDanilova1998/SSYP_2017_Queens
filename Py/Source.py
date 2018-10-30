from Py.Population import Population

queens_count = int(input('queens: '))

A = Population(solution_size=queens_count)

unsolved = A.solutions[0].hits

while unsolved:
    A.new_generation()

    print(f'{A.solutions[0].hits} {A.solutions[A.size // 2].hits} {A.solutions[A.size - 1].hits}')


print(A.solutions[0].genotype)
