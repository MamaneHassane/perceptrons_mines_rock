import numpy as np

from classes.paire import Paire
from classes.ensemble import Ensemble
from helpers.helpers import random_vecteur, vecteur_nul, x_prime, random_omega


# Algorithme d'apprentissage du perceptron version batch
# On va retourner le vecteur omega, ensemble des poids, qui va nous servir à classer de nouvelles données
def apprentissage_batch(ensemble, dimension_n, pas_alpha, omega_random):
    # omega random : les exécutions seront différentes
    omega = omega_random
    # alpha, le pas d'apprentissage
    alpha = pas_alpha
    # le nombre d'itérations
    nb_iterations = 0
    print("Début...")
    # Tant que l'ensemble X, n'est pas correctement classé
    while not(ensemble.est_correctement_classe(omega)):
        # delta_omega est nul au debut
        delta_omega = vecteur_nul(dimension_n+1)
        # Pour toutes les paires, vérifier si elles sont bien prédites
        for paire in ensemble.elements:
            if paire.est_bien_predite(omega): # y = t
                print("La paire", paire.vecteur, " prediction ", paire.classement_paire_y(omega), "classe réelle ",
                      paire.classification_t,
                      "avec omega à ", omega)
            else: # y != t
                delta_omega = delta_omega + np.dot(alpha * (paire.classification_t - paire.classement_paire_y(omega)),
                                     x_prime(paire.vecteur))
        # Version batch : on change omega après avoir tout parcouru
        omega = omega + delta_omega
        # On incrémente le nombre d'itérations
        nb_iterations += 1
        print("Nouveau omega après 1 tour: ", omega)
    print("Toutes les paires ont bien classées avec omega à ",
          omega,
          "\nFin de l'éxecution")
    return omega, nb_iterations

# On définit plusieurs paires
a = Paire((1,1), 1)
b = Paire((1,0), 1)
c = Paire((0,1), 1)
d = Paire((0,0), 0)

# On essaye avec la fonction OU
fonction_OU = Ensemble(a, b, c, d)
fonction_OU.dessiner()
omega = random_omega(2)
apprentissage_batch(fonction_OU,2, 0.2, omega)

