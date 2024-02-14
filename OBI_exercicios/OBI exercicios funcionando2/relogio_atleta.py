R = int(input("Digite sua frequência cardíaca em repouso: "))
F = int(input("Digite a sua frequência cardíaca atual: "))
C = int(input("Digite a sua capacidade de oxigenação sanguinea atual: "))

if F == 3*R:
    print("diminuir")
elif C <95:
    print("diminuir")
elif F < 2*R and C > 97:
    print("aumentar")
else:
    print("manter")