# Écrire un programme qui trie dans l’ordre croissant une liste passés en paramètre.

L = [22, 6, 15, 79, 32, 44, 2, 99, 28, 102]

def ascendingOrder(L):
    tampon = 0
    i = 0
    for k in L:
        tampon = tampon + 1
    for i in range(tampon):
        for j in range(i + 1, tampon):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L

print(ascendingOrder(L))