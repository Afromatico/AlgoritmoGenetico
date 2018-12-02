from math import sqrt

import matplotlib.pyplot as plt

from geneticAlgorithm.algorithsm.queen_eval import QueenEval
from geneticAlgorithm.algorithsm.queen_genetic_algorithm import QueenGenetic
from geneticAlgorithm.definitions.n_queens import NQueens


score = 10

nq = NQueens(score)

gga = QueenGenetic(nq.random_define, nq.define, nq.mutate, number_of_genes=score, population=score*100, n_parents=score, mutation_rate=0.1)

qe = QueenEval(score, nq.cmp)

elements = gga.genetic_generate(score, qe.compare, nq.divide)

plotValues = [elm[1] for elm in elements]

plt.plot(range(0,len(plotValues)), plotValues)

plt.show()

print(elements[len(elements)-1])

# print(qe.compare([['queen', 'empty', 'empty', 'empty'],
#                   ['empty', 'empty', 'empty', 'queen'],
#                   ['empty', 'queen', 'empty', 'empty'],
#                   ['empty', 'empty', 'empty', 'queen']]))