def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1
    
n = 1234
k = 233
posicao_sobrevivente = josephus(n, k)
print(f"A última pessoa sobrevivente está na posição {posicao_sobrevivente}")