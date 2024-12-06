import numpy as np
import matplotlib.pyplot as plt
from classes.ensemble_LS import EnsembleLS
from question_2 import apprendre

def calculer_moyennes(N_values, P_values, eta_values, methode_apprentissage, nb_tirages=100):
    results = {eta: np.zeros((len(N_values), len(P_values)), dtype='U25') for eta in eta_values}

    for i, N in enumerate(N_values):
        for j, P in enumerate(P_values):
            for eta in eta_values:
                iterations_total = 0
                recouvrement_total = 0

                for _ in range(nb_tirages):
                    ensemble_d_apprentissage = EnsembleLS(N, P)
                    _, nb_iterations, recouvrement = apprendre(methode_apprentissage, ensemble_d_apprentissage, N, eta)
                    iterations_total += nb_iterations
                    recouvrement_total += recouvrement

                moy_it = iterations_total / nb_tirages
                moy_r = recouvrement_total / nb_tirages
                results[eta][i, j] = f"<IT>={moy_it:.2f}; <R>={moy_r:.2f}"

    return results

def dessiner_tableaux_combines(results, N_values, P_values):
    fig, axes = plt.subplots(1, len(results), figsize=(18, 6))
    fig.suptitle("Moyenne du nombre d'itérations <IT> et du recouvrement <R> pour différentes valeurs de eta", fontsize=16)

    for ax, (eta, data) in zip(axes, results.items()):
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText=data, colLabels=[f'P={p}' for p in P_values], rowLabels=[f'N={n}' for n in N_values],
                         cellLoc='center', loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.2)
        ax.set_title(f"eta = {eta}")

    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    plt.show()

if __name__ == "__main__":
    N_values = [2, 10]
    P_values = [10, 100]
    eta_values = [0.5, 0.25, 0.05]
    methode_apprentissage = 0  # 0 pour batch, 1 pour online

    results = calculer_moyennes(N_values, P_values, eta_values, methode_apprentissage)

    dessiner_tableaux_combines(results, N_values, P_values)