import numpy as np

from helpers.helpers import transposee, x_prime


class Paire:
    # Créer une paire
    def __init__(self, vecteur, classification):
        self.vecteur = vecteur
        self.classification_t = classification
    # Afficher la paire
    def __str__(self):
        return '[ ' + str(self.vecteur) + '-->' + str(self.classification_t) + ' ]'
    # Calculer transposee(w).x' pour une paire
    def transposee_omega_x_prime(self, omega):
        return np.dot(transposee(omega), x_prime(self.vecteur))
    # Savoir si transposee(w).x' pour une paire est positif
    def classement_paire_y(self, omega):
        if self.transposee_omega_x_prime(omega) > 0:
            return 1
        else:
            return -1
    # Savoir si une paire est bien classée par le perceptron par rapport a sa classification t
    def est_bien_predite(self, omega):
        if self.classement_paire_y(omega) == self.classification_t:
            return True
        else:
            return False