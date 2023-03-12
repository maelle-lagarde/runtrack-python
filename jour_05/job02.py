def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            # affiche la première et la dernière ligne.
            print("|" + "-" * (width - 2) + "|")
        else:
            # affiche les lignes intermédiaires.
            print("|" + " " * (width - 2) + "|")

draw_rectangle(10,3)