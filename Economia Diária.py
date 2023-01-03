dinheiro_semanal = []
vezesMeta = 0
for i in range (1,8):
    dinheiro_diario = float(input())
    dinheiro_semanal.append(dinheiro_diario)

for x, value in enumerate(dinheiro_semanal):
    if x != len(dinheiro_semanal) - 1:
        if dinheiro_semanal[x+1] - dinheiro_semanal[x] >= 0.5:
            vezesMeta += 1



print( f'R$ {sum(dinheiro_semanal):.2f}' )
print(vezesMeta)


