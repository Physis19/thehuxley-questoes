a = input()
b = a.replace(' ','')
lista = list(b)
lista_inteiros = []
for x in lista:
    lista_inteiros.append(int(x))

dunga =[]
nando = []

for z in lista_inteiros:
    if z % 2 == 0:
        dunga.append(z)
    if z % 2 != 0:
        nando.append(z)

soma_dunga = sum(dunga)
soma_nando = sum(nando)

if soma_nando > soma_dunga:
    print('Vencedor: Nando')
    print(f'{soma_nando - soma_dunga} Pontos de Vantagem')

elif soma_dunga > soma_nando:
    print('Vencedor: Dunga')
    print(f'{soma_dunga - soma_nando} Pontos de Vantagem')

else:
    print('Empate')
