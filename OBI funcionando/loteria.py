lista_flavinho = []

while len(lista_flavinho) < 6:
    n = int(input('Digite um número: '))
    lista_flavinho.append(n)

print(lista_flavinho)

lista_sorteados = []

while len(lista_sorteados) < 6:
    n = int(input('Digite um número: '))
    lista_sorteados.append(n)

print(lista_sorteados)

iguais = [elemento for elemento in lista_flavinho if elemento in lista_sorteados]
print (iguais)

if len(iguais) >= 6:
    print("sena")
elif len(iguais) >= 5:
    print("quina")
elif len(iguais) >= 4:
    print("quadra")
elif len(iguais) >= 3:
    print("terno")
else:
    print("azar")




