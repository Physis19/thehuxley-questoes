baseconsultas = {}

while True:
    print('Digite a opcao desejada:\n1- Cadastrar médico.\n2- Cadastrar consulta.\n3- Pesquisar consulta.\n0- Sair do programa.')
    opcao = int(input())
    if opcao == 0:
        break
    
    elif opcao == 1:
        print('Digite codigo do medico:')
        codigo_medico = int(input())
        print('Digite o nome do medico:')
        nome_medico = input()
        print(f'Codigo: {codigo_medico} | Medico: {nome_medico}')
    
    elif opcao == 2:
        print('Digite o codigo da consulta:')
        codigo_consulta = int(input())
        print('Digite o dia da semana:')
        dia_semana = input()
        print('Digite a hora:')
        hora = int(input())
        print('Digite o codigo do medico:')
        codigo_medico_consulta = int(input())
        baseconsultas[codigo_consulta] = codigo_consulta, dia_semana, hora, codigo_medico_consulta
        print(f'Codigo: {codigo_consulta} | Semana: {dia_semana} | Hora: {hora} | Cod. Medico: {codigo_medico_consulta}')
    
    elif opcao == 3:
        print('Digite o codigo da consulta:')
        codigo = int(input())
        for x, y in baseconsultas.items():
            print(f'Codigo: {y[0]} | Semana: {y[1]} | Hora: {y[2]} | Cod. Medico: {y[3]}')

    elif opcao == 0:
        break 