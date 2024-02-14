def last_digit_fib_calls(n, b):
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
        print("Entrada inválida. Certifique-se de inserir números inteiros separados por espaço.")