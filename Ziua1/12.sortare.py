

lista_de_culori = ["verde", "albastru", "alb", "rosu", "negru" ]
print(sorted(lista_de_culori))

print(sorted(lista_de_culori, key=len))

for cuvant in lista_de_culori:
    print(cuvant, " lungime: ", len(cuvant))