import random

from geneticAlgorithm.algorithsm.generic_genetic_algorithm import GeneticAlgorithm


class QueenGenetic(GeneticAlgorithm):
    def mutate(self, son_gens):
        new_gens = []
        for gen in son_gens:
            val = random.random()
            if val < self.mutation_rate:
                new_gens.append(self.mutate_def(gen))
            else:
                new_gens.append(gen)
        return new_gens