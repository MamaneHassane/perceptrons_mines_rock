from algorithmes.apprentissage_batch import apprentissage_batch
from classes.ensemble_LS import EnsembleLS
from helpers.helpers import random_omega, recouvrement_r


def apprendre(dimension_n, exemple_p, pas_eta):
    # On génère un ensemble LS, qui contient son omega correspondant ( professeur )
    ensembleLS = EnsembleLS(dimension_n, exemple_p)
    # On le dessine
    ensembleLS.dessiner()
    # On génère un omega élève
    w_eleve = random_omega(dimension_n)
    # On apprend notre ensemble avec w_eleve
    w_eleve, nb_iterations = apprentissage_batch(ensembleLS, dimension_n, pas_eta, w_eleve)
    # On retourne :
        # les n+1 poids du w_élève
        # le nombre d'itérations
        # le récouvrement entre w_professeur et w_correspondant
    return w_eleve, nb_iterations, recouvrement_r(w_eleve, ensembleLS.omega_correspondant)
