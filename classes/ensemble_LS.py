from classes.ensemble import Ensemble
from classes.paire import Paire
from helpers.helpers import random_omega, random_vecteur, signe_de_x_prime_transposee_omega


class EnsembleLS(Ensemble):
    # Générer un ensemble linéairement séparable
    def __init__(self, dimension_n,  norme_p, *args):
        super().__init__(*args)
        # Générer un vecteur omega qui va servir à générer l'ensemble
        self.omega_correspondant = random_omega(norme_p)
        self.elements = []
        # Générer les éléments grâce à ce omega
        for i in range(norme_p):
            x = random_vecteur(dimension_n)
            # si x'.T(w)>0 => (x,1) , sinon (x,0)
            self.elements.append(Paire(x,1) if signe_de_x_prime_transposee_omega(x, self.omega_correspondant) else Paire(x,0))
    # Afficher un ensemble LS
    def __str__(self):
        return super().__str__() + '\n' + "omega correspondant : " + str(self.omega_correspondant)

# On teste en générant un ensemble
ensembleLS = EnsembleLS(2, 10)
ensembleLS.dessiner()
# On vérifie si notre ensemble est bien LS en l'affichant
