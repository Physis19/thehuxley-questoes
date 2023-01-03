consumo_postos = {}
diferenca_postos = {}

while True:
    informacao = input().split()
    
    if informacao[0] == 'FIM':
        break
    #if informacao2[0] == 'FIM':
        #break
    
    odometro = int(informacao[0])
    volume = float(informacao[1])
    posto = informacao[2]
    
    diferenca_postos[odometro] = volume
    dictOdometro = list(diferenca_postos.keys())
    dictVolume = list(diferenca_postos.values())

    lista_distancias = []
    lista_consumo = []

    if len(diferenca_postos) > 1:
        for x in range(len(dictOdometro)):
            if x != len(dictOdometro) - 1:
                distanciaPercorrida = dictOdometro[x+1] - dictOdometro[x]
                lista_distancias.append(distanciaPercorrida)
               #print(distanciaPercorrida)
    
    for x, y in enumerate(lista_distancias):
        consumo = y/ dictVolume[x]
        lista_consumo.append(consumo)
        print(lista_distancias)
            
        #print(consumo) 
                
    #print(media)
    #print(odometro, odometro2, volume, volume2, posto, posto2)

