# Créez une fonction qui affiche tous les nombres de 0 à 100 compris SAUF 26, 37, 88.

def numbers():
    numbers = range(101)
    for i in numbers:
        if i != 26 and i != 37 and i != 88:
            print(i)

print(numbers())
