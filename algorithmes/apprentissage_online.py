import numpy as np
import random

from classes.paire import Paire
from classes.ensemble import Ensemble
from helpers.helpers import random_vecteur, vecteur_nul, x_prime

# Algorithme d'apprentissage du perceptron version online (incrémentale)
def apprentissage_online(ensemble, dimension_n, pas_alpha):
    # omega random : les exécutions seront différentes
    omega = random_vecteur(dimension_n + 1)
    alpha = pas_alpha
    print("Début...")

    # Liste des indices des paires non traitées et traitées
    index_non_traites = list(range(len(ensemble.elements)))
    index_traites = []

    # Tant que l'ensemble X n'est pas correctement classé
    while not ensemble.est_correctement_classe(omega):
        # Si tous les indices ont été traités, on les remet tous dans la liste non traitée,
        # si l'ensemble n'est pas LS, l'algorithme vas tourner à l'infini,
        # sinon il s'arrêtera à un moment
        if not index_non_traites:
            index_non_traites = index_traites
            index_traites = []

        # Choisir un indice aléatoire parmi les non traités = Choisir une paire
        indice_choisi = random.choice(index_non_traites)
        paire = ensemble.elements[indice_choisi]

        # Déplacer l'indice choisi de index_non_traites à index_traites
        index_non_traites.remove(indice_choisi)
        index_traites.append(indice_choisi)

        if paire.est_bien_predite(omega):  # y = t
            print("La paire", paire.vecteur, "prediction", paire.classement_paire_y(omega),
                  "classe réelle", paire.classification_t, "avec omega à", omega)
        else:  # y != t
            delta_omega = np.dot(alpha * (paire.classification_t - paire.classement_paire_y(omega)), x_prime(paire.vecteur))
            # Version online : on change directement omega
            omega = omega + delta_omega
            print("La paire", paire.vecteur, "prediction actuelle", paire.classement_paire_y(omega),
                  "classe réelle", paire.classification_t, "a causé un changement de omega à", omega)

    print("Toutes les paires ont bien été classées avec omega à", omega, "\nFin de l'exécution")

# On définit plusieurs paires
a = Paire((1, 1), 1)
b = Paire((1, 0), 1)
c = Paire((0, 1), 1)
d = Paire((0, 0), 0)

# On essaye avec la fonction OU
fonction_OU = Ensemble(a, b, c, d)
apprentissage_online(fonction_OU, 2, 0.2)
