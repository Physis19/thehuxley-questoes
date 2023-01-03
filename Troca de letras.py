palavra_tratada = []
while True:
    a = input().strip()
    b = ''
    for i in a:
        i = i.upper()
        i = i.replace('3', 'E')
        i = i.replace('4', 'A')
        i = i.replace('1', 'I')
        i = i.replace('5', 'S')
        palavra_tratada.append(i)
        if i == 'SAIR' or i == 'FIM':
           b = 'terminou'
           break
    if b == 'terminou':
        break

palavra_tratada.pop()
for x in palavra_tratada:
    print(x)
