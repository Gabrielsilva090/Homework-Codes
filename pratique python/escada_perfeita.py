#usar somatóro com recursividade
degraus = int(input())
pedras = [int(x) for x in input().split()]
soma = 0
for altura in pedras:
    soma += altura
    
b = (((2 * soma) // degraus) + (degraus - 1)) // 2
a = 1 + b - degraus

tira_coloca = 0
movimentos = 0

for i in range(degraus):
    tira_coloca += (pedras[i] - (i + a))
    if pedras[i] > (i + a):
            movimentos += (pedras[i] - (i + a))

if tira_coloca != 0:
    print("-1")
else:
    print(movimentos)





