a = float(input())
lista_intervalos = [(0,25), (25,50), (50,75), (75,100)]
def intervalos(a):
    for a in lista_intervalos:
        if (0 < a)  or (a > 100):
             print('Fora do intervalo')
    for a in lista_intervalos:
        x = lista_intervalos.index ()

 def esta_no_intervalo(numero: float, intervalo: tuple) -> float:
    if intervalo[0] <= numero <= intervalo[1]:
        print(f'Intervalo [{intervalo[0]},{intervalo[1]}]')
        
        
a = float(input())
lista_de_intervalos = [(0, 25),(25, 50), (50, 75), (75, 100)]

if 0 > a or a > 100:
    print('Fora de intervalo')
else:
    for inter in lista_de_intervalos:
        esta_no_intervalo(a, inter)