p1, p2, p3 = map(int, input().split())
w1, w2, w3 = map(int, input().split())
#p1, p2, p3 = map(int, input().split())
willy = [w1, w2, w3]
paes = [p1, p2, p3]
def analise_de_pontos(cartas: list):
    cartas.sort()
    a, b, c = (cartas[0]), (cartas[1]), (cartas[2]) 
    pontuacao = 0
    if a + 1 == b and b + 1 == c:
        pontuacao += a
    if a == b and a == c:
        pontuacao += a
    if a == b and b < c:
        pontuacao += (int(a/2))
    if b == c and a < b:
        pontuacao += (int(b/2))
    if a + b + c == 8:
        pontuacao += 8
    return pontuacao

a = analise_de_pontos(willy)
b = analise_de_pontos(paes)
if a > b:
    print('2')
if b > a:
    print('1')
if a == b:
    print('0')

