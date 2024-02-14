def fib(n):
    global rec 
    rec += 1
    if n <= 1:
        return n
    else: 
        return fib(n-1) + fib(n-2)
    
rec = 0
a = int(input("Digite um número: "))
if a <= 1 or a >= 39:
    print("Erro, coloque um valor válido")
print (fib(a))
print (rec - 1)