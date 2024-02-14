def jogo_da_sorte(F, configuracoes):
    for i in range(F):
        mesa = configuracoes[i][0]
        convidados = configuracoes[i][1:]

        rodadas = 0
        vencedor = None

        while rodadas < 1000:
            for j, deck_convidado in enumerate(convidados):
                carta_mesa = mesa.pop(0)
                carta_convidado = deck_convidado.pop(0)

                if carta_mesa == carta_convidado:
                    if not deck_convidado:
                        vencedor = j + 1
                        break
                else:
                    deck_convidado.append(carta_convidado)
                mesa.append(carta_mesa)

            if vencedor is not None:
                break

            rodadas += 1

        print(vencedor if vencedor is not None else 0)


F = int(input())
configuracoes = []

for _ in range(F):
    config_mesa = list(map(int, input().split()))
    deck_convidados = []

    while True:
        deck_convidado = list(map(int, input().split()))
        if deck_convidado[0] == -1:
            break
        deck_convidados.append(deck_convidado)

    configuracoes.append([config_mesa] + deck_convidados)

jogo_da_sorte(F, configuracoes)