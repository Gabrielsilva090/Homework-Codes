def dfs(x, y):
    global contagem_ovelha, contagem_lobo
    if x < 0 or y < 0 or x >= linhas or y >= colunas or visitado[x][y] or fazenda[x][y] == '#':
        return
    visitado[x][y] = True
    if fazenda[x][y] == 'k':
        contagem_ovelha += 1
    elif fazenda[x][y] == 'v':
        contagem_lobo += 1
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

# Lendo as dimensões da fazenda
linhas, colunas = map(int, input().split())

# Lendo a configuração da fazenda
fazenda = []
for i in range(linhas):
    linha = list(input().strip())
    fazenda.append(linha)

# Criando uma matriz para marcar os campos já visitados
visitado = [[False for i in range(colunas)] for i in range(linhas)]
print(visitado)
contagem_ovelha, contagem_lobo = 0, 0

for i in range(linhas):  
    for j in range(colunas):   
        if not visitado[i][j] and fazenda[i][j] != '#':  
            dfs(i, j)  
            if contagem_ovelha > contagem_lobo:
                contagem_lobo = 0
            else:
                contagem_ovelha = 0

# Exibindo a contagem de ovelhas e lobos vivos
print(contagem_ovelha, contagem_lobo)
