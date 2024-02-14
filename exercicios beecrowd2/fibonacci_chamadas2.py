'''def fib(n, lista=None, contador=None):
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
print("Resultado:", resultado)'''




'''def fib (n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        print("Calculando fib(", n, ")")
        return fib(n-1)+fib(n-2)

print(fib(5))'''

'''def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
        
def menu():
    n = int(input('Exibir ate o termo (maior que 2): '))

    for val in range(1,n+1):
        print(fibo(val))
    
while True:
    menu()'''

'''def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def menu():
    n = int(input('Exibir até o termo (maior que 2): '))

    fibo_list = []  # Inicialize uma lista vazia para armazenar os resultados

    for val in range(1, n + 1):
        fibo_list.append(fibo(val))  # Adicione cada resultado à lista

    return fibo_list  # Retorne a lista com os resultados

while True:
    result_list = menu()
    chamadas = len(result_list)
    print(f"Fib", chamadas)'''











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


'''def fib(n):
    global rec 
    rec += 1
    if n <= 1:
        return n
    else: 
        return fib(n-1) + fib(n-2)
    
rec = 0
a = int(input("Digite um número: "))

print (fib(a))
print (rec - 1)'''

def fib(n):
    global rec
    rec += 1
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

rec = 0
a = int(input())

if a <= 1 or a >= 39:
    brake = True
else:
    result = fib(a)
    print(f"fib({a}) = {rec - 1} calls = {result}")