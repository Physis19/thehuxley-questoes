situacao_ensinomedio = input()
enceja = input()
nota_enceja = int(input())
tipo_escola = input()
renda_pessoal = float(input())
isencao_enem2018 = input()

if situacao_ensinomedio != 'CLD' and situacao_ensinomedio != 'CVC' and situacao_ensinomedio != 'CSC' and situacao_ensinomedio != 'NCC':
    print('Informacao sobre ensino medio invalida')
#1 caso escola publica
elif situacao_ensinomedio == 'CVC' and tipo_escola == 'PUB':
    print('Voce terah direito a isencao')

#2 caso nota ecceja 2018
elif enceja == 's' and nota_enceja >= 400:
    print('Voce terah direito a isencao')

#3 caso escola publica ou privada mais renda 
elif tipo_escola == 'PUB' or tipo_escola == 'PCB' and renda_pessoal <= 1431.00:
    print('Voce terah direito a isencao')

else:
    print('Infelizmente voce nao tem direito a isencao')
