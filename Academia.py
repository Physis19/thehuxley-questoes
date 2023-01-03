cadastros = {}

while True:
    nome = input()
    if nome == 'SAIR' or len(cadastros) > 100:
        break
    senha = int(input())
    mensalidade = input()
    cadastros[senha] = nome, mensalidade
    

while True:
    senhas = int(input())
    if senhas == -1:
        break
    indice = 0
   
    for x, y in cadastros.items():
        if senhas == x:
            indice = cadastros.get(x)
            
    if indice == 0:
        print('Seja bem-vindo(a)! Procure a recepção!')
    
    else:
        if indice[1] == 'P':
            print(f'{indice[0]}, seja bem-vindo(a)!')

        else:
            print(f'Não está esquecendo de algo, {indice[0]}? Procure a recepção!')