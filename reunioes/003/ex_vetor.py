# vetor

lista1 = []
lista2 = [10,20,30,40,50,60]
lista3 = list()
lista4 = list(range(6))
lista5 = list('que bom!')
lista6 = [0] * 6

print(lista1, len(lista1), type(lista1))
print(lista2, len(lista2), type(lista2))
print(lista3, len(lista3), type(lista3))
print(lista4, len(lista4), type(lista4))
print(lista5, len(lista5), type(lista5))
print(lista6, len(lista6), type(lista6))

print(lista2[1])
print(lista2[1:4])
print(lista2[1:])
print(lista2[:4])

lista2[1] = 200
print(lista2)

# inserir elementos
lista2.append(200)
print(lista2)

lista2.insert(3, 200)
print(lista2)

# contar
print(lista2.count(200))

# verificar posição
print(lista2.index(30))

# verificar se possui
print(30 in lista2)

# remover elementos
lista2.remove(200)
print(lista2)

del(lista2[3:5])
print(lista2)

lista2.clear()
print(lista2)
