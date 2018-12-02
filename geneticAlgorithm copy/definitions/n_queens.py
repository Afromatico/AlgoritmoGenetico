import random
from geneticAlgorithm.definitions.generic_definition import GenericDefinition


class NQueens(GenericDefinition):

    def __init__(self, table_size):
        self.table_size = table_size
        self.empty = "empty"
        self.queen = 'queen'

    def cmp(self, a, b):
        if a == self.queen and b == self.queen:
            return 1
        return 0

    def random_define(self):
        table = [[self.empty for _ in range(self.table_size)] for _ in range(self.table_size)]
        for elm in table:
            elm[random.randint(0, self.table_size-1)] = self.queen
        return table

    def define(self, a):
        listA = []
        for elm in a:
            listA.append(elm)
        return listA

    def mutate(self, gen):
        ret = [self.empty for _ in range(len(gen))]
        ret[random.randint(0, self.table_size - 1)] = self.queen
        return ret

    def divide(self, elm, n_element):
        return elm
