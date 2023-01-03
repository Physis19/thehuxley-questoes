curvas = []
while True:
    a = input()
    a_convertido = a.lower()
    if a_convertido == '*':
        break
    curvas.append(a_convertido)

direita = 0
esquerda = 0
incorreta = 0

for x in curvas:
    if x =='d' or x == 'dir' or x == 'direita':
        direita += 1
    elif x == 'e'  or x == 'esq' or x == 'esquerda':
        esquerda += 1
    else:
        incorreta += 1


print(f'Esquerda: {esquerda}\nDireita: {direita}\nIncorretas: {incorreta}')


