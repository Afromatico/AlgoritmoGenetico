import random
from geneticAlgorithm.definitions.generic_definition import GenericDefinition


class StringFinder(GenericDefinition):

    def __init__(self, size):
        self.abc = "abcdefghijklmnopqrstuvwxyz"
        self.size = size

    def cmp(self, a, b):
        return a == b

    def random_define(self):
        return [self.abc[random.randint(0, len(self.abc) - 1)] for _ in range(self.size)]

    def define(self, a):
        b = ""
        for ele in a:
            b += ele
        return b

    def mutate(self, gen):
        ret = ""
        for _ in gen:
            ret += self.abc[random.randint(0, len(self.abc) - 1)]
        return ret

    def divide(self, elm, n_element):
        list_elm = []
        div = int(len(elm) / n_element) + 1
        partial = ""
        for i in range(len(elm)):
            if i % div != div - 1:
                partial += elm[i]
            else:
                partial += elm[i]
                list_elm.append(partial)
                partial = ""
        list_elm.append(partial)
        return list_elm