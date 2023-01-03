voos = {}
contador = 0


while contador < 2:
    cadastro_voos = input().split()
    voos[cadastro_voos[0]] = cadastro_voos[1]
    contador += 1


listadisponivel = []
while True:
    pessoas = input().split()
    if pessoas[0] == '9999':
        break

    contador = 0

    for keys, values in voos.items():
        contador_2 = 0
        
        if pessoas[1] ==  keys: 
            contador_2 += 1
        if values != '0':
            print(pessoas[0])

            contador = int(values) - 1

            voos[pessoas[1]] = contador

        else:
            print('INDISPONIVEL')
    if contador_2 == 0:
        print('INDISPONIVEL')
