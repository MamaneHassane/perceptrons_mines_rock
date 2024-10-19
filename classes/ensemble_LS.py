import matplotlib.pyplot as plt

from classes.ensemble import Ensemble
from classes.paire import Paire
from helpers.helpers import random_omega, random_vecteur, signe_de_x_prime_transposee_omega

class EnsembleLS(Ensemble):
    # Générer un ensemble linéairement séparable avec un équilibre entre les classes
    def __init__(self, dimension_n, norme_p, *args):
        # Générer un vecteur omega qui va servir à générer l'ensemble
        super().__init__(*args)
        self.omega_correspondant = random_omega(dimension_n)
        self.elements = []

        # Compteurs pour suivre le nombre de paires classées 0 et 1
        count_class_0 = 0
        count_class_1 = 0

        # Générer les éléments jusqu'à obtenir un équilibre des classes
        while len(self.elements) < norme_p:
            x = random_vecteur(dimension_n)
            classification = 1 if signe_de_x_prime_transposee_omega(x, self.omega_correspondant) == True else 0
            # Ajouter la paire en s'assurant de maintenir un équilibre entre les deux classes
            if classification == 1 and count_class_1 < norme_p // 2:
                self.elements.append(Paire(x, classification))
                count_class_1 += 1
            elif classification == 0:
                self.elements.append(Paire(x, classification))
                count_class_0 += 1
    # Afficher un ensemble LS
    def __str__(self):
        return (super.__str__(self) +
                '\n' + "omega correspondant : " +
                str(self.omega_correspondant))

# Test en générant un ensemble
ensembleLS = EnsembleLS(2, 7)
ensembleLS.dessiner()
