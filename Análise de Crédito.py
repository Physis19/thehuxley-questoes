renda_mensal = float(input())
valor_comprometido = float(input())
limite_emprestimo = renda_mensal * 0.3 - valor_comprometido
if valor_comprometido > renda_mensal * 0.3:
    print('0.00')
else:
    print(f'{limite_emprestimo:.2f}' )
