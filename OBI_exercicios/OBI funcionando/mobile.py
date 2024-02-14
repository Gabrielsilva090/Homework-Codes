
A =  int(input("Digite o valor de A: "))
B =  int(input("Digite o valor de B: "))
C =  int(input("Digite o valor de C: "))
D =  int(input("Digite o valor de D: "))

calculo1 = B + C + D
if calculo1 != A :
    print("N")
else: 
    print("S")

calculo2 = B+ C 
if calculo2 != D :
    print("N")
else:
    print("S")
calculo3 = B
if calculo3 != C :
    print("N")
else: 
    print("S")

print(calculo1, calculo2, calculo3)
