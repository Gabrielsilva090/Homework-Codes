def contar_fatias(K, N, tamanho_fatia):
    total_fatias = 0
    for i in K:
        total_fatias += i // tamanho_fatia
    return total_fatias >= N

def tamanho_maximo(K, N):
    inicio = 1
    fim = max(K)
    resultado = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if contar_fatias(K, N, meio):
            resultado = meio
            inicio = meio + 1
        else:
            fim = meio - 1

    return resultado

N = int(input())
if N <= 1 or N >= 10000:
    exit()
K = int(input())
if K <= 1 or K >= 10000:
    exit()
M = list(map(int, input().split()))
for valor in M:
    if valor <= 1 or valor >= 10000:
        exit()
resultado_final = tamanho_maximo(M, N)
print(resultado_final)