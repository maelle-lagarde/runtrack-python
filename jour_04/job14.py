my_long_words = ["La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"]

my_short_words = []
word = my_short_words[0]

# créer une fonction qui remplace len, créer une foncton qui remplace append, créer une fonction qui remplace split.
# créer une fonction qui prend en paramètre n et str.
# créer une boucle qui parcourt la chaine et dégage les espaces, + position des espaces.
# puis une seconde boucle qui parcourt le mot en comparant à n (condition).

def longeur(liste):
    compteur = 0
    for i in liste:
        compteur += 1
    return compteur

def ajout(liste, x):
    liste += [x]
    return liste

def separation(str):
    phrase = []
    mot = ""
    for i in str:
        if i != " ":
            mot += i
        else:
            ajout(phrase,mot)
            mot = ""
    return phrase

def my_long_word(n,str):
    mots = separation(str)
    phrase = ""
    for i in mots:
        if longeur(i) > n:
            phrase += i
            phrase += " "
    return phrase

print(my_long_word(3," La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"))


