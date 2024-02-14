lista = []

while len(lista) < 3:
    n = int(input('Digite um número: '))
    lista.append(n)

print(lista)

for i, elemento in enumerate(lista):
        if elemento in lista[i+1:]:
            print(f'Elemento repetido: {elemento}')
            
            