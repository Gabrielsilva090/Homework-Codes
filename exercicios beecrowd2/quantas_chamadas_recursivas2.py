'''def last_digit_fib_calls(n, b):
    if n == 0:
        return 1 % b

    a, b = 1, 1
    count = 2

    while count < n:
        a, b = b, (a + b) % b
        count += 1

    return count % b

test_case = 1
while True:
    try:
        n, b = map(int, input().split())
        if n == 0 and b == 0:
            break

        last_digit = last_digit_fib_calls(n, b)
        print(f"Case {test_case}: {n} {b} {last_digit}")
        test_case += 1
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros separados por espaço.")'''


'''def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        print("Calculando fib(", n, ")")
        return fib(n - 1) + fib(n - 2)
    
print (fib(4))'''

'''def fibonacci_calls(n, b):
    def fib(n, calls):
        if n == 0:
            return 0, 0
        elif n == 1:
            return 1, 0

        fib_n_minus_1, calls_n_minus_1 = fib(n - 1, calls)
        fib_n_minus_2, calls_n_minus_2 = fib(n - 2, calls)

        total_calls = calls_n_minus_1 + calls_n_minus_2 + 2
        return (fib_n_minus_1 + fib_n_minus_2) % b, total_calls % b

    fib_n, calls_n = fib(n, 0)

    return fib_n, calls_n

case = 1
while True:
    n, b = map(int, input().split())
    if n == 0 and b == 0:
        break

    fib_n, calls_n = fibonacci_calls(n, b)
    print(f"Case {case}: {n} {b} {calls_n}")
    case += 1'''

'''def fib(n, b):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n - 1, b) + fib(n - 2, b)) % b

def main():
    case = 1
    while True:
        n = int(input("Informe o valor de n (ou 0 para sair): "))
        if n == 0:
            break
        b = int(input("Informe a base do módulo (b): "))
        result = fib(n, b)

        print(f'case {case}: {n} {b} {result}')
        case += 1

main()'''

'''def mudar_base (n, b):#####
    lista = []

    while n > b:
        r = n % b
        lista = [r] + lista
        n = n // b

    lista = [n] + lista
    return lista 

print(mudar_base(2, 100))'''

'''def last_digit_fib_calls(n, b):
    if n <= 1:
        return n % b

    fib_calls = [0] * (n + 1)
    fib_calls[0] = 0
    fib_calls[1] = 1
    total_calls = 2  # Inicializa o total de chamadas com 2 (fib_calls[0] e fib_calls[1])

    for i in range(2, n + 1):
        fib_calls[i] = (fib_calls[i - 1] + fib_calls[i - 2] + 2) % b
        total_calls += fib_calls[i]  # Atualiza o total de chamadas

    return total_calls % b  # Retorna o último dígito do total de chamadas

case = 1

while True:
    n, b = map(int, input().split())

    if n == 0 and b == 0:
        break

    result = last_digit_fib_calls(n, b)
    print(f"Caso de Teste {case}: {n} {b} {result}")
    case += 1'''

'''def ultimo_digito(n, b):
    lista = []

    while n > b:
        r = n % b
        lista = [r] + lista
        n = n // b

    lista = [n] + lista
    return lista'''

    '''a, b = 0, 1
    total_calls = 2  # Inicializa o total de chamadas com 2 (fib(0) e fib(1))

    for i in range(2, n + 1):
        fib = (a + b) if b != 0 else 0  # Evita divisão por zero
        a, b = b, fib
        total_calls += (fib + 2) if b != 0 else 2  # Evita divisão por zero e atualiza o total de chamadas

    return (total_calls - 3) if b != 0 else 0  # Retorna o último dígito do total de chamadas'''

#caso = 1

'''while True:
    n, b = map(int, input().split())

    if n == 0 and b == 0:
        break

    r = ultimo_digito(n, b)
    print(f"Case {caso}: {n} {b} {r}")
    caso += 1 '''


