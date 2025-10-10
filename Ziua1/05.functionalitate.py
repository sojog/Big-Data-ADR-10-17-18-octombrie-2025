
### PROGRAMARE functionala -> pasarea unei functii ca parametru

print("Hello world!!!")
print(print)

def suma(a, b):
    return a + b

print(suma(2, 3))
print(suma)

### NUMELE unei functie este ca numele unei variabile
adunare = suma
print(adunare)
print(adunare(5, 6))

