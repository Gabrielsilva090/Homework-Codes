def destruidos(tabuleiro, disparos):
    def afundar_navio(linha, coluna):
        if linha < 0 or linha >= len(tabuleiro) or coluna < 0 or coluna >= len(tabuleiro[0]) or tabuleiro[linha][coluna] == '.':
            return False  
        tabuleiro[linha][coluna] = '.'
        afundar_navio(linha + 1, coluna)
        afundar_navio(linha - 1, coluna)
        afundar_navio(linha, coluna + 1)
        afundar_navio(linha, coluna - 1)
        return True  

    navios_destruidos = 0
    for disparo in disparos:
        linha, coluna = disparo
        if tabuleiro[linha - 1][coluna - 1] == '#':
            if afundar_navio(linha - 1, coluna - 1):
                navios_destruidos += 1

    return navios_destruidos

N, M = map(int, input().split())
tabuleiro = [list(input().strip()) for i in range(N)]
K = int(input())
disparos = [tuple(map(int, input().split())) for i in range(K)]

navios_destruidos = destruidos(tabuleiro, disparos)
print(navios_destruidos)