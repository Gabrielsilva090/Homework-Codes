def contador_destruidos(tabuleiro, disparos): #contagem de navios destruidos
    def eh_valido(linha, coluna): #função para verificar se a posição é valida
        return 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]) 

    def anda_tabuleiro(linha, coluna):  #função para andar pelo tabuleiro
        if not eh_valido(linha, coluna) or tabuleiro[linha][coluna] == '.': #verifica se a posição é valida e se é um navio
            return
        tabuleiro[linha][coluna] = '.'
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dl, dc in direcoes:
            anda_tabuleiro(linha + dl, coluna + dc)

    navios_destruidos = 0
    for disparo in disparos:
        linha, coluna = disparo
        if tabuleiro[linha - 1][coluna - 1] == '#':
            navios_destruidos += 1
            anda_tabuleiro(linha - 1, coluna - 1)

    return navios_destruidos

N, M = map(int, input().split())
tabuleiro = [list(input().strip()) for _ in range(N)]
K = int(input())
disparos = [tuple(map(int, input().split())) for _ in range(K)]

# Chamada da função para contar navios destruídos
navios_destruidos = contador_destruidos(tabuleiro, disparos)
print(navios_destruidos)