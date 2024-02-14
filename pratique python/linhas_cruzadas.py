def contar_cruzamentos(N, ordem_pregos):
    inv = [0] * (N + 1)
    bit = [0] * (N + 1)
    
    def query(idx):
        soma = 0
        while idx > 0:
            soma += bit[idx]
            idx -= idx & -idx
        return soma

    def update(idx, val):
        while idx <= N:
            bit[idx] += val
            idx += idx & -idx

    mapeamento = {ordem_pregos[i]: i + 1 for i in range(N)}

    total_cruzamentos = 0
    for i in range(N):
        total_cruzamentos += i - query(mapeamento[i + 1])
        update(mapeamento[i + 1], 1)

    return total_cruzamentos

N = int(input())
ordem_pregos = list(map(int, input().split()))

resultado = contar_cruzamentos(N, ordem_pregos)
print(resultado)