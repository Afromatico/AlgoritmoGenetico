from geneticAlgorithm.algorithsm.generic_eval import genericEvaluator


class QueenEval(genericEvaluator):

    def __init__(self, data, compare_method):
        super().__init__(data, compare_method)

    def compare(self, evaluated_object):
        queens = []

        for i in range(len(evaluated_object)):
            for j in range(len(evaluated_object[i])):
                if self.compare_method("queen", evaluated_object[i][j]):
                    queens.append([1, (i, j)])

        for queen in queens:
            for queen2 in queens:
                if queen[1] != queen2[1]:
                    (i1, j1) = queen[1]
                    (i2, j2) = queen2[1]

                    val1 = (j1 + (i2 - i1))
                    val2 = (j1 - (i2 - i1))

                    if i1 == i2 or j1 == j2 or val1 == j2 or val2 == j2:
                        queen[0] = 0
                        queen2[0] = 0

        score = 0
        for elm in queens:
            score += elm[0]
        return score
