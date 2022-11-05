qtd_jogadores_partidas = input().split()
qtd_jogadores = int(qtd_jogadores_partidas[0])
qtd_partidas = int(qtd_jogadores_partidas[1])

contador = 0
qtd_gols = 0
while contador != qtd_jogadores:
    gols = []
    partidasJogadas = input().split()
    for i in partidasJogadas:
        if i == '0':
            contador += 1
        if i != '0':
            gols.append(i)
    print(contador)

