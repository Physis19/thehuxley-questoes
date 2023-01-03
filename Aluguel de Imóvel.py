tipo_imovel = input()
dias_aluguel = int(input())
dias_tv = int(input())
dias_internet = int(input())

standard = (150 * dias_aluguel) + (dias_tv*10) + (dias_internet * 15)
premium = (200 * dias_aluguel) + (dias_tv*10) + (dias_internet * 15)


if tipo_imovel == 'STANDARD':
    print(f'{standard:.2f}')

if tipo_imovel == 'PREMIUM':
    print(f'{premium:.2f}')



