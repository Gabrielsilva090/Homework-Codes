'''def josephus(n, k):
    sobrevivente = 0
    for i in range(2, n + 1):
        sobrevivente = (sobrevivente + k) % i
    return sobrevivente + 1

n = 1234
k = 233
posicao_sobrevivente = josephus(n, k)
print(f"Case: {posicao_sobrevivente}")'''

def josephus(n, k):
    sobrevivente = 0
    for i in range(2, n + 1):
        sobrevivente = (sobrevivente + k) % i
    return sobrevivente + 1

NC = int(input())
if NC < 1 :
    exit()
elif NC > 30:
    exit()
     
for caso in range(1, NC + 1):
    while True:
        try:
            n, k = map(int, input().split())
            if n < 1 or n > 10000 or k < 1 or k > 1000:
                exit()
            break
        except ValueError:
            exit()

    posicao_sobrevivente = josephus(n, k)

    print(f"Case {caso}: {posicao_sobrevivente}")


