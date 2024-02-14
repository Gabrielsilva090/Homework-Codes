def calcular_classificacao(N, M, resultados):
    classificacao = {i: [0, 0, 0] for i in range(1, N + 1)}

    for modalidade in resultados:
        ouro, prata, bronze = modalidade
        classificacao[ouro][0] += 1
        classificacao[prata][1] += 1
        classificacao[bronze][2] += 1

    classificacao_ordenada = sorted(classificacao.keys(), key=lambda x: (classificacao[x][0], classificacao[x][1], classificacao[x][2], -x), reverse=True)

    print(" ".join(map(str, classificacao_ordenada)))


N, M = map(int, input().split())
resultados = [list(map(int, input().split())) for _ in range(M)]

calcular_classificacao(N, M, resultados)