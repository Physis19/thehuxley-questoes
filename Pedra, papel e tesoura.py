def vitoria(jog1, jog2):
    if jog1 == 'papel' and jog2 == 'pedra':
        return True
    if jog1 == 'pedra' and jog2 == 'tesoura':
        return True
    if jog1 == 'tesoura' and jog2 == 'papel':
        return True
    return False

qtd_jogadas = int(input())
kyraCount = 0
viniciusCount = 0
jogadainvalidaCount = 0
jogadas_validas = [ 'pedra', 'papel', 'tesoura']
for i in range(qtd_jogadas):
   kyra, vinicius = input().lower(), input().lower()
   if not((kyra in jogadas_validas) and (vinicius in jogadas_validas)):
        jogadainvalidaCount += 1
        continue
    
   if vitoria(kyra, vinicius):
        kyraCount += 1
        
   elif vitoria(vinicius, kyra):
        viniciusCount += 1
        


if kyraCount > viniciusCount:
    print('VINICIUS VAI LAVAR A LOUÇA!')
elif kyraCount < viniciusCount:
    print('KYARA VAI LAVAR A LOUÇA!') 
else:
    print('OS DOIS VÃO LAVAR A LOUÇA JUNTOS!')      