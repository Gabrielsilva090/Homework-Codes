def calcula_maximo(L, C, M, N, fazenda):
    max_valor = 0

    soma_acumulada = [[0] * (C + 1) for _ in range(L + 1)]
    for i in range(1, L + 1):
        for j in range(1, C + 1):
            soma_acumulada[i][j] = fazenda[i - 1][j - 1] + soma_acumulada[i - 1][j] + soma_acumulada[i][j - 1] - soma_acumulada[i - 1][j - 1]

    for i in range(L - M + 1):
        for j in range(C - N + 1):
            soma_area = soma_acumulada[i + M][j + N] - soma_acumulada[i][j + N] - soma_acumulada[i + M][j] + soma_acumulada[i][j]
            max_valor = max(max_valor, soma_area)

    return max_valor

L, C, M, N = map(int, input().split())
fazenda = []
for _ in range(L):
    linha = list(map(int, input().split()))
    fazenda.append(linha)

resultado = calcula_maximo(L, C, M, N, fazenda)
print(resultado)