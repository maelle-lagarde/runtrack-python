# Écrire un programme qui affiche le plus petit et le plus grand des éléments dans la liste

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
# on initialise les variables min et max à la première valeur de la liste.
min = L[0]
max = L[0]

# on parcourt la liste et on compare les valeurs avec le min et max.
for i in L:
    if i < min:
        min = i
    if i > max:
        max = i

print("La plus petite valeur est", min)
print("La plus grande valeur est", max)
