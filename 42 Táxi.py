def isPrimo(numero):
    divisor = 0

    for x in range(1, numero+1):
        if numero % x == 0:
            divisor += 1
        
    if divisor == 2:
        return numero
    
    else:
        return False

qtd_corrida = int(input())
corridaCount = 0

while corridaCount != qtd_corrida:
    corrida = input().split()
    valor_total = float(corrida[1]) * float(corrida[0])
  
    inteiro = int(valor_total)

    teste = isPrimo(inteiro)

    desconto = 0

    if teste == False:
        print(f'{valor_total:.2f}')

    else:
        desconto = valor_total - (valor_total * 0.42)
        print(f'{desconto:.2f}')

    corridaCount += 1