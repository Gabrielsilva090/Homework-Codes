def calcular(N, B, n):
    n.sort()  
    pastas = 0
    esq, dir = 0, N - 1   #direcionar o arquivo maior ou menor par a pasta 

    while esq <= dir:
        if n[esq] + n[dir] <= B:
            esq += 1  
        dir -= 1  
        pastas += 1  

    return pastas

N, B = map(int, input().split())
if N <= 1 or N >= 10**5 or B <= 1 or B >= 10**9:
    exit()
n = list(map(int, input().split()))

resultado = calcular(N, B, n)
print(resultado)