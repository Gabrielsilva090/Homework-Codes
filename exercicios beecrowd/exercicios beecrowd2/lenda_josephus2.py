def josephus(n, k):
    sobrevivente = 0
    for i in range(2, n + 1):
        sobrevivente = (sobrevivente + k) % i
    return sobrevivente + 1

n = 6
k = 3
posicao_sobrevivente = josephus(n, k)
print(f"A última pessoa sobrevivente está na posição {posicao_sobrevivente}")