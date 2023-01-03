a = float(input())
b = float(input())
c = float(input())
lista = [a, b, c]
media = (a + b + c)/3
lista = [x for x in lista if x > media]
qtd = len(lista)
print(qtd)


