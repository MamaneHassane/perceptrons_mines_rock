from classes.ensemble import Ensemble
from classes.paire import Paire


def lire_fichier_ensemble(filepath):
    """
    Lit un fichier train ou test et crée un objet Ensemble.

    Args:
        filepath (str): Le chemin vers le fichier à lire.

    Returns:
        Ensemble: Un objet contenant toutes les paires lues depuis le fichier.
    """
    ensemble = Ensemble()
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        i = 0
        while i < len(lines):
            ligne = lines[i].strip()
            print(f"Ligne {i}: {ligne}")  # Debug pour voir chaque ligne lue

            if ligne.startswith('*') or ligne.startswith('CM'):
                # Identifie le début d'un bloc
                bloc_id = ligne
                i += 1
                bloc_vecteur = []

                # Lire les vecteurs
                while i < len(lines) and not lines[i].strip().isdigit():
                    vecteur_ligne = lines[i].strip('{} \n')
                    bloc_vecteur.extend([float(val) for val in vecteur_ligne.split()])
                    i += 1

                # Lire la classification
                if i < len(lines) and lines[i].strip().isdigit():
                    classification = int(lines[i].strip())
                    print(f"Bloc {bloc_id}: Classification {classification}")  # Debug pour la classification
                    i += 1
                else:
                    print(f"Erreur : Classification manquante pour le bloc {bloc_id}")
                    continue

                # Ajouter la paire à l'ensemble
                paire = Paire(bloc_vecteur, classification)
                print(f"Paire ajoutée: {paire}")  # Debug pour la paire ajoutée
                ensemble.ajouter_paire(paire)
            else:
                i += 1  # Ignorer les lignes non pertinentes
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {filepath} : {e}")
    return ensemble


# Exemple d'utilisation
train_ensemble = lire_fichier_ensemble('tp2/result_sets/train_set.txt')
test_ensemble = lire_fichier_ensemble('tp2/result_sets/test_set.txt')

# Affichage pour validation
print("Train Ensemble contient :", len(train_ensemble.elements), "paires.")
print("Test Ensemble contient :", len(test_ensemble.elements), "paires.")
