'''def max_caju(L, C, M, N, fazenda):
    max_produtividade = 0

    for i in range(L - M + 1):
        for j in range(C - N + 1):
            area = [fazenda[x][j:j + N] for x in range(i, i + M)]
            produtividade = sum(sum(row) for row in area)
            max_produtividade = max(max_produtividade, produtividade)

    return max_produtividade

# Leitura da entrada
L, C, M, N = map(int, input().split())
fazenda = []
for _ in range(L):
    linha = list(map(int, input().split()))
    fazenda.append(linha)

resultado = max_caju(L, C, M, N, fazenda)
print(resultado)'''

'''def calcula_soma_area(i, j, M, N, fazenda):
    soma = 0
    for x in range(i, i + M):
        for y in range(j, j + N):
            soma += fazenda[x][y]
    return soma

def calcula_maximo(L, C, M, N, fazenda):
    max_valor = 0

    for i in range(L - M + 1):
        for j in range(C - N + 1):
            soma_area = calcula_soma_area(i, j, M, N, fazenda)
            max_valor = max(max_valor, soma_area)

    return max_valor

# Leitura da entrada
L, C, M, N = map(int, input().split())
fazenda = []
for _ in range(L):
    linha = list(map(int, input().split()))
    fazenda.append(linha)

resultado = calcula_maximo(L, C, M, N, fazenda)
print(resultado)'''

'''def calcula_soma_area(i, j, M, N, fazenda): 
    soma = 0 # soma dos valores da área
    for x in range(i, i + M): # percorre as linhas da área 
        for y in range(j, j + N):
            soma += fazenda[x][y]
    return soma

def maximo(a, b): 
    if a > b:
        return a
    return b

def calcula_maximo(L, C, M, N, fazenda): # calcula a área de maior produtividade
    max_valor = 0 # valor máximo da área

    for i in range(L - M + 1): # percorre as linhas da fazenda
        for j in range(C - N + 1): # percorre as colunas da fazenda
            soma_area = calcula_soma_area(i, j, M, N, fazenda) # calcula a soma da área
            max_valor = maximo(max_valor, soma_area) # calcula o valor máximo da área

    return max_valor

L, C, M, N = map(int, input().split())
fazenda = [] 
for _ in range(L):
    linha = list(map(int, input().split()))
    fazenda.append(linha) 

resultado = calcula_maximo(L, C, M, N, fazenda) 
print(resultado)'''

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