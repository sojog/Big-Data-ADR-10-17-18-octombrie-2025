

def adunare(a, b):
    return a + b    

suma_a_2_numere = lambda a, b: a + b  

print(adunare(2, 3))
print(suma_a_2_numere(2, 3))


def calcul(func, a, b):
    return func(a, b)

print(calcul(adunare, 30, 20))
print(calcul(lambda x, y: x ** y, 2, 4))