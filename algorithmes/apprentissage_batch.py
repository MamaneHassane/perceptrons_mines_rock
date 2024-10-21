from helpers.helpers import random_vecteur, vecteur_nul, x_prime, random_omega

# Algorithme d'apprentissage du perceptron version batch
# On retourne le vecteur omega, ensemble des poids, qui va nous servir à classer de nouvelles données
def apprentissage_batch(ensemble, dimension_n, pas_alpha, omega_random):
    # Initialisation du vecteur omega
    omega = omega_random
    # Pas d'apprentissage alpha
    alpha = pas_alpha
    # Nombre d'itérations pour converger
    nb_iterations = 0

    print("Début de l'apprentissage batch...")

    # Tant que l'ensemble n'est pas correctement classé
    while not ensemble.est_correctement_classe(omega):
        # Initialisation de delta_omega à un vecteur nul
        delta_omega = vecteur_nul(dimension_n + 1)

        # Calcul du delta_omega pour toutes les paires mal classées
        for paire in ensemble.elements:
            if not paire.est_bien_predite(omega):  # Si la paire est mal classée
                delta_omega += alpha * (paire.classification_t - paire.classement_paire_y(omega)) * x_prime(
                    paire.vecteur)

        # Mise à jour du vecteur omega après avoir parcouru toutes les paires
        omega += delta_omega
        nb_iterations += 1

        # Affichage intermédiaire pour suivre l'évolution
        print(f"Itération {nb_iterations}: Nouveau omega = {omega}")

    print("Toutes les paires ont été correctement classées.")
    print(f"Omega final : {omega}")
    print(f"Nombre d'itérations nécessaires : {nb_iterations}")

    return omega, nb_iterations
