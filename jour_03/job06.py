s = "abcdefghijklmnopqrstuvwxyz" * 10
n = 1 # nombre de caractère dans la ligne
i = 0 # position du premier caractère

while i + n < len(s):
    print(s[i:i+n]) # entre l'index 0 et l'index +1
    i += n
    n += 1 # +1 caractère