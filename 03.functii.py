
## Python - limbaj imperativ ( Procedural + Orientat Obiect )

def suma(a, b):
    return a + b
print(suma(3, 4))


def cel_mai_mare_numar(*args):
    print("args:", args, type(args))
    maxim = 0
    for i in args:
        if maxim < i:
            maxim = i
    print("valoarea maxima este:", maxim)
    return maxim    

cel_mai_mare_numar(1, 2, 3)
cel_mai_mare_numar(1)
cel_mai_mare_numar(1, 2, 3, 3)
cel_mai_mare_numar()



