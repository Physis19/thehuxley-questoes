p1 = float(input())
p2 = float(input())
p3 = float(input())
p4 = float(input())
tamanhos = [p1, p2, p3, p4]
tamanhos.sort()
final = [tamanhos[0], tamanhos[2], tamanhos[3], tamanhos[1]]
for i in final:
    print(f'{i:.2f}')

