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
            lines = [line.strip() for line in file if line.strip()]  # Supprime les lignes vides
            i = 0

            while i < len(lines):
                print(f"Iteration {i}:")
                bloc_donnees = []

                # Lire les lignes jusqu'à rencontrer une ligne vide ou un en-tête
                while i < len(lines) and lines[i] and not lines[i].startswith('*') and not lines[i].startswith('CM'):
                    print(f"Ligne {i}: {lines[i]}")  # Affichage pour vérifier les lignes lues
                    bloc_donnees.append(lines[i])
                    i += 1

                # Si on n'a pas suffisamment de lignes pour former un bloc valide, on passe au bloc suivant
                if len(bloc_donnees) < 12:
                    print("Nombre de lignes insuffisant, on passe au bloc suivant")
                    break

                # La 13ème ligne contient la classification
                classification_str = lines[i].strip()
                if classification_str.startswith('*') or classification_str.startswith('CM'):
                    print(f"En-tête trouvé, on saute le bloc")
                    continue  # Ignorer les en-têtes de bloc

                try:
                    classification = int(classification_str)
                    i += 1
                except ValueError:
                    print(f"Erreur : Classification invalide pour le bloc : {classification_str}")
                    continue

                # Convertir les données en un vecteur de floats en combinant toutes les lignes du bloc
                vecteur = []
                for data_line in bloc_donnees:
                    print(f"Processing line: {data_line}")
                    vecteur.extend([float(val) for val in data_line.strip('{}').split(',')])

                # Créer une paire et l'ajouter à l'ensemble
                paire = Paire(vecteur, classification)
                print("Paired created:", paire)
                ensemble.ajouter_paire(paire)

                # Sauter la ligne vide avant de passer au bloc suivant
                i += 1
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {filepath} : {e}")
    return ensemble

# Exemple d'utilisation
if __name__ == "__main__":
    train_ensemble = lire_fichier_ensemble('tp2/result_sets/train_set.txt')
    test_ensemble = lire_fichier_ensemble('tp2/result_sets/test_set.txt')

    # Affichage pour validation
    print("Train Ensemble contient :", len(train_ensemble.elements), "paires.")
    print("Test Ensemble contient :", len(test_ensemble.elements), "paires.")
