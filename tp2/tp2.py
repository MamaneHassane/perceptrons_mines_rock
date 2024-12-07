from classes.ensemble import Ensemble
from classes.paire import Paire


def lire_blocs(filepath):
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
    vecteur = []
    # Lire les lignes de vecteurs (2ème à 11ème)
    for i in range(1, 12):  # On commence à la 1ère ligne (1) jusqu'à la 11ème
        ligne_donnees = bloc[i].strip('{} \n')
        if ligne_donnees:  # Ignore les lignes vides
            valeurs = [float(val) for val in ligne_donnees.split()]
            vecteur.extend(valeurs)

    # La 13ème ligne contient la classification
    classification_str = bloc[12].strip()  # La ligne vide avant la classification
    classification = 1 if classification_str == '1' else -1

    return Paire(tuple(vecteur), classification)


def construire_ensemble(filepath):
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


def creer_all_ensemble(train_filepath, test_filepath):
    train_ensemble = construire_ensemble(train_filepath)
    test_ensemble = construire_ensemble(test_filepath)

    # Créer un nouvel ensemble qui combine les paires des deux ensembles
    all_ensemble = Ensemble(*train_ensemble.elements, *test_ensemble.elements)

    return all_ensemble


# Exemple d'utilisation
all_ensemble = creer_all_ensemble('tp2/result_sets/train_set.txt', 'tp2/result_sets/test_set.txt')

# Affichage pour validation
print("All Ensemble contient :", len(all_ensemble.elements), "paires.")
print(all_ensemble)