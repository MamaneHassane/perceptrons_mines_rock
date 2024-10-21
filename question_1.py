# On définit plusieurs paires
from algorithmes.apprentissage_batch import apprentissage_batch
from algorithmes.apprentissage_online import apprentissage_online
from classes.ensemble import Ensemble
from classes.paire import Paire
from helpers.helpers import random_omega

if __name__ == "__main__":
    a = Paire((1,1), 1)
    b = Paire((1,0), 1)
    c = Paire((0,1), 1)
    d = Paire((0,0), 0)

    # On définit notre pas alpha
    pas_alpha = 0.2
    # On essaye avec la fonction OU
    fonction_OU = Ensemble(a, b, c, d)
    fonction_OU.dessiner()
    omega = random_omega(2)


    # apprentissage_batch(fonction_OU,2, 0.2, omega)
    apprentissage_online(fonction_OU, pas_alpha, omega)
