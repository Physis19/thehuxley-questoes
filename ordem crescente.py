a = int (input())
b = int (input ())
c = int (input ())

lista = [a, b, c]
lista.sort()
a, b, c = lista
print(f'{a}\n{b}\n{c}\n')