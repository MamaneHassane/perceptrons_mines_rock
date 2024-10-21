import matplotlib.pyplot as plt

# Un ensemble X = { (x(u), t(u)), x vecteur de R^n et t = { -1 / 1 } } est constitué de paire
from classes.paire import Paire

class Ensemble :
    def __init__(self, *args):
        self.elements = []
        for arg in args:
            self.elements.append(arg)
    def __str__(self):
        result = ''
        for paire in self.elements :
            if isinstance(paire, Paire) :
                result += str(paire) + '\n'
        return result
    def dessiner(self):
        # Séparer les points en fonction de leur classification
        points_0 = [paire.vecteur for paire in self.elements if paire.classification_t == -1]
        points_1 = [paire.vecteur for paire in self.elements if paire.classification_t == 1]
        # Convertir les listes de points en coordonnées x et y
        x0 = [point[0] for point in points_0]
        y0 = [point[1] for point in points_0]
        x1 = [point[0] for point in points_1]
        y1 = [point[1] for point in points_1]
        # Dessiner les points sur le graphique
        plt.scatter(x0, y0, color='blue', label='Classification -1')
        plt.scatter(x1, y1, color='red', label='Classification 1')
        # Ajouter des labels et afficher la légende
        plt.xlabel('X1')
        plt.ylabel('X2')
        # plt.legend()
        plt.title('Représentation des points de l\'ensemble')
        plt.grid(True)
        # Afficher le graphe
        plt.show()
    def ajouter_paire(self, vecteur):
        if isinstance(vecteur, Paire):
            self.elements.append(vecteur)
    # Savoir si un ensemble est correctement classé par rappor à un omega donné
    def est_correctement_classe(self, omega):
        for exemple in self.elements:
            if not(exemple.est_bien_predite(omega)):
                return False
        return True