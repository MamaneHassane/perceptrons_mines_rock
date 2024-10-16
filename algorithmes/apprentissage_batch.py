import numpy as np

from classes.Paire import Paire
from classes.ensemble import Ensemble
from helpers.helpers import random_vecteur, vecteur_nul, x_prime


# Algorithme d'apprentissage du perceptron version batch
def apprentissage_batch(ensemble, dimension_n):
    # omega random
    omega = random_vecteur(dimension_n+1)
    # alpha = 0.2
    alpha = 0.2
    # Tant que l'ensemble X, n'est pas correctement classé
    while not(ensemble.est_correctement_classe(omega)):
        # delta_omega est nul au debut
        delta_omega = vecteur_nul(dimension_n)
        # Pour toutes les paires, vérifier si elles sont bien prédites
        for paire in ensemble.elements:
            if not(paire.est_bien_predite(omega)):
                delta_omega = np.dot(alpha*(paire.classification - paire.classement_paire(omega) ),x_prime(paire.vecteur))
                print("Nouveau delta_omega", delta_omega)
                omega = omega + delta_omega
                print("La paire", paire.vecteur, " prediction ", paire.classement_paire(omega), "classe réelle ", paire.classification,
                      " cause un changement de omega à ", omega)
            else:
                print("La paire", paire.vecteur, " prediction ", paire.classement_paire(omega), "classe réelle ", paire.classification,
                      "avec omega à ", omega)
    print("Toutes les paires ont bien classées !")

# On définit plusieurs ensembles
a = Paire((1,1), 1)
b = Paire((1,0), 0)
c = Paire((0,1), 0)
d = Paire((0,0), 1)

# On essaye avec la fonction OU
fonction_OU = Ensemble(a, b, c, d)
apprentissage_batch(fonction_OU,2)

