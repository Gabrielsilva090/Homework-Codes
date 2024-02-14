peso1 = int(input("Digite o peso da primeira criança: ")) #peso da criança no lado esquerdo da gangorra
c1 = int(input("Digite o tamanho da gangorra no lado esquerdo: ")) #comprimento da gangorra no lado esquerdo
peso2 = int(input("Digite o peso da segunda criança: "))
c2 = int(input("Digite o tamanho da gangorra no lado direito: "))

calc1 = peso1 * c1 #calculo do lado esquerdo da gangorra 
calc2 = peso2 * c2 #calculo do lado direito da gangorra

if calc1 == calc2:
    print("0")
else:
    print("1")

