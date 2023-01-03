pi = int(input())
ai = int(input())
q = int(input())
af = int(input())

percentual = q/100 #calcular a porcentagem
soma_2valor = pi * percentual #achar a diferença de a2 e a1
valor2 = pi + soma_2valor #achar o a2
razao = valor2 / pi

print(f'{ai} {pi}')
while True:
    ai += 1
    pi = pi * razao
    print(f'{ai} {int(pi)}')
    if ai == af:
        break

    


    
    