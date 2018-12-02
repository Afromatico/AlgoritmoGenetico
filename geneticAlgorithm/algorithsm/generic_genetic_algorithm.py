import random

class GeneticAlgorithm:

    def __init__(self, random_define, define, mutate_def, population=500, n_parents=13, number_of_genes=10, mutation_rate=0.001):
        self.data = []
        self.random_define = random_define
        self.define = define
        self.population = population
        self.parents = []
        self.n_parents = n_parents
        self.number_of_genes = number_of_genes
        self.mutation_rate = mutation_rate
        self.mutate_def = mutate_def
        self.bests = []

    def populate(self):
        self.data = []
        for _ in range(self.population):
            element = [self.define(self.random_define()), 0]
            self.data.append(element)

    def evaluate(self, eval):
        for i in range(len(self.data)):
            self.data[i][1] = eval(self.data[i][0])

    def select_parents(self):
        self.parents = []
        for _ in range(len(self.data)):
            parent = [self.tournament(self.data,self.n_parents), self.tournament(self.data,self.n_parents)]
            self.parents.append(parent)

    def tournament(self, pop, k):
        best = pop[random.randint(0,len(pop)-1)]
        for _ in range(k-1):
            eval = pop[random.randint(0,len(pop)-1)]
            if eval[1]>= best[1]:
                if eval[1]> best[1]:
                    best = eval
                else:
                    if [random.randint(0, 1)]:
                        best = eval
        return best[0]

    def reproduction(self, divide):
        for i in range(self.population):
            parent = [divide(self.parents[i][0], self.number_of_genes), divide(self.parents[i][1], self.number_of_genes)]
            son_gens = []
            for j in range(self.number_of_genes):
                son_gens.append(parent[random.randint(0,1)][j])
            son_gens = self.mutate(son_gens)
            self.data[i] = [self.define(son_gens), 0]

    def mutate(self, son_gens):
        new_gens = []
        for gen in son_gens:
            new_gen = ""
            for elm in gen:
                val = random.random()
                if val < self.mutation_rate:
                    new_gen += self.mutate_def(elm)
                else:
                    new_gen += elm
            new_gens.append(new_gen)
        return new_gens

    def eval(self, expected):
        good_elements = []
        best = [None, 0]
        for elm in self.data:
            if elm[1]>best[1]:
                best = elm
            if elm[1]>=expected:
                good_elements.append(elm[0])
        self.bests.append(best)
        return good_elements

    def genetic_generate(self, score, eval, divide):

        self.populate()

        self.evaluate(eval)

        our_elements = self.eval(score)

        i = 0

        while not our_elements or i > 1000:

            self.select_parents()

            self.reproduction(divide)

            self.evaluate(eval)

            our_elements = self.eval(score)

            i+= 1

        return self.bests