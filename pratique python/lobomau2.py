TAM_MATRIZ = 250
CERCA = '#'
PASTO = '.'
OVELHA = 'k'
LOBO = 'v'
VAZIO = 'r'
VISITADO = 'b'

def dfs(i, j, fazenda, visitado):
    ovelhas_pasto = lobos_pasto = 0
    busca_valida = 1

    def explore(x, y):
        nonlocal ovelhas_pasto, lobos_pasto, busca_valida
        if fazenda[x][y] == VAZIO:
            busca_valida = 0
            return

        if fazenda[x][y] == CERCA or visitado[x][y]:
            return

        if fazenda[x][y] == OVELHA:
            ovelhas_pasto += 1
        elif fazenda[x][y] == LOBO:
            lobos_pasto += 1

        visitado[x][y] = True

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            explore(x + di, y + dj)

    explore(i, j)

    return ovelhas_pasto, lobos_pasto, busca_valida

def busca_pasto(i, j, fazenda, visitado, ovelhas_vivas, lobos_vivos):
    ovelhas_pasto, lobos_pasto, busca_valida = dfs(i, j, fazenda, visitado)

    if busca_valida:
        if ovelhas_pasto > lobos_pasto:
            ovelhas_vivas += ovelhas_pasto
        else:
            lobos_vivos += lobos_pasto

    return ovelhas_vivas, lobos_vivos

def calcula(num_linhas, num_colunas, fazenda):
    ovelhas_vivas = lobos_vivos = 0

    visitado = [[False for _ in range(num_colunas + 2)] for _ in range(num_linhas + 2)]

    for i in range(1, num_linhas + 1):
        for j in range(1, num_colunas + 1):
            if fazenda[i][j] != CERCA and not visitado[i][j]:
                ovelhas_vivas, lobos_vivos = busca_pasto(i, j, fazenda, visitado, ovelhas_vivas, lobos_vivos)

    return ovelhas_vivas, lobos_vivos

def le_entrada():
    num_linhas, num_colunas = map(int, input().split())

    fazenda = [['r'] * (num_colunas + 2) for _ in range(num_linhas + 2)]

    for i in range(num_linhas + 2):
        fazenda[i][0] = fazenda[i][num_colunas + 1] = VAZIO
    for i in range(num_colunas + 2):
        fazenda[0][i] = fazenda[num_linhas + 1][i] = VAZIO

    for i in range(1, num_linhas + 1):
        fazenda[i][1:num_colunas + 1] = input().strip()

    return num_linhas, num_colunas, fazenda

def main():
    num_linhas, num_colunas, fazenda = le_entrada()
    ovelhas_vivas, lobos_vivos = calcula(num_linhas, num_colunas, fazenda)
    print(f"{ovelhas_vivas} {lobos_vivos}")

if __name__ == "__main__":
    main()