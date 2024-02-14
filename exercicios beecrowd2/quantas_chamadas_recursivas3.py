'''def ultimo_digito(n, b):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    total_calls = 2  # Inicializa o total de chamadas com 2 (fib(0) e fib(1))

    for i in range(2, n + 1):
        fib = (a + b) % (10 if b == 0 else b)  # Evita divisão por zero
        a, b = b, fib
        total_calls += (fib + 2)

    return total_calls % (10 if b == 0 else b)  # Retorna o último dígito do total de chamadas

caso = 1

while True:
    n, b = map(int, input().split())

    if n == 0 and b == 0:
        break

    r = ultimo_digito(n, b)
    print(f"Case {caso}: {n} {b} {r}")
    caso += 1'''

'''def fibonacci(n):
    if n == 0:
        return n, n 
    fib = [0] * (n+1)
    call = [0] * (n+1)
    fib[1] = 1
    call [1] = 0
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
        call[i] = call[i-1] + call[i-2] + 2
    return call[n], fib[n]

while True:
    i = 0
    i += 1 
    n, b = map(int, input().split())
    if n == 0 and b == 0:
        break
    chamadas, resultado = fibonacci(n)
    digito = (chamadas+1) % b
    print("Case %d: %d %d %d" % (i, n, b, digito))'''

'''def fibonacci_modified(input_number):
    if input_number == 0:
        return input_number, input_number
    fibonacci_sequence = [0] * (input_number + 1)
    call_count = [0] * (input_number + 1)
    fibonacci_sequence[1] = 1
    call_count[1] = 0
    for index in range(2, input_number + 1):
        fibonacci_sequence[index] = fibonacci_sequence[index - 1] + fibonacci_sequence[index - 2]
        call_count[index] = call_count[index - 1] + call_count[index - 2] + 2
    return call_count[input_number], fibonacci_sequence[input_number]

iteration_count = 0

while True:
    iteration_count += 1
    n, b = map(int, input().split())
    if n == 0 and b == 0:
        break
    call_count, result = fibonacci_modified(n)
    digit = (call_count + 1) % b
    print("Case %d: %d %d %d" % (iteration_count, n, b, digit))'''

'''def fibonacci(n):
    if n == 0:
        return n, n
    fib = [0] * (n + 1)
    call = [0] * (n + 1)
    fib[1] = 1
    call[1] = 0
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        call[i] = call[i - 1] + call[i - 2] + 2
    return call[n], fib[n]

for i, line in enumerate(iter(input, '0 0')):
    n, b = map(int, line.split())
    chamadas, resultado = fibonacci(n)
    digito = (chamadas + 1) % b
    print(f"Case {i + 1}: {n} {b} {digito}")'''

def fibonacci(n):
    if n == 0:
        return 0, 0
    if n == 1:
        return 0, 1

    fib = [0] * (n + 1)
    calls = [0] * (n + 1)
    fib[1] = 1
    calls[1] = 0

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        calls[i] = calls[i - 1] + calls[i - 2] + 2

    return calls[n], fib[n]

for i, line in enumerate(iter(input, '0 0')):
    n, b = map(int, line.split())
    chamadas, resultado = fibonacci(n)
    digito = (chamadas + 1) % b
    print(f"Case {i + 1}: {n} {b} {digito}")


