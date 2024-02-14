def fib(n, lista=None, contador=None):
    if lista is None:
        lista = []
    if contador is None:
        contador = [0]

    contador[0] += 1

    if n==1:
        lista.append(1)
        return 1
    elif n==2:
        lista.append(1)
        return 1
    else: 
        lista.append(n)
        print("Calculando fib(", n , ")")
        return fib(n-1, lista, contador) + fib(n-2, lista, contador)
    
valores = []
contador = [0]
resultado = fib(4, valores, contador)
print("Calculando fib:", valores)
print("fib(4) =", contador[0])
print("Resultado:", resultado)















'''def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        print("Calculando fib(", n, ")")
        return fib(n-1)+fib(n-2)
    
resultado = fib(15)
print("Resultado:", resultado)'''
