minha_lista = []

ultimo_numero = None

while True:
    try:
        numero = int(input("Digite um número (ou qualquer outra tecla para parar): "))
        
        if numero == 0:
            if ultimo_numero is not None:
                minha_lista.pop()  #pop para remover o ultimo indice
            break
        
        minha_lista.append(numero)
        ultimo_numero = numero
    except ValueError: #se n for numero quebra
        break

print(minha_lista) #lista de numeros depois que remove o ultimo antes de zero 

