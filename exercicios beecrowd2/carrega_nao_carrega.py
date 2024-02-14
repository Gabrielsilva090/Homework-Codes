val1, val2 = input().split()
val1 = bin(abs(int(val1)))
val2 = bin(abs(int(val2)))

val1 = val1[2:]
val2 = val2[2:]

if len(val1) > len(val2):
    val2 = val2.zfill(len(val1))

if len(val2) > len(val1):
    val1 = val1.zfill(len(val2))

a = list(val1)
b = list(val2)
lista = []
d = ""

for i in range(len(val1)):
    if val1[i] == val2[i]:
        lista.append("0")
    else:
        lista.append("1")

for i in range(len(lista)):
    d += lista[i]

d = int(d, 2)
print(d)
