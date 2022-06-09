# -*- coding: UTF-8 -*-
#Trouver le minimum de deux nombres
# auteur : rf_it
# programme principal 
print("Donnez deux valeurs entieres :")
x = int(input("n1 = "))
y = int(input("n2 = "))
# ecriture classique :
if x < y:
    plus_petit = x
else:
    plus_petit = y
# ecriture compacte :
#plus_petit = x if x < y else y
print("\nLa plus petite des deux est", plus_petit)
print("\nAu revoir")
