L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
prod = 1

for i in L: #parcourt les éléments, affiche la valeur.
    if i > 25 and i < 90:
        prod *= i # ou prod = prod * i

print(prod)