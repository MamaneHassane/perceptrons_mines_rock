from algorithmes.apprentissage_batch import apprentissage_batch
from algorithmes.apprentissage_online import apprentissage_online
from classes.ensemble_LS import EnsembleLS, ensembleLS
from helpers.helpers import random_omega, recouvrement_r


def apprendre(apprentissage, ensemble,  dimension_n, pas_eta):
    # On génère un ensemble LS, qui contient son omega correspondant ( professeur )
    ensemble_ls = ensemble
    # On le dessine
    ensembleLS.dessiner()
    # On génère un omega élève
    w_eleve = random_omega(dimension_n)
    # On apprend notre ensemble avec w_eleve
    if apprentissage=="batch":
        w_eleve, nb_iterations = apprentissage_batch(ensembleLS, dimension_n, pas_eta, w_eleve)
    elif apprentissage=="online":
        w_eleve, nb_iterations = apprentissage_online(ensembleLS, dimension_n, pas_eta, w_eleve)
    else:
        print("Méthode d'apprentissage non réconnue !")
        return
    # On retourne :
    # les n+1 poids du w_élève
    # le nombre d'itérations
    # le récouvrement entre w_professeur et w_correspondant
    print("w_eleve : ", w_eleve,
          "nb_iterations : ", nb_iterations,
          "recouvrement : ", recouvrement_r(w_eleve,ensembleLS.omega_correspondant)
          )
    return w_eleve, nb_iterations, recouvrement_r(w_eleve, ensembleLS.omega_correspondant)

ensemble_d_apprentissage = EnsembleLS(2, 50)
eta = 0.5
apprendre("jn", ensemble_d_apprentissage, 2, eta)