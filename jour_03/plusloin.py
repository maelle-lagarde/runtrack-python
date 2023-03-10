# Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l'inversant. Par exemple, « nikana » deviendra « anakin ».

def reverse_string(x):
  return x[::-1]

new_string = reverse_string("nikana")

print(new_string)