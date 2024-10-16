import numpy as np

# Transposée d'un vecteur
def transposee(vecteur_np):
    return vecteur_np.T

# Calculer x' : ajouter x au début d'un vecteur
def x_prime(vecteur_np):
    return transposee(np.insert(vecteur_np, 0, 1))

# Générer un vecteur de n éléments nuls
def vecteur_nul(dimension):
    return np.zeros(dimension)

# Générer un vecteur de n éléments aléatoires entre 0 et 1
def random_vecteur(dimension) :
    return np.random.uniform(0, 1, dimension)


