la1, la2, la3, la4 = map(int,input().split())
li1, li2, li3, li4 = map(int,input().split())
ri1, ri2, ri3, ri4 = map(int,input().split())
list_lado_amigo = [la1, la2, la3, la4]
list_lado_inimigo = [li1, li2, li3, li4]
list_reforco_inimigo = [ri1, ri2, ri3, ri4]
forca_inimiga = []
for elemA, elemB in zip(list_lado_inimigo, list_reforco_inimigo):
    forca_inimiga.append(elemA + elemB)
for a, b, c in list_lado_amigo:
    for j, k, l in forca_inimiga:
        if (a, b, c > (j, k, l)/2):
            print('Avancar')
        elif (j, k, l > (a, b, c)/2):
            print('Recuar')
        else:
            print('Permanecer')

#total_de_aliados = sum(list_lado_amigo)
#total_de_inimigos = sum(forca_inimiga)


