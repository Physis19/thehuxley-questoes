a1, a2, a3, a4 = map(int,input().split())
li1, li2, li3, li4 = map(int,input().split())
ri1, ri2, ri3, ri4 = map(int,input().split())
list_lado_inimigo = [li1, li2, li3, li4]
list_reforco_inimigo = [ri1, ri2, ri3, ri4]
forca_inimiga = []
for elemA, elemB in zip(list_lado_inimigo, list_reforco_inimigo):
    forca_inimiga.append(elemA + elemB)

countAmigos = 0
countInimmigos = 0
countEmpate = 0

if a1 > forca_inimiga[0]:
    countAmigos += 1
elif a1 < forca_inimiga[0]:
    countInimmigos += 1 
else:
    countEmpate += 1 


if a2 > forca_inimiga[1]:
    countAmigos+= 1
elif a2 < forca_inimiga [1]:
    countInimmigos += 1
else:
    countEmpate +=1    


if a3 > forca_inimiga[2]:
    countAmigos+= 1
elif a3 < forca_inimiga [2]:
    countInimmigos += 1
else:
    countEmpate +=1    


if a4 > forca_inimiga[3]:
    countAmigos+= 1
elif a4 < forca_inimiga [3]:
    countInimmigos += 1
else:
    countEmpate +=1    


if  countAmigos > countInimmigos:
    print('Avancar')
elif countInimmigos > countAmigos:
    print('Recuar')
elif countEmpate:
    print('Permanecer')
