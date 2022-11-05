matriculas = {}

qtd_alunos = int(input())
contador = 0

notas = []

while contador != qtd_alunos:
    dados = input().split('-')
    nota = float(dados[2])
    notas.append(nota)
    matriculas[int(dados[0])] = dados[1], float(dados[2])
    contador += 1 

media_notas = sum(notas)/len(notas)



print('Alunos abaixo da media:')
for x,y in sorted(matriculas.items()):
    if y[1] < media_notas:
        print(f'Matricula: {x} Nome: {y[0]} Nota: {y[1]}')

print('Alunos iguais ou acima da media:')
for x,y in sorted(matriculas.items()):
    if y[1] >= media_notas:
        print(f'Matricula: {x} Nome: {y[0]} Nota: {y[1]}')  

print(f'Media = {media_notas:.2f}')