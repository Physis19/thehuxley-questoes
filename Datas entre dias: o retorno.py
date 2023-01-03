qtd_elementos = int(input())
valor  = input().split()
lista1 = [int(valor[x]) for x in range(qtd_elementos)]
lista2 = sorted(lista1)

iguais = 0 

elemigual = []
elemindex = []

for x, y in enumerate(lista1):
    if y == lista2[x]:
        iguais += 1 
        
        elemigual.append(y)
        elemindex.append(x+1)
    
print(iguais)

for x, y in enumerate(elemigual):
    print(f'{y} {elemindex[x]}')



