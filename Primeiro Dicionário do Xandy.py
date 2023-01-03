chars = ['(', '*', '$', '#', '.', '"', ':']
def remover_especiais(palavra):
    for x in palavra:
        for y in chars:
            if x == y:
                palavra = palavra.replace(x, '')
    return palavra

texto_tratado = []

while True:
    texto = input()
    if texto == '-1':
        break
    frase = remover_especiais(texto)
    frase = frase.split()
    for i in frase:
        i = i.lower()
        texto_tratado.append(i)
        
texto_tratado.sort()
palavras = {}

for i in (texto_tratado):
    vezes = 0

    for k, l in enumerate(texto_tratado):
        if i == l:
            vezes += 1
    
    palavras[i] = vezes


for chaves, valores in palavras.items():
    print(f'{chaves} - {valores}' )
