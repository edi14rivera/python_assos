# Trouver la somme de deux nombres entiers
nbr1 = input('Entrez le premier nombre: ')
nbr2 = input('Entrez le deuxième nombre: ')
# Additionner les deux nombres 
s = int(nbr1) + int(nbr2)
d = int(nbr1) - int(nbr2)
f = int(nbr1) * int(nbr2)
g = int(nbr1) / int(nbr2)
# Afficher la somme
print('La somme de {0} et  {1} est {2}'.format(nbr1, nbr2, s))
print('La sustraction de {0} et  {1} est {2}'.format(nbr1, nbr2, d))
print('La multiplication de {0} et  {1} est {2}'.format(nbr1, nbr2, f))
print('La division de {0} et  {1} est {2}'.format(nbr1, nbr2, g))
