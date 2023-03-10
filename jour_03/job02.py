# Créez une fonction qui parcourt les nombres de 0 à 20, affichez 1 nombre sur 2 dans le terminal.

def numbers():
    numbers = range(21)
    for i in numbers:
        if i % 2 != 0:
            print(i)

print(numbers())