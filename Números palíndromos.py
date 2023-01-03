#a = input()
#b = a [: : -1]
#if a == b:
    #print(f'{b} é um palindromo')
#else:
   # print('Não é palindromo')

palindromos = []
for a in range (1001, 10000):
    conversao = ''
    conversao = str(a)
    valores_convertidos = conversao[: : -1]

    if str(a) == valores_convertidos:
        palindromos.append(valores_convertidos)
    

for a in palindromos:
    print(a)


    




    
    

