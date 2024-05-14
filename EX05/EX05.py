import random

taille = 15
tableau_aléa = [random.randint(1, 100) for _ in range(taille)]

def tri_décroissant(tableau):
    for i in range(len(tableau)):  # Correction de l'itération de i
        for j in range(i+1, len(tableau)):  # Correction de l'itération de j
            if tableau[i] < tableau[j]:
                tableau[i], tableau[j] = tableau[j], tableau[i]
    return tableau

print("Tableau aléatoire:", tableau_aléa)
tableau_trié = tri_décroissant(tableau_aléa)
print("Tableau trié en ordre décroissant:", tableau_trié)
