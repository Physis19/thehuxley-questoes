f = input().strip().casefold()
palavra = f.split()
palavra_junta = ''.join(palavra)
b = palavra_junta [: : -1]

if palavra_junta == b:
    print('SIM')
else:
    print('NAO')

