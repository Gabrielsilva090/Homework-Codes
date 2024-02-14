def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return F(n // 2)
    else:
        return F(3 * n + 1)

def G(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + G(n // 2)
    else:
        return 1 + G(3 * n + 1)

def maior_valor_G(A, B):
    max_valor = 0
    for i in range(A, B + 1):
        max_valor = max(max_valor, G(i))
    return max_valor

T = int(input())
if T <= 0 or T > 100:
    exit()

for caso in range(1, T + 1):
    A, B = map(int, input().split())
    if not (1 <= A <= B <= 10**5):
        exit()
    resultado = maior_valor_G(A, B)
    print(f"Caso {caso}: {resultado + 1}")

