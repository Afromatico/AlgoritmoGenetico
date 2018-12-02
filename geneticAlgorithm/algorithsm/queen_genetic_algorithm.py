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

    def genetic_generate(self, score, eval, divide):

        self.populate()

        self.evaluate(eval)

        our_elements = self.eval(score)

        i = 0

        while not our_elements or i > 2000:

            self.select_parents()

            self.reproduction(divide)

            self.evaluate(eval)

            our_elements = self.eval(score)

            i += 1

            if not our_elements and i % 50 == 0:

                self.populate()

                self.evaluate(eval)

                our_elements = self.eval(score)

                i += 1

        return self.bests
