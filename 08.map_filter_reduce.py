
## MAPARE fiecarui element folosind o functie
lista = [22, 33, 44, 55, 66]

def transforma(x):
    return x + x  # noul X

print(list(map(lambda x: x/2 ,lista)))
print(list(map(transforma,lista)))
print(list(map(str,lista)))


### FILTER - filtrarea unor elemente dupa o functie
def conditie_de_filtrare(x):
    return True if x % 2 == 0 else False # True or False

print(list(filter(conditie_de_filtrare, lista)))
print(list(filter(lambda x: x > 40, lista)))


### REDUCE - reduce toata lista la unul singur
from functools import reduce

# [22, 33, 44, 55, 66]
#   [22, 33] -> rezultat
#       [ rezultat, 44, 55, 66]
#           [rezultat, 44] -> nou_rezultat
#               [noul_rezultat, 55] -> 


lista = [22, 33, 44, 55, 66]
def adunare(a, b):
    return a + b

reduce()

