class genericEvaluator:

    def __init__(self, data, compare_method):
        self.data = data
        self.compare_method = compare_method

    def comapare(self, evaluated_object):
        score  = 0
        for elm in range(len(self.data)):
            score += self.compare_method(self.data[elm], evaluated_object[elm])
        return score