A = int(input("Qual o tamanho da primeira caixa? "))
B = int(input("Qual o tamanho da segunda caixa? "))
C = int(input("Qual o tamanho da terceira caixa? "))
minha_lista = list()

if A > B:
    minha_lista.append("1")
else: pass
if B > C:
    minha_lista.append("2")
else: pass

minha_lista = [int(elemento) for elemento in minha_lista]

if minha_lista:  # Verifique se a lista não está vazia
    soma_elementos = sum(minha_lista)  # Somar os elementos da lista
    print(soma_elementos)
