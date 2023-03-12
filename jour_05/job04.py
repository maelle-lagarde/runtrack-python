def code_cesar(message, decalage):
    message_chiffre = ""
    for lettre in message:
        # on vérifie si la lettre est alphabétique.
        if lettre.isalpha():
            # on convertit en miniscule la lettre.
            lettre = lettre.lower()
            # on applique le décalage en veillant au dépassement de z à a.
            lettre_chiffree = chr((ord(lettre) - 97 + decalage) % 26 + 97)
            # on ajoute la lettre chiffrée au message chiffré.
            message_chiffre += lettre_chiffree
        else:
            message_chiffre += lettre
    return message_chiffre

print(code_cesar("ave cesar", 3))