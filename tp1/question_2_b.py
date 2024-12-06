from classes.ensemble_LS import EnsembleLS
from helpers.helpers import random_omega, recouvrement_r
from question_2 import apprendre

if __name__ == "__main__":

    dimension_test = 4
    ensemble_d_apprentissage = EnsembleLS(dimension_test, 100)
    eta = 0.5
    methode_dapprentissage = 0  # batch

    w_eleve_1, nb_iterations_1, recouvrement = apprendre(methode_dapprentissage, ensemble_d_apprentissage,
                                                         dimension_test, eta)
    print("w_eleve : ", w_eleve_1,
          "nb_iterations : ", nb_iterations_1,
          "recouvrement : ", recouvrement_r(w_eleve_1, ensemble_d_apprentissage.omega_correspondant)
          )
