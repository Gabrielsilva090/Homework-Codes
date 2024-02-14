J1 = int(input("Digite quantos jogos você ganhou"))

if J1 > 6 :
    print("Coloque até 6 jogos")
else:
    if J1 >= 5:      
        print("1")
    elif 5 > J1 >= 3:
        print("2")
    elif 3 > J1 >= 1:
        print("3")
    else:
        print("-1")