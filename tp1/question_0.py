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
    d = Paire((0,0), -1)
    e = Paire((0,0), -1)
    f = Paire((1,0), -1)
    g = Paire((0, 1), -1)
    h = Paire((2,1), 1)
    i = Paire((0,-1), 1)
    j = Paire((-2, 1), -1)
    k = Paire((0, -2), -1)
    # On définit notre pas alpha
    pas_alpha = 0.2
    # fonction OU
    fonction_OU = Ensemble(a, b, c, d)
    fonction_OU.dessiner()
    # fonction ET
    fonction_ET = Ensemble(a, e, f, g)
    fonction_ET.dessiner()
    # fonction Diapo33
    fonction_Diapo33 = Ensemble(h, i, j, k)
    fonction_Diapo33.dessiner()

    omega = random_omega(2)

    apprentissage_batch(fonction_OU,2, pas_alpha, omega)
    apprentissage_online(fonction_OU, pas_alpha, omega)

    apprentissage_batch(fonction_ET, 2, pas_alpha, omega)
    apprentissage_online(fonction_ET, pas_alpha, omega)

    apprentissage_batch(fonction_Diapo33, 2, pas_alpha, omega)
    apprentissage_online(fonction_Diapo33, pas_alpha, omega)
