
## First class function
def suma(a, b):
    return a + b

def diferenta(a, b):
    return a - b

def produs(a, b):
    return a * b


def calcul(func, a, b):
    return func(a, b)


for f in (suma, diferenta, produs):
    print(calcul(f, 10, 2))
