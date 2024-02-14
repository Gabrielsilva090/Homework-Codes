'''def mdc(F1,F2):
        if F2>F1:
            F1,F2 = F2,F1
        if F2 == 0:
            return F1
        else:
            return mdc(F2,F1%F2)

lista = []'''

#N = int(input("Digite o valor de vezes que irá ser chamado os testes: "))
'''if N < 1:
    print("Erro, insira um valor válido")
elif N > 3000:
    print("Erro, insira um valor válido")
else:
    lista.append(N)''' 

'''F1 = int(input("Insira a quantidade de figurinhas do primeiro garoto: "))
F2 = int(input("Digite a quantidade de cartas do segundo garoto: "))

if F1 < 1 or F1 > 1000 or F2 < 1 or F2 > 1000:
    print("Erro, valor inválido, tente novamente")
else:
    resultado_mdc = mdc(F1, F2)
    print(resultado_mdc)
    

#print("MDC de", F1, "e", F2, "é:", mdc(F1, F2))




#print(lista)
    












''''''def mdc(a,b):
    if b>a:
        a,b = b,a
    if b == 0:
        return a
    else:
        return mdc(b,a%b)'''
    

#print(mdc(8,12))

'''def mdc(F1, F2):
    if F2 > F1:
        F1, F2 = F2, F1
    if F2 == 0:
        return F1
    else:
        return mdc(F2, F1 % F2)

N = int(input())

for i in range(N):
    F1 = int(input("F1: "))
    F2 = int(input("F2: "))

    if F1 < 1 or F1 > 1000 or F2 < 1 or F2 > 1000:
        print("Erro, Coloque um valor válido")
    else:
        resultado_mdc = mdc(F1, F2)
        print(resultado_mdc)'''

def mdc(F1, F2):
    if F2 > F1:
        F1, F2 = F2, F1
    if F2 == 0:
        return F1
    else:
        return mdc(F2, F1 % F2)

N = int(input())
if 1 >= N or N >= 3000:
    exit()

for i in range(N):
    F1, F2 = map(int, input().split())

    if F1 < 1 or F1 > 1000 or F2 < 1 or F2 > 1000:
        break 
    else:
        resultado_mdc = mdc(F1, F2)
        print(resultado_mdc)
