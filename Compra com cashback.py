cartao = input().lower()
valor_compra = float(input())
limite_cashback = float(input())

if cartao == 'infinity':
    cashback = valor_compra * 0.05
    print(f'{cashback:.2f}')
        
elif cartao == 'platinum':
    cashback = valor_compra * 0.025
    if cashback <= limite_cashback:
        print(f'{cashback:.2f}')
    else:
        print(f'{limite_cashback:.2f}')
        
elif cartao == 'gold':
    cashback = valor_compra * 0.01
    if cashback <= limite_cashback:
        print(f'{cashback:.2f}')
    else:
        print(f'{limite_cashback:.2f}')