import sys
import matplotlib.pyplot as plt
import numpy as np
import time
# import pandas

from geneticAlgorithm.algorithsm.queen_eval import QueenEval
from geneticAlgorithm.algorithsm.queen_genetic_algorithm import QueenGenetic
from geneticAlgorithm.definitions.n_queens import NQueens

score = int(sys.argv[1])

nq = NQueens(score)

gga = QueenGenetic(nq.random_define, nq.define, nq.mutate, number_of_genes=score, population=score * 100,
                   n_parents=score, mutation_rate=float(sys.argv[2]))

qe = QueenEval(score, nq.cmp)

start = time.time()

elements = gga.genetic_generate(score, qe.compare, nq.divide)

end = time.time()

plotValues = [elm[1] for elm in elements]

plt.plot(range(0, len(plotValues)), plotValues)

plt.show()

plt.savefig('grafico' + str(time.time()) + '.png')

table = np.array([[val2 == 'queen' for val2 in val1] for val1 in elements[len(elements) - 1][0]])

print(table)

print("tiempo de ejecucion: " + str(end - start))

# # Codigo obtenido de:
# # https://stackoverflow.com/questions/10194482/custom-matplotlib-plot-chess-board-like-table-with-colored-cells
# # Make a 9x9 grid...
# nrows, ncols = score, score
#
# from matplotlib.table import Table
#
#
# def checkerboard_table(data, fmt='{:.2f}', bkg_colors=['yellow', 'white']):
#     fig, ax = plt.subplots()
#     ax.set_axis_off()
#     tb = Table(ax, bbox=[0, 0, 1, 1])
#
#     nrows, ncols = data.shape
#     width, height = 1.0 / ncols, 1.0 / nrows
#
#     # Add cells
#     for (i, j), val in np.ndenumerate(data):
#         # Index either the first or second item of bkg_colors based on
#         # a checker board pattern
#         idx = [j % 2, (j + 1) % 2][i % 2]
#         color = bkg_colors[idx]
#
#         tb.add_cell(i, j, width, height, text=fmt.format(val),
#                     loc='center', facecolor=color)
#
#     # Row Labels...
#     for i, label in enumerate(data.index):
#         tb.add_cell(i, -1, width, height, text=label, loc='right',
#                     edgecolor='none', facecolor='none')
#     # Column Labels...
#     for j, label in enumerate(data.columns):
#         tb.add_cell(-1, j, width, height / 2, text=label, loc='center',
#                     edgecolor='none', facecolor='none')
#     ax.add_table(tb)
#     return fig
#
#
# data = pandas.DataFrame(np.random.random((nrows, ncols)),
#                         columns=[chr(i + 65) for i in range(ncols)])
# checkerboard_table(data)
# plt.show()
