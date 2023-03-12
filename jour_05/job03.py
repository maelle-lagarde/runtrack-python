def draw_carpet(n):
    # Dessine la première ligne du rectangle avec des tirets et des barres verticales. n-2 car 2 + aux extrémités.
    print("+" ,"-" * (n-2),"+")

    # Dessine les lignes du milieu avec des # et des espaces
    for i in range(n-2):
        print("|", "#" * (n-3-i) + " "+ "#" * i,"|")
    # Dessine la dernière ligne du rectangle avec des tirets et des barres verticales
    print("+" ,"-" * (n-1),"+")

draw_carpet(10)

