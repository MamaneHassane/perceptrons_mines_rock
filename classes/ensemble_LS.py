from classes.ensemble import Ensemble
from classes.paire import Paire
from helpers.helpers import random_omega, random_vecteur, signe_de_x_prime_transposee_omega

class EnsembleLS(Ensemble):
    # Générer un ensemble linéairement séparable avec un équilibre entre les classes
    # Parce que le hasard de la génération peut faire un ensemble avec exclusivement des
    # exemples de classe 0 ou de classe 1, ou 2 exemples d'une classe et 98 de l'autre
    # donc on va essayer d'équilibrer notre génération pour qu'elle soit cohérente
    def __init__(self, dimension_n, norme_p, *args):
        # Générer un vecteur omega qui va servir à générer l'ensemble
        super().__init__(*args)
        self.omega_correspondant = random_omega(dimension_n)
        self.elements = []

        # Générer la moitié des vecteurs pour la classe 1
        for _ in range(norme_p // 2):
            x = random_vecteur(dimension_n)
            # Modifier le vecteur pour qu'il soit classé comme 1
            while not signe_de_x_prime_transposee_omega(x, self.omega_correspondant):
                x = random_vecteur(dimension_n)  # Regénérer jusqu'à obtenir une classification correcte
            self.elements.append(Paire(x, 1))

        # Générer la moitié des vecteurs pour la classe 0
        for _ in range(norme_p // 2):
            x = random_vecteur(dimension_n)
            # Modifier le vecteur pour qu'il soit classé comme 0
            while signe_de_x_prime_transposee_omega(x, self.omega_correspondant):
                x = random_vecteur(dimension_n)  # Regénérer jusqu'à obtenir une classification correcte
            self.elements.append(Paire(x, 0))

    # Afficher un ensemble LS
    @property
    def __str__(self):
        return (super().__str__() +
                '\n' + "omega correspondant : " +
                str(self.omega_correspondant))

# Test en générant un ensemble
ensembleLS = EnsembleLS(2, 1500)
ensembleLS.dessiner()
