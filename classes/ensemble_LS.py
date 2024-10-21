from classes.ensemble import Ensemble
from classes.paire import Paire
from helpers.helpers import random_omega, random_vecteur, signe_de_x_prime_transposee_omega

class EnsembleLS(Ensemble):
    # Générer un ensemble linéairement séparable
    def __init__(self, dimension_n, norme_p, *args):
        # Générer un vecteur omega qui va servir à générer l'ensemble
        super().__init__(*args)
        self.omega_correspondant = random_omega(dimension_n)
        self.elements = []

        for _ in range(norme_p):
            x = random_vecteur(dimension_n)
            if signe_de_x_prime_transposee_omega(x, self.omega_correspondant):
                self.elements.append(Paire(x, 1))
            else :
                self.elements.append(Paire(x, -1))

    # Afficher un ensemble LS
    def __str__(self):
        return (super().__str__() +
                '\n' + "omega correspondant : " +
                str(self.omega_correspondant))

if __name__ == "__main__":
    # Test en générant un ensemble
    ensembleLS = EnsembleLS(2, 100)
    ensembleLS.dessiner()
    print(ensembleLS)
