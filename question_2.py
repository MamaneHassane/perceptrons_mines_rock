from algorithmes.apprentissage_batch import apprentissage_batch
from algorithmes.apprentissage_online import apprentissage_online
from classes.ensemble_LS import EnsembleLS
from helpers.helpers import random_omega, recouvrement_r


def apprendre(apprentissage, ensemble,  dimension_n, pas_eta):
    # On génère un ensemble LS, qui contient son omega correspondant ( professeur )
    ensemble_ls = ensemble
    # On le dessine : A éviter, dessiner un ensemble de plus de 100 points prend beaucoup de temps
    # ensemble.dessiner()
    # On génère un omega élève
    w_eleve = random_omega(dimension_n)
    # On apprend notre ensemble avec w_eleve
    if apprentissage==0:
        print("batch..........................")
        w_eleve, nb_iterations = apprentissage_batch(ensemble, dimension_n, pas_eta, w_eleve)
    elif apprentissage==1:
        print("online..........................")
        w_eleve, nb_iterations = apprentissage_online(ensemble, pas_eta, w_eleve)
    else:
        print("Méthode d'apprentissage non réconnue !")
        exit()
    # On retourne :
    # les n+1 poids du w_élève
    # le nombre d'itérations
    # le récouvrement entre w_professeur et w_correspondant
    return w_eleve, nb_iterations, recouvrement_r(w_eleve, ensemble.omega_correspondant)

if __name__ == "__main__":
    dimension_test = 2
    ensemble_d_apprentissage = EnsembleLS(dimension_test, 5000)
    eta = 0.5

    w_eleve_1, nb_iterations_1, recouvrement = apprendre(1, ensemble_d_apprentissage, dimension_test, eta)
    print("w_eleve : ", w_eleve_1,
          "nb_iterations : ", nb_iterations_1,
          "recouvrement : ", recouvrement_r(w_eleve_1,ensemble_d_apprentissage.omega_correspondant)
        )
