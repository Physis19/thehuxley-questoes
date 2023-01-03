palavra = input().strip().casefold()
palavra_formatada = list(palavra)
qtd_a = palavra_formatada.count('a')
qtd_e = palavra_formatada.count('e')
qtd_i = palavra_formatada.count('i')
qtd_o = palavra_formatada.count('o')
qtd_u = palavra_formatada.count('u')
soma_vogais = (qtd_a + qtd_e + qtd_i + qtd_u + qtd_o)


media = (soma_vogais / len(palavra_formatada)) * 100
print(f'a {qtd_a}\ne {qtd_e}\ni {qtd_i}\no {qtd_o}\nu {qtd_u}')
print(f'{media:.2f}%')





