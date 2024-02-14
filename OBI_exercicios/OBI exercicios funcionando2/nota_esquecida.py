
def calcular_b(m, a):
    b = 2 * m - a
    return b 

m = int(input("Digite o valor da média obtida: "))
a = int(input("Digite a primeiro nota: "))
b = calcular_b(m, a)
print(b)
