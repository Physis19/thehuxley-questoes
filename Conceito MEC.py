livros = int(input())
alunos = int(input())
c = (livros/alunos)
if c >= 0.125:
    print('A')
if 0.111 >= c >= 0.083:
    print( 'B')
if 0.076 >= c >= 0.055:
    print('C')
if c < 0.052:
    print('D')
    
