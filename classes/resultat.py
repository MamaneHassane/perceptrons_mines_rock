# On répresente le résultat des tests sous forme d'une classe simple
class Resultat:
    def __init__(self, dimension_n, exemples_p, iterations_it, recouvrement_r):
        self.dimension_n = dimension_n,
        self.exemples_p = exemples_p,
        self.iterations_it = iterations_it,
        self.recouvrement_r = recouvrement_r

    def __str__(self):
        return ("N = " + str(self.dimension_n) +
                " , P = " + str(self.exemples_p) +
                " , IT = " + str(self.iterations_it) +
                " , R = " + str(self.recouvrement_r))