from classes.ensemble import Ensemble
from classes.paire import Paire


def lire_blocs(filepath):
    """
    Lit un fichier et retourne une liste de blocs (groupes de 14 lignes).

    Args:
        filepath (str): Le chemin vers le fichier à lire.

    Returns:
        list: Une liste de blocs, chaque bloc est une liste de lignes de vecteurs.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        blocs = []
        i = 0

        while i < len(lines):
            # Lire 14 lignes pour un bloc
            bloc = lines[i:i + 14]
            if len(bloc) < 14:
                break  # Sortir si le bloc n'est pas complet

            blocs.append(bloc)
            i += 14  # Passer au bloc suivant

        return blocs

    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {filepath} : {e}")
        return []


def traiter_bloc_en_paire(bloc):
    """
    Transforme un bloc en une paire de vecteurs et de classification.

    Args:
        bloc (list): Un bloc contenant 14 lignes (vecteurs, nom, classification).

    Returns:
        Paire: Une instance de `Paire` avec le vecteur et la classification.
    """
    vecteur = []

    # Lire les lignes de vecteurs (2ème à 11ème)
    for i in range(2, 12):  # Les premières 10 lignes contiennent les vecteurs
        ligne_donnees = bloc[i].strip('{} \n')
        if ligne_donnees:  # Ignore les lignes vides
            valeurs = [float(val) for val in ligne_donnees.split()]
            vecteur.extend(valeurs)

    # La 13ème ligne contient la classification
    classification_str = bloc[12].strip()  # La ligne vide avant la classification
    # print("classification str ",classification_str)
    classification = 1 if classification_str == '1' else -1
    return Paire(tuple(vecteur), classification)


def construire_ensemble(filepath):
    """
    Crée un Ensemble à partir d'un fichier train ou test.

    Args:
        filepath (str): Le chemin vers le fichier à lire.

    Returns:
        Ensemble: Un objet `Ensemble` contenant toutes les paires lues depuis le fichier.
    """
    ensemble = Ensemble()
    try:
        blocs = lire_blocs(filepath)
        if not blocs:
            return ensemble

        for bloc in blocs:
            paire = traiter_bloc_en_paire(bloc)
            if paire:
                ensemble.ajouter_paire(paire)

    except Exception as e:
        print(f"Erreur lors de la création de l'ensemble depuis {filepath} : {e}")

    return ensemble


# Exemple d'utilisation
train_ensemble = construire_ensemble('tp2/result_sets/train_set.txt')
test_ensemble = construire_ensemble('tp2/result_sets/test_set.txt')

# Affichage pour validation
print("Train Ensemble contient :", len(train_ensemble.elements), "paires.")
print("Test Ensemble contient :", len(test_ensemble.elements), "paires.")
# print(train_ensemble)
# print(test_ensemble)