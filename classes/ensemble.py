# Un ensemble X = { (x(u), t(u)), x vecteur de R^n t = { 0 / 1 } } est constitué de paire
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
    def ajouter_paire(self, vecteur):
        if isinstance(vecteur, Paire):
            self.elements.append(vecteur)
    # Savoir si un ensemble est correctement classé
    def est_correctement_classe(self, omega):
        for exemple in self.elements:
            if not(exemple.est_bien_predite(omega)):
                return False
        return True