import numpy as np

from classes.paire import Paire
from classes.ensemble import Ensemble
from helpers.helpers import random_vecteur, vecteur_nul, x_prime

# Algorithme d'apprentissage du perceptron version batch
def apprentissage_batch(ensemble, dimension_n, pas_alpha):
    # omega random : les exécutions seront différentes
    omega = random_vecteur(dimension_n+1)
    # alpha, le pas d'apprentissage
    alpha = pas_alpha
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
        omega = omega + delta_omega
        print("La paire", paire.vecteur, " prediction actuelle ", paire.classement_paire_y(omega), "classe réelle ",
              paire.classification_t,
              " à causé un changement de omega à ", omega)
    print("Toutes les paires ont bien classées avec omega à ",
          omega,
          "\nFin de l'éxecution")

# On définit plusieurs paires
a = Paire((1,1), 1)
b = Paire((1,0), 1)
c = Paire((0,1), 1)
d = Paire((0,0), 0)

# On essaye avec la fonction OU
fonction_OU = Ensemble(a, b, c, d)
apprentissage_batch(fonction_OU,2, 0.2)

